"""
Topic-Aware Recursive Web Crawler for EU Digital Identity Standards
====================================================================
Intelligently crawls websites starting from seed URLs, following only
links relevant to European digital identity, eIDAS 2.0, OpenID4VCI,
and related standards.

Features:
- Topic-aware link filtering (no LLM required, zero API cost)
- Content extraction via trafilatura (clean text, no nav/footer)
- Async concurrent crawling with per-domain rate limiting
- Resumable with checkpointing
- Organized directory output ready for the pipeline

Usage:
    pip install httpx beautifulsoup4 trafilatura lxml
    python topic_crawler.py
"""

import asyncio
import json
import hashlib
import re
import time
import signal
import sys
import subprocess
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag
from dataclasses import dataclass, field, asdict
from typing import Set, List, Dict, Any, Optional, Tuple
from collections import defaultdict
import logging

try:
    import httpx
    from bs4 import BeautifulSoup
    import trafilatura
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install httpx beautifulsoup4 trafilatura lxml")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s"
)
logger = logging.getLogger("Crawler")


# =============================================================================
# CONFIGURATION
# =============================================================================

@dataclass
class CrawlerConfig:
    """Configuration for the topic-aware crawler."""

    # Seed URLs to start crawling from
    seed_urls: List[str] = field(default_factory=list)

    # Output directory
    output_dir: str = "./data_lake/crawled"

    # Crawling limits
    max_depth: int = 2
    max_pages_per_domain: int = 150
    max_total_pages: int = 3000
    max_retries: int = 3
    request_timeout: int = 30
    concurrent_requests: int = 8
    delay_per_domain: float = 1.0  # seconds between requests to same domain

    # Link relevance thresholds
    min_link_relevance: float = 0.30
    min_content_length: int = 400

    # Content extraction
    extract_format: str = "markdown"
    include_comments: bool = False
    include_tables: bool = True

    # Resumability
    checkpoint_file: str = "crawler_state.json"

    # Domain restrictions
    allowed_domains: Optional[Set[str]] = None
    blocked_domains: Set[str] = field(default_factory=lambda: {
        "facebook.com", "twitter.com", "x.com", "linkedin.com",
        "youtube.com", "instagram.com", "tiktok.com",
        "google.com", "bing.com", "yahoo.com", "reddit.com",
        "pinterest.com", "tumblr.com", "medium.com"
    })


# =============================================================================
# RELEVANCE ENGINE
# =============================================================================

