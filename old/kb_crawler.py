"""
Simplified Knowledge-Base Crawler for Azure Agent RAG
======================================================
Point at a seed URL (e.g. https://openid.net/developers/specs/)
and crawl outward. For every page we store:
  1. meta.json   – URL, title, crawl time, links, etc.
  2. content.md  – clean extracted text (trafilatura + BS4 fallback)
  3. raw.html    – original HTML for re-processing later
  4. chunks.jsonl– overlapping text chunks with source references

Dependencies:
    pip install httpx beautifulsoup4 trafilatura lxml

Usage:
    python kb_crawler.py --seeds https://openid.net/developers/specs/
"""

import argparse
import asyncio
import hashlib
import json
import logging
import re
import signal
import sys
import time
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urldefrag, urljoin, urlparse

import httpx
from bs4 import BeautifulSoup

try:
    import trafilatura
except ImportError:
    trafilatura = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s"
)
logger = logging.getLogger("kb_crawler")


# =============================================================================
# CONFIG
# =============================================================================

@dataclass
class Config:
    seeds: List[str]
    out_dir: str = "./kb_output"
    max_depth: int = 2
    max_pages: int = 500
    max_per_domain: int = 100
    concurrency: int = 6
    delay: float = 1.0          # seconds between requests to same domain
    timeout: int = 30
    retries: int = 2
    min_text_len: int = 200     # ignore pages with less extracted text
    chunk_size: int = 800       # target chunk size in words
    chunk_overlap: int = 100    # word overlap between chunks

    # Simple keyword gate – if a cross-domain link contains any of these,
    # we follow it. Same-domain links are always followed.
    topic_keywords: Set[str] = field(default_factory=lambda: {
        "openid", "eidas", "credential", "verifiable", "identity",
        "wallet", "oid4vci", "oid4vp", "sd-jwt", "oauth", "iso 18013",
        "trust framework", "digital identity", "pid", "presentation",
        "issuance", "qualified", "electronic signature", "reference framework",
        "interoperability", "conformance", "architecture", "specification",
        "standard", "protocol", "authorization", "authentication", "token",
        "did", "decentralized identifier", "mdoc", "mso", "cbor", "cose",
        "jwk", "jws", "jwe", "jwt", "pki", "cryptographic", "encryption",
        "gdpr", "psd2", "payment services", "strong customer authentication",
        "privacy", "data protection", "regulation", "directive", "compliance",
        "implementation", "api", "endpoint", "rest", "json", "schema",
        "mobile driving licence", "mDL", "iso/iec 18013", "haip", "par"
    })

    blocked_domains: Set[str] = field(default_factory=lambda: {
        "facebook.com", "twitter.com", "x.com", "linkedin.com",
        "youtube.com", "instagram.com", "tiktok.com", "reddit.com",
        "pinterest.com", "tumblr.com", "medium.com", "google.com",
        "bing.com", "yahoo.com", "doubleclick.net", "googletagmanager.com",
        "google-analytics.com", "cloudflareinsights.com"
    })

    blocked_extensions: Set[str] = field(default_factory=lambda: {
        ".pdf", ".zip", ".tar", ".gz", ".rar", ".7z",
        ".exe", ".bin", ".dmg", ".pkg", ".deb", ".rpm",
        ".jpg", ".jpeg", ".png", ".gif", ".svg", ".ico", ".webp",
        ".mp4", ".mp3", ".avi", ".mov", ".wmv",
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".css", ".js", ".xml", ".woff", ".woff2", ".ttf", ".eot"
    })


# =============================================================================
# HELPERS
# =============================================================================

def normalize_url(url: str) -> str:
    url, _ = urldefrag(url)
    url = url.rstrip("/")
    if url.startswith("http://"):
        url = "https://" + url[7:]
    return url


def safe_filename(url: str) -> str:
    """Create a filesystem-safe name from URL path."""
    parsed = urlparse(url)
    path = parsed.path.strip("/") or "index"
    name = re.sub(r"[^\w\-_.]", "_", path)[-120:]  # keep last 120 chars
    if not name:
        name = "index"
    # append short hash to avoid collisions on similar paths
    h = hashlib.md5(url.encode()).hexdigest()[:6]
    return f"{name}_{h}"


def is_blocked(url: str, cfg: Config) -> bool:
    parsed = urlparse(url)
    ext = Path(parsed.path).suffix.lower()
    if ext in cfg.blocked_extensions:
        return True
    if any(bd in parsed.netloc.lower() for bd in cfg.blocked_domains):
        return True
    return False


