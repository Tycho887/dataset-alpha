"""
Source Manager
==============
Handles downloading, caching, and registry management for 100+ data sources.
Supports both HTML scraping and Git repository cloning.
"""

import json
import re
import asyncio
import logging
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import List, Dict, Optional
from datetime import datetime
from urllib.parse import urlparse

import aiohttp
from bs4 import BeautifulSoup

logger = logging.getLogger("SourceManager")


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class Source:
    """Represents a single data source in the registry."""
    id: str
    name: str
    type: str                      # "html" or "git"
    url: str
    category: str
    force_reprocess: bool = False
    last_processed: Optional[str] = None
    branch: Optional[str] = "main"
    depth: int = 1
    status: str = "pending"        # pending, downloaded, processed, failed
    error: Optional[str] = None


# =============================================================================
# REGISTRY MANAGEMENT
# =============================================================================

class SourceRegistry:
    """
    Manages the source_registry.json file.
    Tracks which sources have been processed, failed, or need reprocessing.
    """

    def __init__(self, registry_path: str = "source_registry.json"):
        self.registry_path = Path(registry_path)
        self.sources: List[Source] = []
        self._load()

    def _load(self):
        """Load registry from disk or create empty."""
        if not self.registry_path.exists():
            logger.info(f"Creating new registry: {self.registry_path}")
            self.save()
            return

        with open(self.registry_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.sources = [Source(**s) for s in data.get("sources", [])]

        logger.info(f"Loaded registry with {len(self.sources)} sources")

    def save(self):
        """Persist registry to disk."""
        with open(self.registry_path, "w", encoding="utf-8") as f:
            json.dump(
                {"sources": [asdict(s) for s in self.sources]},
                f,
                indent=2,
                ensure_ascii=False,
                default=str
            )

    def get_pending(self) -> List[Source]:
        """
        Return sources that need processing.
        A source needs processing if:
        - force_reprocess is True
        - last_processed is None (never processed)
        - status is failed
        """
        pending = []
        for s in self.sources:
            needs_processing = (
                s.force_reprocess or
                s.last_processed is None or
                s.status in ("pending", "failed")
            )
            if needs_processing:
                pending.append(s)

        logger.info(f"Pending sources: {len(pending)}/{len(self.sources)}")
        return pending

    def mark_processed(self, source_id: str, success: bool = True, 
                       error: Optional[str] = None):
        """Update source status after processing attempt."""
        for s in self.sources:
            if s.id == source_id:
                s.last_processed = datetime.utcnow().isoformat() + "Z"
                s.status = "processed" if success else "failed"
                s.error = error
                if success:
                    s.force_reprocess = False
                break
        self.save()

    def get_by_id(self, source_id: str) -> Optional[Source]:
        """Retrieve a source by its ID."""
        for s in self.sources:
            if s.id == source_id:
                return s
        return None

    def add_source(self, source: Source):
        """Add a new source to the registry."""
        # Prevent duplicates by URL
        if any(s.url == source.url for s in self.sources):
            logger.warning(f"Source with URL {source.url} already exists. Skipping.")
            return
        self.sources.append(source)
        self.save()

    def get_summary(self) -> Dict[str, int]:
        """Return counts by status."""
        summary = {"total": len(self.sources), "pending": 0, 
                   "processed": 0, "failed": 0, "downloaded": 0}
        for s in self.sources:
            if s.status in summary:
                summary[s.status] += 1
        return summary


# =============================================================================
# DOWNLOAD MANAGER
# =============================================================================

class SourceDownloader:
    """
    Downloads source content from the web.
    - HTML sources: scraped and saved as clean text files
    - Git sources: cloned or pulled to local directories
    """

    def __init__(self, data_lake_root: str = "./data_lake",
                 max_concurrent_downloads: int = 5,
                 request_delay: float = 1.0):
        self.data_lake_root = Path(data_lake_root)
        self.data_lake_root.mkdir(parents=True, exist_ok=True)
        self.max_concurrent = max_concurrent_downloads
        self.request_delay = request_delay
        self._semaphore: Optional[asyncio.Semaphore] = None
        self._session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        self._semaphore = asyncio.Semaphore(self.max_concurrent)
        timeout = aiohttp.ClientTimeout(total=60, connect=10)
        self._session = aiohttp.ClientSession(
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36 "
                    "(EUDigitalKnowledgeBot/1.0; Research Purpose)"
                ),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "DNT": "1",
                "Connection": "keep-alive",
            },
            timeout=timeout,
            raise_for_status=True
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            await self._session.close()

    @staticmethod
    def sanitize_name(name: str, max_len: int = 50) -> str:
        """
        Convert a descriptive name to a filesystem-safe directory name.
        - Replaces unsafe characters with underscores
        - Collapses whitespace
        - Truncates to max_len characters
        """
        safe = re.sub(r"[^\w\s-]", "_", name)
        safe = re.sub(r"[\s]+", "_", safe).strip("_")
        return safe[:max_len]

    def get_source_dir(self, source: Source) -> Path:
        """Get the local directory path for a source."""
        safe_name = self.sanitize_name(source.name)
        return self.data_lake_root / safe_name

    async def download(self, source: Source) -> Path:
        """Download a source and return its local directory path."""
        source_dir = self.get_source_dir(source)
        source_dir.mkdir(parents=True, exist_ok=True)

        if source.type == "html":
            return await self._download_html(source, source_dir)
        elif source.type == "git":
            return await self._download_git(source, source_dir)
        else:
            raise ValueError(f"Unknown source type: {source.type}")

    async def _download_html(self, source: Source, output_dir: Path) -> Path:
        """Scrape an HTML page and save clean text content."""
        if not self._session:
            raise RuntimeError("Downloader must be used as async context manager")

        async with self._semaphore:
            logger.info(f"[HTML] Scraping: {source.url}")

            # Respectful delay between requests
            await asyncio.sleep(self.request_delay)

            try:
                async with self._session.get(source.url) as resp:
                    html = await resp.text()

                    soup = BeautifulSoup(html, "html.parser")

                    # Extract metadata
                    title = ""
                    if soup.title and soup.title.string:
                        title = soup.title.string.strip()

                    # Try to find canonical URL
                    canonical = ""
                    canonical_tag = soup.find("link", rel="canonical")
                    if canonical_tag and canonical_tag.get("href"):
                        canonical = canonical_tag["href"]

                    # Remove noise elements
                    noise_tags = [
                        "script", "style", "nav", "footer", "header",
                        "aside", "iframe", "noscript", "svg", "canvas",
                        "form", "button", "input", "select", "textarea"
                    ]
                    for tag_name in noise_tags:
                        for tag in soup.find_all(tag_name):
                            tag.decompose()

                    # Remove common ad/tracking containers
                    for cls in ["advertisement", "ads", "cookie-banner", 
                                "newsletter-signup", "social-share"]:
                        for tag in soup.find_all(class_=re.compile(cls, re.I)):
                            tag.decompose()

                    # Extract main content using common selectors
                    main_content = None
                    selectors = [
                        ("main", {}),
                        ("article", {}),
                        ("div", {"id": re.compile(r"content|main|body", re.I)}),
                        ("div", {"class": re.compile(r"content|main|body|markdown-body|entry-content", re.I)}),
                        ("section", {"class": re.compile(r"content|main", re.I)}),
                    ]

                    for tag, attrs in selectors:
                        main_content = soup.find(tag, attrs)
                        if main_content:
                            break

                    if main_content:
                        text = main_content.get_text(separator="\n", strip=True)
                    else:
                        # Fallback to body
                        body = soup.find("body")
                        if body:
                            text = body.get_text(separator="\n", strip=True)
                        else:
                            text = soup.get_text(separator="\n", strip=True)

                    # Clean up excessive whitespace while preserving structure
                    text = re.sub(r"\n{3,}", "\n\n", text)
                    text = re.sub(r"[ \t]+", " ", text)
                    text = text.strip()

                    # Save metadata + content
                    output_file = output_dir / "content.txt"
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(f"# Source Metadata\n")
                        f.write(f"source_url: {source.url}\n")
                        f.write(f"canonical_url: {canonical or source.url}\n")
                        f.write(f"title: {title}\n")
                        f.write(f"category: {source.category}\n")
                        f.write(f"scraped_at: {datetime.utcnow().isoformat()}Z\n")
                        f.write(f"content_length: {len(text)}\n")
                        f.write("=" * 80 + "\n\n")
                        f.write(text)

                    # Also save raw HTML for reference
                    raw_file = output_dir / "raw.html"
                    with open(raw_file, "w", encoding="utf-8") as f:
                        f.write(html)

                    logger.info(f"[HTML] Saved {len(text)} chars to {output_file}")
                    return output_dir

            except aiohttp.ClientError as e:
                logger.error(f"[HTML] HTTP error for {source.url}: {e}")
                raise
            except Exception as e:
                logger.error(f"[HTML] Unexpected error scraping {source.url}: {e}")
                raise

    async def _download_git(self, source: Source, output_dir: Path) -> Path:
        """Clone or pull a Git repository."""
        async with self._semaphore:
            logger.info(f"[GIT] Processing: {source.url}")

            git_dir = output_dir / ".git"

            try:
                if git_dir.exists():
                    # Repository exists — pull latest
                    logger.info(f"[GIT] Repo exists, pulling: {output_dir}")
                    proc = await asyncio.create_subprocess_exec(
                        "git", "-C", str(output_dir), "pull", "--ff-only",
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE
                    )
                    stdout, stderr = await proc.communicate()

                    if proc.returncode != 0:
                        err_msg = stderr.decode().strip()
                        # If pull fails (e.g., diverged), do a fresh clone
                        logger.warning(f"[GIT] Pull failed: {err_msg}. Re-cloning...")
                        import shutil
                        shutil.rmtree(output_dir)
                        output_dir.mkdir(parents=True, exist_ok=True)
                        return await self._git_clone(source, output_dir)
                    else:
                        logger.info(f"[GIT] Pull complete: {output_dir}")
                else:
                    # Fresh clone
                    return await self._git_clone(source, output_dir)

                return output_dir

            except Exception as e:
                logger.error(f"[GIT] Error processing {source.url}: {e}")
                raise

    async def _git_clone(self, source: Source, output_dir: Path) -> Path:
        """Execute git clone command."""
        cmd = [
            "git", "clone",
            "--depth", str(source.depth),
            "--branch", source.branch or "main",
            "--single-branch",
            source.url, str(output_dir)
        ]

        logger.info(f"[GIT] Cloning: {' '.join(cmd)}")

        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()

        if proc.returncode != 0:
            err_msg = stderr.decode().strip()
            raise RuntimeError(f"Git clone failed: {err_msg}")

        logger.info(f"[GIT] Clone complete: {output_dir}")
        return output_dir