class RelevanceEngine:
    """
    Scores URL/link relevance without API calls.
    Uses keyword matching, URL patterns, and anchor text analysis.
    """

    TOPIC_KEYWORDS = [
        # Core standards
        "openid", "verifiable", "credential", "presentation", "issuance",
        "vci", "vp", "haip", "par", "oidc", "oauth", "oid4vci", "oid4vp",

        # EU specific
        "eidas", "eidas2", "digital identity", "identity wallet",
        "eu wallet", "eu digital", "trust framework", "qualified",
        "electronic identification", "electronic signature", "eid",
        "person identification", "pid", "wallet provider",

        # Technical mechanisms
        "sd-jwt", "selective disclosure", "jwt", "jws", "jwe", "jwk",
        "did", "decentralized identifier", "blockchain", "ledger",
        "mdl", "mobile driving licence", "iso 18013", "iso/iec 18013",
        "mdoc", "mso", "cbor", "cose", "cwt",

        # Protocol flows
        "authorization", "authentication", "token", "issuer", "holder",
        "verifier", "relying party", "wallet", "pid provider",
        "credential offer", "authorization request", "token request",

        # Regulatory
        "psd2", "payment services", "strong customer authentication",
        "sca", "gdpr", "data protection", "privacy", "regulation",
        "directive", "compliance", "legal", "framework",

        # ARF / Architecture
        "arf", "architecture reference framework", "reference implementation",
        "interoperability", "conformance", "certification", "testing",

        # Cryptography
        "cryptographic", "signature", "verification", "key", "certificate",
        "pki", "post-quantum", "pqc", "encryption", "hash", "ecdsa", "eddsa",

        # Implementation
        "implementation", "endpoint", "api", "rest", "http",
        "json", "schema", "protocol", "flow", "sequence", "diagram"
    ]

    BOOST_PATTERNS = [
        r'/specs?/', r'/standard', r'/rfc', r'/draft', r'/doc/',
        r'/documentation', r'/guide', r'/tutorial', r'/reference',
        r'/openid', r'/eidas', r'/credential', r'/identity',
        r'/wallet', r'/sd-jwt', r'/architecture', r'/protocol'
    ]

    PENALTY_PATTERNS = [
        r'/login', r'/signin', r'/register', r'/auth',
        r'/search', r'/tag/', r'/category/', r'/author/',
        r'/feed', r'/rss', r'/atom', r'/api/', r'/wp-json/',
        r'/comment', r'/trackback', r'/print',
        r'/contact', r'/about', r'/team', r'/career',
        r'/news', r'/press', r'/event', r'/webinar',
        r'\?.*share=', r'\?.*print=', r'\?.*format=',
        r'/cookie', r'/privacy-policy', r'/terms', r'/legal'
    ]

    SKIP_EXTENSIONS = {
        '.pdf', '.zip', '.tar', '.gz', '.rar', '.7z',
        '.exe', '.bin', '.dmg', '.pkg', '.deb', '.rpm',
        '.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.webp',
        '.mp4', '.mp3', '.avi', '.mov', '.wmv',
        '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
        '.css', '.js', '.xml', '.woff', '.woff2', '.ttf', '.eot'
    }

    def __init__(self):
        self.boost_re = [re.compile(p, re.I) for p in self.BOOST_PATTERNS]
        self.penalty_re = [re.compile(p, re.I) for p in self.PENALTY_PATTERNS]

    def score_link(self, url: str, anchor_text: str = "", 
                   parent_context: str = "") -> Tuple[float, str]:
        parsed = urlparse(url)
        path = parsed.path.lower()
        query = parsed.query.lower()
        anchor = anchor_text.lower().strip()

        ext = Path(path).suffix.lower()
        if ext in self.SKIP_EXTENSIONS:
            return 0.0, f"skip_extension:{ext}"

        if parsed.netloc in CrawlerConfig().blocked_domains:
            return 0.0, "blocked_domain"

        score = 0.0
        reasons = []

        # URL path keywords
        path_matches = sum(1 for kw in self.TOPIC_KEYWORDS if kw in path)
        if path_matches > 0:
            path_score = min(path_matches * 0.08, 0.35)
            score += path_score
            reasons.append(f"path:{path_matches}")

        # Boost patterns
        for pattern in self.boost_re:
            if pattern.search(path):
                score += 0.12
                reasons.append("boost")
                break

        # Penalty patterns
        for pattern in self.penalty_re:
            if pattern.search(path) or pattern.search(query):
                score -= 0.35
                reasons.append("penalty")
                break

        # Anchor text
        if anchor:
            anchor_matches = sum(1 for kw in self.TOPIC_KEYWORDS if kw in anchor)
            if anchor_matches > 0:
                anchor_score = min(anchor_matches * 0.08, 0.25)
                score += anchor_score
                reasons.append(f"anchor:{anchor_matches}")

        # Parent context
        if parent_context:
            ctx = parent_context.lower()
            ctx_matches = sum(1 for kw in self.TOPIC_KEYWORDS if kw in ctx)
            if ctx_matches >= 3:
                score += min(ctx_matches * 0.03, 0.15)
                reasons.append(f"ctx:{ctx_matches}")

        # Known good domains
        good_domains = [
            'openid.net', 'ietf.org', 'eur-lex.europa.eu', 
            'iso.org', 'w3.org', 'digst.dk', 'github.com',
            'oauth.net', 'identity.foundation', 'cre8.github.io'
        ]
        if any(gd in parsed.netloc for gd in good_domains):
            score += 0.08
            reasons.append("known_domain")

        final_score = max(0.0, min(1.0, score))
        reason_str = ";".join(reasons) if reasons else "none"
        return final_score, reason_str

    def is_content_url(self, url: str) -> bool:
        parsed = urlparse(url)
        ext = Path(parsed.path).suffix.lower()
        if ext in self.SKIP_EXTENSIONS:
            return False
        if parsed.netloc in CrawlerConfig().blocked_domains:
            return False
        return True


