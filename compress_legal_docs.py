#!/usr/bin/env python3
"""
EUDI Nexus MCP - Legal Document Compressor (Async + Robust DOCX)
=================================================================

Reads raw regulatory/specification documents from the downloads folder
and uses DeepSeek R1 to compress them into structured legal markdown.

Now with:
  - Robust DOCX loading (python-docx + zipfile/XML fallback)
  - Async/concurrent API processing for speed
  - Configurable concurrency with semaphore-based rate limiting

Preserves:
  - Normative language (shall, must, should, may, etc.)
  - Cross-references and citations
  - Hierarchical structure (Articles, Clauses, Sections)
  - Definitions and terms of art
  - Requirements and obligations

Usage:
    python compress_legal_docs.py [--downloads-dir ./downloads] [--output-dir ./compressed] [--api-key KEY] [--concurrency 5]

Prerequisites:
    pip install openai tqdm

Environment:
    LLM_API_KEY - Your LLM API key (or use --api-key)
    OPENROUTER_API_KEY - Alternative: OpenRouter API key
"""

import argparse
import asyncio
import json
import os
import re
import sys
import time
import hashlib
import zipfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from dotenv import load_dotenv

load_dotenv()

import numpy as np

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

@dataclass
class CompressorConfig:
    """Compression configuration."""
    downloads_dir: str = "./downloads"
    output_dir: str = "./compressed"
    specs_dir: str = "./downloads/specs"
    references_json: str = "./downloads/references.json"

    # API Configuration
    api_provider: str = "deepseek"  # "deepseek" or "openrouter"
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    model: str = "deepseek-reasoner"  # DeepSeek R1

    # Processing
    max_tokens_per_chunk: int = 60000
    max_output_tokens: int = 16000
    temperature: float = 0.2
    top_p: float = 0.95

    # Rate limiting & concurrency
    concurrency: int = 5              # Max concurrent API calls
    requests_per_minute: int = 30     # Global rate limit
    retry_attempts: int = 3
    retry_delay: float = 5.0

    # Output
    compression_suffix: str = "_compressed.md"
    preserve_raw_link: bool = True

    def to_dict(self):
        return asdict(self)


# ---------------------------------------------------------------------------
# Document Loader (with robust DOCX fallback)
# ---------------------------------------------------------------------------