def should_follow(url: str, base_domain: str, cfg: Config) -> bool:
    """Decide whether to follow a link.
    Same domain = always (unless blocked).
    Cross domain = only if it looks relevant by keyword.
    """
    if is_blocked(url, cfg):
        return False
    parsed = urlparse(url)
    if parsed.netloc == base_domain:
        return True
    combined = (parsed.path + " " + parsed.query).lower()
    return any(kw in combined for kw in cfg.topic_keywords)


# =============================================================================
# CONTENT EXTRACTION
# =============================================================================

class Extractor:
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def extract(self, html: str, url: str) -> Optional[Dict]:
        """Return dict with title, text, author, date, word_count or None."""
        # Try trafilatura first
        if trafilatura is not None:
            try:
                text = trafilatura.extract(
                    html,
                    url=url,
                    output_format="markdown",
                    include_tables=True,
                    include_comments=False,
                    deduplicate=True,
                    target_language="en",
                )
                meta = trafilatura.extract_metadata(html, url=url)
                if text and len(text) >= self.cfg.min_text_len:
                    return {
                        "title": getattr(meta, "title", "") or "",
                        "author": getattr(meta, "author", "") or "",
                        "date": getattr(meta, "date", "") or "",
                        "text": text,
                        "word_count": len(text.split()),
                        "extractor": "trafilatura",
                    }
            except Exception as e:
                logger.debug(f"trafilatura failed for {url}: {e}")

        # Fallback to BeautifulSoup
        try:
            soup = BeautifulSoup(html, "lxml")
            for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
                tag.decompose()
            main = (
                soup.find("main")
                or soup.find("article")
                or soup.find("div", class_=re.compile("content|main|article"))
            )
            body = main.get_text(separator="\n", strip=True) if main else soup.get_text(separator="\n", strip=True)
            body = re.sub(r"\n{3,}", "\n\n", body)
            if len(body) >= self.cfg.min_text_len:
                return {
                    "title": soup.title.get_text(strip=True) if soup.title else "",
                    "author": "",
                    "date": "",
                    "text": body,
                    "word_count": len(body.split()),
                    "extractor": "beautifulsoup",
                }
        except Exception as e:
            logger.debug(f"BS4 fallback failed for {url}: {e}")

        return None


# =============================================================================
# CHUNKER
# =============================================================================

class SimpleChunker:
    """Split text into overlapping chunks by headings or paragraphs.
    No ML dependencies – just word counts."""

    def __init__(self, cfg: Config):
        self.size = cfg.chunk_size
        self.overlap = cfg.chunk_overlap

    def chunk(self, text: str, meta: Dict) -> List[Dict]:
        # Split by headers first (h1-h3) to keep semantic boundaries
        sections = self._split_by_headers(text)
        chunks: List[Dict] = []
        buffer_words: List[str] = []
        buffer_headings: List[str] = []

        def flush():
            if not buffer_words:
                return
            content = " ".join(buffer_words)
            chunks.append({
                "id": f"{meta['domain']}_{meta['file_stem']}_chk_{len(chunks):04d}",
                "text": content,
                "headings": list(dict.fromkeys(buffer_headings)),  # dedupe, keep order
                "source_url": meta["url"],
                "source_title": meta.get("title", ""),
                "source_domain": meta["domain"],
                "word_count": len(buffer_words),
                "chunk_index": len(chunks),
            })

        for sec_text, sec_heading in sections:
            words = sec_text.split()
            if len(words) > self.size:
                # Oversized section – split with overlap
                i = 0
                while i < len(words):
                    end = min(i + self.size, len(words))
                    chunk_words = words[i:end]
                    chunks.append({
                        "id": f"{meta['domain']}_{meta['file_stem']}_chk_{len(chunks):04d}",
                        "text": " ".join(chunk_words),
                        "headings": list(dict.fromkeys(buffer_headings + ([sec_heading] if sec_heading else []))),
                        "source_url": meta["url"],
                        "source_title": meta.get("title", ""),
                        "source_domain": meta["domain"],
                        "word_count": len(chunk_words),
                        "chunk_index": len(chunks),
                    })
                    i += self.size - self.overlap
            else:
                if len(buffer_words) + len(words) > self.size and buffer_words:
                    flush()
                    # overlap: keep last N words from previous chunk
                    overlap_words = buffer_words[-self.overlap:] if self.overlap < len(buffer_words) else buffer_words[:]
                    buffer_words = overlap_words + words
                    buffer_headings = buffer_headings[-2:]  # keep recent headings
                else:
                    buffer_words.extend(words)
                if sec_heading and sec_heading not in buffer_headings:
                    buffer_headings.append(sec_heading)

        flush()
        # backfill total_chunks
        for c in chunks:
            c["total_chunks"] = len(chunks)
        return chunks

    def _split_by_headers(self, text: str) -> List[Tuple[str, str]]:
        pattern = re.compile(r"^(#{1,3}\s+.+)$", re.MULTILINE)
        matches = list(pattern.finditer(text))
        if not matches:
            return [(text, "")]
        sections = []
        for i, m in enumerate(matches):
            start = m.start()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            sections.append((text[start:end].strip(), m.group(1).strip()))
        return sections