# =============================================================================
# CONTENT EXTRACTOR
# =============================================================================

class ContentExtractor:
    def __init__(self, config: CrawlerConfig):
        self.config = config

    def extract(self, html: str, url: str) -> Optional[Dict[str, Any]]:
        try:
            result = trafilatura.extract(
                html,
                url=url,
                output_format=self.config.extract_format,
                include_comments=self.config.include_comments,
                include_tables=self.config.include_tables,
                with_metadata=True,
                deduplicate=True,
                target_language="en"
            )

            if result and len(result) > self.config.min_content_length:
                metadata = trafilatura.extract_metadata(html, url=url)
                return {
                    "title": getattr(metadata, 'title', "") or "",
                    "author": getattr(metadata, 'author', "") or "",
                    "date": getattr(metadata, 'date', "") or "",
                    "url": url,
                    "content": result,
                    "length": len(result),
                    "extractor": "trafilatura"
                }
        except Exception as e:
            logger.debug(f"Trafilatura failed for {url}: {e}")

        return self._fallback_extract(html, url)

    def _fallback_extract(self, html: str, url: str) -> Optional[Dict[str, Any]]:
        try:
            soup = BeautifulSoup(html, 'lxml')
            for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                element.decompose()

            main = soup.find('main') or soup.find('article') or soup.find('div', class_=re.compile('content|main|article'))
            text = main.get_text(separator='\n', strip=True) if main else soup.get_text(separator='\n', strip=True)
            text = re.sub(r'\n{3,}', '\n\n', text)

            if len(text) > self.config.min_content_length:
                return {
                    "title": soup.title.string if soup.title else "",
                    "author": "",
                    "date": "",
                    "url": url,
                    "content": text,
                    "length": len(text),
                    "extractor": "beautifulsoup"
                }
        except Exception as e:
            logger.debug(f"Fallback extraction failed for {url}: {e}")
        return None


# =============================================================================
# URL FRONTIER
# =============================================================================