class DocumentLoader:
    """Load and extract text from PDF, HTML, TXT, and DOCX files."""

    def __init__(self):
        self._pdf_available = False
        self._bs4_available = False
        self._lxml_available = False
        self._docx_available = False
        self._check_deps()

    def _check_deps(self):
        try:
            import pdfplumber
            self._pdf_available = True
        except ImportError:
            pass
        try:
            from bs4 import BeautifulSoup
            self._bs4_available = True
        except ImportError:
            pass
        try:
            import lxml
            self._lxml_available = True
        except ImportError:
            pass
        try:
            import docx
            self._docx_available = True
        except ImportError:
            pass

    def load(self, file_path: str) -> Optional[str]:
        path = Path(file_path)
        ext = path.suffix.lower()

        if ext == ".pdf":
            return self._load_pdf(file_path)
        elif ext in (".html", ".htm"):
            return self._load_html(file_path)
        elif ext == ".txt":
            return self._load_txt(file_path)
        elif ext in (".docx", ".doc"):
            return self._load_docx(file_path)
        elif ext == ".md":
            return self._load_txt(file_path)
        else:
            return None

    def _load_pdf(self, path: str) -> Optional[str]:
        if not self._pdf_available:
            print(f"  [WARN] pdfplumber not installed, skipping PDF: {path}")
            return None
        import pdfplumber
        try:
            text_parts = []
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    txt = page.extract_text()
                    if txt:
                        text_parts.append(txt)
            return "\n".join(text_parts) if text_parts else None
        except Exception as e:
            print(f"  [WARN] Failed to parse PDF {path}: {e}")
            return None

    def _load_html(self, path: str) -> Optional[str]:
        if not self._bs4_available:
            print(f"  [WARN] beautifulsoup4 not installed, skipping HTML: {path}")
            return None
        from bs4 import BeautifulSoup
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                html = f.read()
            soup = BeautifulSoup(html, "lxml" if self._lxml_available else "html.parser")
            for tag in soup(["script", "style", "nav", "header", "footer"]):
                tag.decompose()
            text = soup.get_text(separator="\n")
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            return "\n".join(lines)
        except Exception as e:
            print(f"  [WARN] Failed to parse HTML {path}: {e}")
            return None

    def _load_txt(self, path: str) -> Optional[str]:
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        except Exception as e:
            print(f"  [WARN] Failed to read TXT {path}: {e}")
            return None

    def _load_docx(self, path: str) -> Optional[str]:
        """Load DOCX with python-docx, fallback to zipfile/XML extraction."""
        # Attempt 1: python-docx (best formatting)
        if self._docx_available:
            try:
                import docx
                document = docx.Document(path)
                paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
                if paragraphs:
                    return "\n".join(paragraphs)
            except Exception as e:
                print(f"  [WARN] python-docx failed for {path}: {e}")
                print(f"  [INFO] Attempting zipfile/XML fallback...")
        else:
            print(f"  [WARN] python-docx not installed, using zipfile fallback for: {path}")

        # Attempt 2: Direct zipfile + XML text extraction
        # Handles corrupted/malformed docx, or .doc files misnamed as .docx
        try:
            return self._load_docx_zip_fallback(path)
        except Exception as e:
            print(f"  [WARN] Zipfile fallback also failed for {path}: {e}")

        # Attempt 3: Try reading as plain text (last resort for misnamed files)
        try:
            raw = self._load_txt(path)
            if raw and len(raw) > 100:
                # If it looks like readable text, return it
                # This catches .doc files that are actually text, or RTF-like content
                print(f"  [INFO] Falling back to raw text read for {path}")
                return raw
        except Exception:
            pass

        return None

    def _load_docx_zip_fallback(self, path: str) -> Optional[str]:
        """Extract text from docx by reading word/document.xml directly."""
        with zipfile.ZipFile(path, 'r') as zf:
            # List of XML files that may contain text
            xml_files = [name for name in zf.namelist() if name.endswith('.xml')]

            # Priority: main document, then headers/footnotes/endnotes
            priority_files = []
            for name in xml_files:
                if name == 'word/document.xml':
                    priority_files.insert(0, name)
                elif 'word/' in name and 'document' in name:
                    priority_files.append(name)

            all_texts = []
            for xml_name in priority_files[:3]:  # Limit to avoid noise
                try:
                    xml_content = zf.read(xml_name).decode('utf-8', errors='ignore')
                    # Extract text between w:t tags
                    texts = re.findall(r'<w:t[^>]*>([^<]+)</w:t>', xml_content)
                    if texts:
                        all_texts.extend(texts)
                except Exception:
                    continue

            if not all_texts:
                return None

            # Reconstruct paragraphs by looking at paragraph boundaries in XML
            xml_content = zf.read('word/document.xml').decode('utf-8', errors='ignore')
            # Split by paragraph tags and extract text from each
            paragraphs = re.split(r'<w:p[\s>]', xml_content)
            result_paras = []
            for para in paragraphs:
                texts = re.findall(r'<w:t[^>]*>([^<]+)</w:t>', para)
                if texts:
                    para_text = ''.join(texts).strip()
                    if para_text:
                        result_paras.append(para_text)

            return "\n".join(result_paras) if result_paras else "\n".join(all_texts)


# ---------------------------------------------------------------------------
# Text Chunking for API Limits
# ---------------------------------------------------------------------------