# =============================================================================
# STORAGE
# =============================================================================

class Storage:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.root = Path(cfg.out_dir)
        self.root.mkdir(parents=True, exist_ok=True)
        # manifest for pipeline ingestion
        self.manifest = open(self.root / "manifest.jsonl", "a", encoding="utf-8")

    def save(self, url: str, html: str, extracted: Dict, depth: int,
             headings: List[str], outlinks: List[str]) -> Path:
        parsed = urlparse(url)
        domain = parsed.netloc.replace(":", "_")
        stem = safe_filename(url)
        page_dir = self.root / "pages" / domain / stem
        page_dir.mkdir(parents=True, exist_ok=True)

        # 1. Metadata
        meta = {
            "url": url,
            "domain": domain,
            "depth": depth,
            "crawled_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "title": extracted.get("title", ""),
            "author": extracted.get("author", ""),
            "date": extracted.get("date", ""),
            "extractor": extracted.get("extractor", ""),
            "word_count": extracted.get("word_count", 0),
            "headings": headings,
            "outlinks": outlinks,
        }
        meta_path = page_dir / "meta.json"
        meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

        # 2. Extracted content (markdown)
        md_path = page_dir / "content.md"
        md_path.write_text(extracted["text"], encoding="utf-8")

        # 3. Raw HTML
        html_path = page_dir / "raw.html"
        html_path.write_text(html, encoding="utf-8")

        # 4. Chunks
        chunker = SimpleChunker(self.cfg)
        chunks = chunker.chunk(extracted["text"], {"url": url, "domain": domain, "file_stem": stem, "title": extracted.get("title", "")})
        chunks_path = page_dir / "chunks.jsonl"
        with open(chunks_path, "w", encoding="utf-8") as f:
            for c in chunks:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")

        # Manifest entry
        manifest_entry = {
            "url": url,
            "domain": domain,
            "depth": depth,
            "page_dir": str(page_dir.relative_to(self.root)),
            "title": extracted.get("title", ""),
            "word_count": extracted.get("word_count", 0),
            "chunk_count": len(chunks),
        }
        self.manifest.write(json.dumps(manifest_entry, ensure_ascii=False) + "\n")
        self.manifest.flush()

        logger.info(f"Saved {domain}/{stem}  ({extracted.get('word_count', 0)} words, {len(chunks)} chunks)")
        return page_dir

    def close(self):
        self.manifest.close()


# =============================================================================
# CRAWLER
# =============================================================================