class URLFrontier:
    def __init__(self, config: CrawlerConfig):
        self.config = config
        self.visited: Set[str] = set()
        self.queued: Set[str] = set()
        self.frontier: List[Tuple[float, int, str]] = []
        self.domain_counts: Dict[str, int] = defaultdict(int)
        self.relevance_engine = RelevanceEngine()
        self._load_checkpoint()

    def _normalize_url(self, url: str) -> str:
        url, _ = urldefrag(url)
        url = url.rstrip('/')
        if url.startswith('http://'):
            url = 'https://' + url[7:]
        return url

    def _load_checkpoint(self):
        checkpoint_path = Path(self.config.output_dir) / self.config.checkpoint_file
        if checkpoint_path.exists():
            try:
                with open(checkpoint_path, 'r') as f:
                    state = json.load(f)
                self.visited = set(state.get('visited', []))
                self.domain_counts = defaultdict(int, state.get('domain_counts', {}))
                for item in state.get('frontier', []):
                    self.add_url(item['url'], item['depth'], item['score'])
                logger.info(f"Resumed: {len(self.visited)} visited, {len(self.frontier)} queued")
            except Exception as e:
                logger.warning(f"Could not load checkpoint: {e}")

    def save_checkpoint(self):
        checkpoint_path = Path(self.config.output_dir) / self.config.checkpoint_file
        checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
        state = {
            'visited': list(self.visited),
            'domain_counts': dict(self.domain_counts),
            'frontier': [
                {'url': url, 'depth': depth, 'score': score}
                for score, depth, url in self.frontier
            ]
        }
        with open(checkpoint_path, 'w') as f:
            json.dump(state, f, indent=2)

    def add_url(self, url: str, depth: int = 0, score: float = 1.0) -> bool:
        normalized = self._normalize_url(url)
        if normalized in self.visited or normalized in self.queued:
            return False

        parsed = urlparse(normalized)
        if self.config.allowed_domains and parsed.netloc not in self.config.allowed_domains:
            return False
        if parsed.netloc in self.config.blocked_domains:
            return False
        if self.domain_counts[parsed.netloc] >= self.config.max_pages_per_domain:
            return False
        if depth > self.config.max_depth:
            return False
        if len(self.visited) + len(self.frontier) >= self.config.max_total_pages:
            return False

        self.queued.add(normalized)
        self.frontier.append((-score, depth, normalized))
        self.frontier.sort()
        return True

    def get_next(self) -> Optional[Tuple[str, int]]:
        while self.frontier:
            score, depth, url = self.frontier.pop(0)
            normalized = self._normalize_url(url)
            if normalized in self.visited:
                continue
            self.queued.discard(normalized)
            self.visited.add(normalized)
            parsed = urlparse(normalized)
            self.domain_counts[parsed.netloc] += 1
            return normalized, depth
        return None

    def is_done(self) -> bool:
        return len(self.frontier) == 0 or len(self.visited) >= self.config.max_total_pages


# =============================================================================
# STORAGE
# =============================================================================

class StorageManager:
    def __init__(self, config: CrawlerConfig):
        self.config = config
        self.output_dir = Path(config.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.metadata_path = self.output_dir / "metadata.jsonl"
        self.metadata_file = open(self.metadata_path, 'a', encoding='utf-8')

    def save_content(self, url: str, extracted: Dict[str, Any], 
                     depth: int, relevance_score: float) -> Path:
        parsed = urlparse(url)
        domain = parsed.netloc.replace(':', '_')
        path_part = parsed.path.strip('/')
        if not path_part:
            path_part = "index"

        safe_name = re.sub(r'[^\w\-_.]', '_', path_part)[:100]
        if not safe_name.endswith(('.md', '.txt')):
            safe_name += '.md'

        domain_dir = self.output_dir / "extracted" / domain
        domain_dir.mkdir(parents=True, exist_ok=True)
        file_path = domain_dir / safe_name

        if file_path.exists():
            url_hash = hashlib.md5(url.encode()).hexdigest()[:6]
            file_path = domain_dir / f"{file_path.stem}_{url_hash}{file_path.suffix}"

        frontmatter = {
            "title": extracted.get("title", ""),
            "url": url,
            "domain": domain,
            "depth": depth,
            "relevance_score": round(relevance_score, 3),
            "extractor": extracted.get("extractor", "unknown"),
            "author": extracted.get("author", ""),
            "date": extracted.get("date", ""),
            "length": extracted.get("length", 0),
            "crawled_at": time.strftime("%Y-%m-%dT%H:%M:%S")
        }

        content_lines = [
            "---",
            json.dumps(frontmatter, indent=2, ensure_ascii=False),
            "---",
            "",
            extracted.get("content", "")
        ]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content_lines))

        meta_record = {
            "url": url,
            "file_path": str(file_path.relative_to(self.output_dir)),
            "depth": depth,
            "relevance_score": relevance_score,
            "length": extracted.get("length", 0),
            "title": extracted.get("title", "")
        }
        self.metadata_file.write(json.dumps(meta_record, ensure_ascii=False) + "\n")
        self.metadata_file.flush()
        return file_path

    def close(self):
        self.metadata_file.close()


# =============================================================================
# CRAWLER
# =============================================================================