class TextChunker:
    """Split long documents into chunks that fit within API token limits."""

    def __init__(self, max_chars_per_chunk: int = 240000):
        self.max_chars_per_chunk = max_chars_per_chunk

    def chunk(self, text: str) -> List[str]:
        """Split text into roughly equal chunks at paragraph boundaries."""
        if len(text) <= self.max_chars_per_chunk:
            return [text]

        paragraphs = re.split(r"\n{2,}", text)
        paragraphs = [p.strip() for p in paragraphs if p.strip()]

        chunks = []
        current_chunk = []
        current_len = 0

        for para in paragraphs:
            para_len = len(para)

            if current_len + para_len > self.max_chars_per_chunk and current_chunk:
                chunks.append("\n\n".join(current_chunk))
                # Overlap: keep last ~10% for context continuity
                overlap_start = max(0, len(current_chunk) - max(1, len(current_chunk) // 10))
                current_chunk = current_chunk[overlap_start:] + [para]
                current_len = sum(len(p) for p in current_chunk)
            else:
                current_chunk.append(para)
                current_len += para_len

        if current_chunk:
            chunks.append("\n\n".join(current_chunk))

        return chunks


# ---------------------------------------------------------------------------
# Async DeepSeek R1 Compression Engine
# ---------------------------------------------------------------------------

class AsyncLegalCompressor:
    """Compress legal/regulatory documents using DeepSeek R1 (async)."""

    SYSTEM_PROMPT = """You are a legal document compression specialist. Your task is to convert raw regulatory, normative, or technical specification text into dense, structured markdown.

CRITICAL RULES:
1. PRESERVE ALL NORMATIVE LANGUAGE exactly: shall, must, should, may, required, mandatory, optional, prohibited, etc.
2. PRESERVE ALL CROSS-REFERENCES: "Article X", "Section Y", "Clause Z", "as defined in...", "see RFC...", "refer to EN..."
3. PRESERVE ALL DEFINITIONS: Terms of art must keep their exact legal meaning.
4. PRESERVE STRUCTURAL HIERARCHY: Use markdown headers (#, ##, ###) to reflect document structure.
5. PRESERVE ENUMERATIONS: Numbered lists, bullet points, and lettered sub-points must retain their sequence.
6. REMOVE REDUNDANCY: Eliminate repetitive boilerplate, excessive introductory text, and duplicated informative annexes.
7. SUMMARIZE INFORMATIVE CONTENT: Less-Important or Supplementary Informative annexes, examples, and non-normative explanations may be condensed to 1-2 sentences. Important informative content that provides essential context should be preserved in detail, leaving the reader with the same understanding as the original.
8. KEEP METADATA: Document ID, title, version, date, and source authority must appear in the header.

OUTPUT FORMAT:
```markdown
# [Document ID]: [Title]
**Source**: [Authority] | **Version**: [Version] | **Date**: [Date] | **Type**: [Normative/Informative]
**Original**: [path or URL to raw document]

## Scope (Summary)
[1-2 sentence summary of scope]

## Normative References
- [Ref 1]
- [Ref 2]

## Definitions and Abbreviations
- **Term**: [definition]

## [Section/Article Title]
### [Subsection]
- **[Requirement ID/Clause]**: [Exact requirement text preserving shall/must/should/may]
- **[Cross-reference]**: [Preserved reference text]

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | [Exact text] | shall | Section X.Y |

## Informative Annexes (Condensed)
- **[Annex Title]**: [1-2 sentence summary of purpose and key points]
```

Be precise. Do not invent requirements. Do not soften normative language."""

    CHUNK_PROMPT = """You are processing chunk {chunk_num} of {total_chunks} from the same document.
{context_note}

Compress the following text into structured legal markdown following the system rules. 
If this is not the first chunk, continue the structure from where the previous chunk left off.
Do not add a document header if this is not chunk 1.

TEXT TO COMPRESS:
{text}

OUTPUT ONLY VALID MARKDOWN."""

    def __init__(self, config: CompressorConfig):
        self.config = config
        self.client = self._init_client()
        self.semaphore = asyncio.Semaphore(config.concurrency)
        self.rate_limit_lock = asyncio.Lock()
        self.last_request_time = 0
        self.min_interval = 60.0 / max(config.requests_per_minute, 1)

    def _init_client(self):
        try:
            from openai import AsyncOpenAI
        except ImportError:
            print("ERROR: openai package not installed. Run: pip install openai")
            sys.exit(1)

        api_key = self.config.api_key or os.environ.get("LLM_API_KEY") or os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            print("ERROR: No API key provided. Set LLM_API_KEY or OPENROUTER_API_KEY, or use --api-key")
            sys.exit(1)

        if self.config.api_provider == "openrouter":
            base_url = self.config.base_url or "https://openrouter.ai/api/v1"
        else:
            base_url = self.config.base_url or "https://api.deepseek.com"

        return AsyncOpenAI(api_key=api_key, base_url=base_url)

    async def _rate_limit(self):
        """Enforce requests per minute limit globally."""
        async with self.rate_limit_lock:
            elapsed = time.time() - self.last_request_time
            if elapsed < self.min_interval:
                await asyncio.sleep(self.min_interval - elapsed)
            self.last_request_time = time.time()

    async def compress_chunk(self, text: str, chunk_num: int, total_chunks: int, 
                             doc_metadata: Dict) -> str:
        """Compress a single chunk using DeepSeek R1 (async)."""

        context_note = ""
        if total_chunks > 1:
            if chunk_num == 1:
                context_note = "This is the FIRST chunk. Include the document header metadata."
            elif chunk_num == total_chunks:
                context_note = "This is the FINAL chunk. Ensure all remaining requirements and references are captured."
            else:
                context_note = "This is a MIDDLE chunk. Continue the markdown structure seamlessly."

        prompt = self.CHUNK_PROMPT.format(
            chunk_num=chunk_num,
            total_chunks=total_chunks,
            context_note=context_note,
            text=text[:self.config.max_tokens_per_chunk * 4]
        )

        async with self.semaphore:
            for attempt in range(self.config.retry_attempts):
                try:
                    await self._rate_limit()

                    response = await self.client.chat.completions.create(
                        model=self.config.model,
                        messages=[
                            {"role": "system", "content": self.SYSTEM_PROMPT},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=self.config.temperature,
                        top_p=self.config.top_p,
                        max_tokens=self.config.max_output_tokens,
                    )

                    content = response.choices[0].message.content
                    # Strip markdown code fences if present
                    content = re.sub(r"^```markdown\s*", "", content)
                    content = re.sub(r"```\s*$", "", content)
                    return content.strip()

                except Exception as e:
                    print(f"    [ERROR] API call failed (attempt {attempt + 1}/{self.config.retry_attempts}): {e}")
                    if attempt < self.config.retry_attempts - 1:
                        await asyncio.sleep(self.config.retry_delay * (attempt + 1))
                    else:
                        raise

        return ""

    async def compress_document(self, text: str, doc_metadata: Dict) -> str:
        """Compress a full document, handling chunking if necessary."""
        chunker = TextChunker(max_chars_per_chunk=self.config.max_tokens_per_chunk * 4)
        chunks = chunker.chunk(text)

        print(f"  Document split into {len(chunks)} chunk(s)")

        # Process chunks sequentially within a document to maintain coherence,
        # but documents themselves are processed concurrently
        compressed_parts = []
        for i, chunk in enumerate(chunks, 1):
            print(f"  Processing chunk {i}/{len(chunks)}...")
            part = await self.compress_chunk(chunk, i, len(chunks), doc_metadata)
            compressed_parts.append(part)

            if i < len(chunks):
                await asyncio.sleep(0.5)

        return "\n\n".join(compressed_parts)


# ---------------------------------------------------------------------------
# Document Discovery
# ---------------------------------------------------------------------------

def discover_documents(config: CompressorConfig) -> List[Dict]:
    """Discover all documents in the downloads/specs directory."""
    specs_dir = Path(config.specs_dir)
    if not specs_dir.exists():
        print(f"ERROR: Specs directory not found: {specs_dir}")
        sys.exit(1)

    documents = []
    extensions = {".pdf", ".html", ".htm", ".txt", ".md", ".docx", ".doc"}

    for ext in extensions:
        for file_path in specs_dir.rglob(f"*{ext}"):
            relative = file_path.relative_to(specs_dir)
            source = relative.parts[0] if len(relative.parts) > 1 else "unknown"
            doc_id = _extract_doc_id(file_path.stem, source)

            documents.append({
                "id": doc_id,
                "title": doc_id,
                "source": source.lower(),
                "path": str(file_path),
                "relative_path": str(relative),
                "extension": ext,
            })

    refs_path = Path(config.references_json)
    if refs_path.exists():
        try:
            with open(refs_path, "r", encoding="utf-8") as f:
                refs_data = json.load(f)
            graph = refs_data.get("graph", refs_data)
            nodes = graph.get("nodes", []) if isinstance(graph, dict) else []

            node_map = {n["id"]: n for n in nodes}
            for doc in documents:
                node = node_map.get(doc["id"])
                if node:
                    doc["title"] = node.get("title", doc["title"])
                    doc["type"] = node.get("type", "unknown")
                    doc["is_draft"] = node.get("isDraft", False)
                    doc["is_eudi_core"] = node.get("isEudiCore", False)
        except Exception as e:
            print(f"[WARN] Could not load references.json: {e}")

    return sorted(documents, key=lambda x: x["path"])


def _extract_doc_id(stem: str, source: str) -> str:
    """Extract a document ID from filename."""
    etsi_match = re.match(r"(en|ts|tr|es|eg|sr)_(\d{3})(\d{3})(\d{2})?", stem, re.I)
    if etsi_match:
        prefix = etsi_match.group(1).upper()
        num = etsi_match.group(2) + " " + etsi_match.group(3)
        part = etsi_match.group(4)
        if part:
            num += "-" + str(int(part))
        return f"{prefix} {num}"

    rfc_match = re.match(r"rfc(\d+)", stem, re.I)
    if rfc_match:
        return f"RFC {rfc_match.group(1)}"

    oidf_match = re.match(r"OpenID.*|HAIP|SD-JWT.*", stem, re.I)
    if oidf_match:
        return stem.replace("_", " ")

    return stem.replace("_", " ").replace("-", " ")


# ---------------------------------------------------------------------------
# Async Main Pipeline
# ---------------------------------------------------------------------------

class AsyncCompressionPipeline:
    def __init__(self, config: CompressorConfig):
        self.config = config
        self.loader = DocumentLoader()
        self.compressor = AsyncLegalCompressor(config)
        self.output_dir = Path(config.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.progress_file = self.output_dir / "_compression_progress.json"
        self.completed = self._load_progress()

    def _load_progress(self) -> set:
        if self.progress_file.exists():
            with open(self.progress_file, "r", encoding="utf-8") as f:
                return set(json.load(f))
        return set()

    def _save_progress(self):
        with open(self.progress_file, "w", encoding="utf-8") as f:
            json.dump(list(self.completed), f, indent=2)

    def _get_output_path(self, doc: Dict) -> Path:
        relative = Path(doc["relative_path"])
        out_path = self.output_dir / relative.parent / f"{relative.stem}{self.config.compression_suffix}"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        return out_path

    async def process_document(self, doc: Dict, stats: Dict) -> None:
        """Process a single document."""
        doc_key = doc["path"]

        print(f"\n[PROCESS] {doc['id']} ({doc['source']})")
        print(f"  Path: {doc['path']}")

        text = self.loader.load(doc["path"])
        if not text:
            print(f"  [FAIL] Could not load text")
            stats["failed"] += 1
            return

        raw_chars = len(text)
        stats["total_tokens_in"] += raw_chars // 4
        print(f"  Raw text: {raw_chars:,} chars (~{raw_chars // 4:,} tokens)")

        try:
            compressed = await self.compressor.compress_document(text, doc)
            compressed_chars = len(compressed)
            stats["total_chars_out"] += compressed_chars

            if not compressed.startswith("# "):
                header = f"# {doc['id']}: {doc.get('title', doc['id'])}\n"
                header += f"**Source**: {doc.get('source', 'unknown')} | **Type**: {doc.get('type', 'unknown')}\n"
                header += f"**Original**: `{doc['path']}`\n\n"
                compressed = header + compressed

            out_path = self._get_output_path(doc)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(compressed)

            ratio = raw_chars / max(compressed_chars, 1)
            print(f"  [OK] Compressed to {compressed_chars:,} chars (ratio: {ratio:.1f}x)")
            print(f"  Output: {out_path}")

            self.completed.add(doc_key)
            stats["success"] += 1

        except Exception as e:
            print(f"  [FAIL] Compression error: {e}")
            stats["failed"] += 1

    async def run(self):
        documents = discover_documents(self.config)
        print(f"Discovered {len(documents)} documents")
        print(f"Already completed: {len(self.completed)}")
        print(f"Output directory: {self.output_dir}")
        print(f"Concurrency: {self.config.concurrency}")
        print("=" * 60)

        stats = {"success": 0, "failed": 0, "skipped": 0, "total_tokens_in": 0, "total_chars_out": 0}

        # Filter out already completed
        pending = [d for d in documents if d["path"] not in self.completed]
        stats["skipped"] = len(documents) - len(pending)

        if not pending:
            print("No pending documents to process.")
        else:
            # Process documents concurrently
            tasks = [self.process_document(doc, stats) for doc in pending]
            await asyncio.gather(*tasks)

        self._save_progress()

        print("\n" + "=" * 60)
        print("COMPRESSION COMPLETE")
        print("=" * 60)
        print(f"Success: {stats['success']}")
        print(f"Failed: {stats['failed']}")
        print(f"Skipped: {stats['skipped']}")
        if stats['total_chars_out'] > 0:
            overall_ratio = stats['total_tokens_in'] * 4 / stats['total_chars_out']
            print(f"Overall compression ratio: {overall_ratio:.1f}x")
        print(f"Output directory: {self.output_dir}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Compress legal/regulatory documents to structured markdown using DeepSeek R1 (Async)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Default run (uses LLM_API_KEY env var)
  python compress_legal_docs.py

  # Use OpenRouter with 10 concurrent workers
  python compress_legal_docs.py --provider openrouter --model deepseek/deepseek-r1 --concurrency 10

  # Custom directories, low rate limit
  python compress_legal_docs.py --downloads-dir ./downloads --output-dir ./compressed --rpm 10

  # Resume interrupted run
  python compress_legal_docs.py --output-dir ./compressed
        """
    )
    parser.add_argument("--downloads-dir", default="./downloads", help="Downloads root directory")
    parser.add_argument("--output-dir", default="./compressed", help="Output directory for compressed markdown")
    parser.add_argument("--provider", default="deepseek", choices=["deepseek", "openrouter"], help="API provider")
    parser.add_argument("--model", default="deepseek-reasoner", help="Model name")
    parser.add_argument("--api-key", default=None, help="API key (or set env var)")
    parser.add_argument("--base-url", default=None, help="Custom API base URL")
    parser.add_argument("--concurrency", type=int, default=10, help="Max concurrent API calls")
    parser.add_argument("--rpm", type=int, default=30, help="Requests per minute limit")
    parser.add_argument("--max-chunk-tokens", type=int, default=100000, help="Max input tokens per chunk")
    parser.add_argument("--max-output-tokens", type=int, default=50000, help="Max output tokens per request")
    parser.add_argument("--temperature", type=float, default=0.2, help="Sampling temperature")
    parser.add_argument("--retry", type=int, default=3, help="Retry attempts per chunk")

    args = parser.parse_args()

    config = CompressorConfig(
        downloads_dir=args.downloads_dir,
        output_dir=args.output_dir,
        specs_dir=os.path.join(args.downloads_dir, "specs"),
        references_json=os.path.join(args.downloads_dir, "references.json"),
        api_provider=args.provider,
        api_key=args.api_key,
        base_url=args.base_url,
        model=args.model,
        max_tokens_per_chunk=args.max_chunk_tokens,
        max_output_tokens=args.max_output_tokens,
        temperature=args.temperature,
        concurrency=args.concurrency,
        requests_per_minute=args.rpm,
        retry_attempts=args.retry,
    )

    pipeline = AsyncCompressionPipeline(config)
    asyncio.run(pipeline.run())


if __name__ == "__main__":
    main()