class Crawler:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.extractor = Extractor(cfg)
        self.storage = Storage(cfg)
        self.client = httpx.AsyncClient(
            timeout=httpx.Timeout(cfg.timeout),
            follow_redirects=True,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                ),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
            },
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
        )

        # State
        self.visited: Set[str] = set()
        self.queued: Set[str] = set()
        self.frontier: List[Tuple[int, float, str]] = []   # (depth, priority, url)
        self.domain_counts: Dict[str, int] = defaultdict(int)
        self.domain_last_req: Dict[str, float] = {}
        self.domain_locks: Dict[str, asyncio.Lock] = defaultdict(asyncio.Lock)
        self.shutdown = False

        signal.signal(signal.SIGINT, self._on_signal)
        signal.signal(signal.SIGTERM, self._on_signal)

    def _on_signal(self, signum, frame):
        logger.info("Shutdown signal received, finishing current batch...")
        self.shutdown = True

    def _normalize_and_add(self, url: str, depth: int, base_domain: str) -> bool:
        url = normalize_url(url)
        if url in self.visited or url in self.queued:
            return False
        if is_blocked(url, self.cfg):
            return False
        parsed = urlparse(url)
        if self.domain_counts[parsed.netloc] >= self.cfg.max_per_domain:
            return False
        if depth > self.cfg.max_depth:
            return False
        if len(self.visited) >= self.cfg.max_pages:
            return False
        if not should_follow(url, base_domain, self.cfg):
            return False
        self.queued.add(url)
        # Simple priority: same domain gets higher priority (lower number)
        priority = 0.0 if parsed.netloc == base_domain else 1.0
        self.frontier.append((depth, priority, url))
        self.frontier.sort(key=lambda x: (x[0], x[1]))
        return True

    async def _fetch(self, url: str) -> Optional[httpx.Response]:
        parsed = urlparse(url)
        domain = parsed.netloc
        async with self.domain_locks[domain]:
            last = self.domain_last_req.get(domain, 0)
            wait = self.cfg.delay - (time.time() - last)
            if wait > 0:
                await asyncio.sleep(wait)
            for attempt in range(self.cfg.retries + 1):
                try:
                    resp = await self.client.get(url)
                    self.domain_last_req[domain] = time.time()
                    return resp
                except Exception as e:
                    logger.warning(f"Fetch error {url} (attempt {attempt+1}): {e}")
                    if attempt < self.cfg.retries:
                        await asyncio.sleep(2 ** attempt)
        return None

    def _extract_links(self, html: str, base_url: str, base_domain: str) -> List[str]:
        try:
            soup = BeautifulSoup(html, "lxml")
            links = []
            for a in soup.find_all("a", href=True):
                abs_url = urljoin(base_url, a["href"])
                if abs_url.startswith(("http://", "https://")):
                    links.append(abs_url)
            return links
        except Exception as e:
            logger.debug(f"Link extraction failed: {e}")
            return []

    def _extract_headings(self, html: str) -> List[str]:
        try:
            soup = BeautifulSoup(html, "lxml")
            return [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]
        except Exception:
            return []

    async def _process(self, url: str, depth: int):
        if self.shutdown:
            return
        logger.info(f"[{depth}] {url[:90]}")

        resp = await self._fetch(url)
        if not resp or resp.status_code != 200:
            logger.debug(f"Skip {url} – status {resp.status_code if resp else 'none'}")
            return
        ctype = resp.headers.get("content-type", "").lower()
        if "text/html" not in ctype and "application/xhtml" not in ctype:
            logger.debug(f"Skip {url} – non-html {ctype}")
            return

        html = resp.text
        extracted = self.extractor.extract(html, url)
        if not extracted:
            logger.debug(f"Skip {url} – no usable content")
            return

        headings = self._extract_headings(html)
        outlinks = self._extract_links(html, url, urlparse(url).netloc)

        # Save everything
        self.storage.save(url, html, extracted, depth, headings, outlinks)

        # Queue children
        if depth < self.cfg.max_depth:
            base_domain = urlparse(url).netloc
            for link in outlinks:
                self._normalize_and_add(link, depth + 1, base_domain)

    async def run(self):
        # Seed
        for s in self.cfg.seeds:
            self._normalize_and_add(s, 0, urlparse(s).netloc)

        processed = 0
        while self.frontier and not self.shutdown and len(self.visited) < self.cfg.max_pages:
            batch = []
            for _ in range(self.cfg.concurrency):
                if not self.frontier:
                    break
                depth, _, url = self.frontier.pop(0)
                if url in self.visited:
                    continue
                self.queued.discard(url)
                self.visited.add(url)
                self.domain_counts[urlparse(url).netloc] += 1
                batch.append((url, depth))

            if not batch:
                break

            await asyncio.gather(*[self._process(url, depth) for url, depth in batch],
                                 return_exceptions=True)
            processed += len(batch)
            if processed % 10 == 0:
                logger.info(f"Progress: {processed} pages, {len(self.frontier)} queued")

        self.storage.close()
        await self.client.aclose()
        logger.info(f"Done. {processed} pages processed -> {self.cfg.out_dir}")


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Knowledge-Base Crawler for Azure Agent")
    parser.add_argument("--seeds", nargs="+", required=True, help="Seed URLs")
    parser.add_argument("--out", default="./Nexus", help="Output directory")
    parser.add_argument("--depth", type=int, default=2, help="Max crawl depth")
    parser.add_argument("--max-pages", type=int, default=500, help="Max total pages")
    parser.add_argument("--max-per-domain", type=int, default=100, help="Max pages per domain")
    parser.add_argument("--concurrency", type=int, default=6, help="Concurrent requests")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests (s)")
    parser.add_argument("--chunk-size", type=int, default=800, help="Chunk size in words")
    parser.add_argument("--chunk-overlap", type=int, default=100, help="Chunk overlap in words")
    args = parser.parse_args()

    cfg = Config(
        seeds=args.seeds,
        out_dir=args.out,
        max_depth=args.depth,
        max_pages=args.max_pages,
        max_per_domain=args.max_per_domain,
        concurrency=args.concurrency,
        delay=args.delay,
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
    )
    crawler = Crawler(cfg)
    asyncio.run(crawler.run())


if __name__ == "__main__":
    main()