class TopicAwareCrawler:
    def __init__(self, config: CrawlerConfig):
        self.config = config
        self.frontier = URLFrontier(config)
        self.extractor = ContentExtractor(config)
        self.storage = StorageManager(config)
        self.relevance = RelevanceEngine()

        self.client = httpx.AsyncClient(
            timeout=httpx.Timeout(config.request_timeout),
            follow_redirects=True,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "DNT": "1",
                "Connection": "keep-alive",
            },
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=20)
        )

        self.domain_last_request: Dict[str, float] = {}
        self.domain_locks: Dict[str, asyncio.Lock] = defaultdict(asyncio.Lock)
        self.shutdown = False
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

    def _signal_handler(self, signum, frame):
        logger.info("Shutdown signal received, finishing current batch...")
        self.shutdown = True

    async def _rate_limited_get(self, url: str) -> Optional[httpx.Response]:
        parsed = urlparse(url)
        domain = parsed.netloc

        async with self.domain_locks[domain]:
            last = self.domain_last_request.get(domain, 0)
            elapsed = time.time() - last
            if elapsed < self.config.delay_per_domain:
                await asyncio.sleep(self.config.delay_per_domain - elapsed)

            for attempt in range(self.config.max_retries):
                try:
                    response = await self.client.get(url)
                    self.domain_last_request[domain] = time.time()
                    return response
                except httpx.TimeoutException:
                    logger.warning(f"Timeout for {url} (attempt {attempt + 1})")
                    if attempt < self.config.max_retries - 1:
                        await asyncio.sleep(2 ** attempt)
                except Exception as e:
                    logger.warning(f"Request failed for {url}: {e}")
                    if attempt < self.config.max_retries - 1:
                        await asyncio.sleep(2 ** attempt)

        return None

    def _extract_links(self, html: str, base_url: str, parent_context: str = "") -> List[Tuple[str, str, float, str]]:
        links = []
        try:
            soup = BeautifulSoup(html, 'lxml')
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                anchor_text = a_tag.get_text(strip=True)
                absolute_url = urljoin(base_url, href)

                if not absolute_url.startswith(('http://', 'https://')):
                    continue
                if not self.relevance.is_content_url(absolute_url):
                    continue

                score, reason = self.relevance.score_link(absolute_url, anchor_text, parent_context)
                if score >= self.config.min_link_relevance:
                    links.append((absolute_url, anchor_text, score, reason))
        except Exception as e:
            logger.debug(f"Link extraction failed for {base_url}: {e}")
        return links

    async def _process_url(self, url: str, depth: int):
        if self.shutdown:
            return

        logger.info(f"[{depth}] {url[:80]}...")

        response = await self._rate_limited_get(url)
        if not response or response.status_code != 200:
            logger.debug(f"Failed: {url} ({response.status_code if response else 'no response'})")
            return

        content_type = response.headers.get('content-type', '').lower()
        if 'text/html' not in content_type and 'application/xhtml' not in content_type:
            logger.debug(f"Non-HTML: {content_type}")
            return

        html = response.text
        extracted = self.extractor.extract(html, url)
        if not extracted:
            logger.debug(f"No content: {url}")
            return

        content_preview = extracted['content'][:3000].lower()
        page_score, _ = self.relevance.score_link(url, "", content_preview)

        file_path = self.storage.save_content(url, extracted, depth, page_score)
        logger.info(f"Saved: {file_path.name} ({extracted['length']} chars)")

        if depth < self.config.max_depth:
            links = self._extract_links(html, url, content_preview)
            links.sort(key=lambda x: x[2], reverse=True)

            for link_url, anchor, score, reason in links:
                added = self.frontier.add_url(link_url, depth + 1, score)
                if added:
                    logger.debug(f"  + [{depth+1}] {link_url[:60]}... ({score:.2f})")

    async def run(self):
        logger.info("=" * 60)
        logger.info("Topic-Aware Crawler Starting")
        logger.info("=" * 60)

        for seed in self.config.seed_urls:
            self.frontier.add_url(seed, depth=0, score=1.0)

        processed = 0

        while not self.frontier.is_done() and not self.shutdown:
            batch = []
            for _ in range(self.config.concurrent_requests):
                next_item = self.frontier.get_next()
                if not next_item:
                    break
                batch.append(next_item)

            if not batch:
                break

            tasks = [self._process_url(url, depth) for url, depth in batch]
            await asyncio.gather(*tasks, return_exceptions=True)

            processed += len(batch)

            if processed % 10 == 0:
                self.frontier.save_checkpoint()
                logger.info(f"Progress: {processed} done, {len(self.frontier.frontier)} queued")

        self.frontier.save_checkpoint()
        self.storage.close()
        await self.client.aclose()

        logger.info("=" * 60)
        logger.info(f"Done! {processed} pages processed.")
        logger.info(f"Output: {self.config.output_dir}")
        logger.info("=" * 60)


# =============================================================================
# REPO DOWNLOADER
# =============================================================================

class RepoDownloader:
    """Clones GitHub repos and extracts text files."""

    def __init__(self, output_dir: str = "./data_lake/repos"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def download(self, repo_urls: List[str]):
        for url in repo_urls:
            repo_name = url.rstrip('/').split('/')[-1].replace('.git', '')
            target = self.output_dir / repo_name

            if target.exists():
                logger.info(f"Repo exists: {repo_name}")
                continue

            logger.info(f"Cloning {repo_name}...")
            try:
                subprocess.run(
                    ["git", "clone", "--depth", "1", url, str(target)],
                    check=True, capture_output=True, text=True, timeout=120
                )
                logger.info(f"Cloned: {repo_name}")
            except subprocess.CalledProcessError as e:
                logger.error(f"Clone failed {repo_name}: {e.stderr}")
            except subprocess.TimeoutExpired:
                logger.error(f"Clone timeout: {repo_name}")

    def extract_text_files(self, repo_dir: Path) -> List[Path]:
        text_exts = {'.md', '.txt', '.rst', '.py', '.js', '.ts', 
                     '.java', '.go', '.rs', '.c', '.cpp', '.h',
                     '.yaml', '.yml', '.json', '.toml', '.sh', '.dockerfile'}
        files = []
        for ext in text_exts:
            files.extend(repo_dir.rglob(f"*{ext}"))
        return files


# =============================================================================
# MAIN
# =============================================================================

def main():
    seeds = [
        # OpenID specs
        "https://openid.net/developers/specs/"


        # # IETF
        # "https://datatracker.ietf.org/doc/html/rfc9126",
        # "https://datatracker.ietf.org/doc/rfc9901/",
        # "https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/",

        # # EU / eIDAS
        # "https://digst.dk/it-loesninger/eid-og-single-digital-gateway/eidas2-og-den-digitale-identitetstegnebog/",
        # "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2014.257.01.0073.01.ENG",
        # "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32015L2366",

        # # ISO
        # "https://www.iso.org/standard/69084.html",

        # # Reference
        # "https://cre8.github.io/eudi-nexus/",

        # # GitHub org pages (crawler will follow relevant repos)
        # "https://github.com/eu-digital-identity-wallet",
        # "https://github.com/walt-id/waltid-identity",
    ]

    config = CrawlerConfig(
        seed_urls=seeds,
        output_dir="./data_lake/crawled",
        max_depth=2,
        max_pages_per_domain=100,
        max_total_pages=2000,
        concurrent_requests=6,
        delay_per_domain=1.5,
        min_link_relevance=0.30,
        min_content_length=300,
    )

    crawler = TopicAwareCrawler(config)
    asyncio.run(crawler.run())

    # Clone key repos
    repos = [
        "https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework.git",
        "https://github.com/walt-id/waltid-identity.git",
    ]
    downloader = RepoDownloader()
    downloader.download(repos)


if __name__ == "__main__":
    main()
