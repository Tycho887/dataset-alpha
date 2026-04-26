"""
Knowledge-Base Builder with Density Filtering & Embedding Deduplication
========================================================================
Reads kb_crawler.py output and produces:
  1. knowledge_base/     – Deduplicated, density-filtered markdown per subtopic
  2. qa_pairs/           – Q&A pairs from compressed chunks
  3. fine_tuning/        – Alpaca & ChatML datasets

Three defence layers against token bloat:
  • Density heuristics   – drop list-heavy / repetitive / nav-like content
  • Embedding dedup      – cosine-similarity merge of near-duplicate chunks
  • LLM compression      – optional DeepSeek distillation for verbose survivors

Usage:
    # Zero-cost local run (filtering + dedup only)
    python kb_builder_v2.py --input ./kb_output --output ./pipeline_out --mode local

    # With cheap LLM compression + Q&A (~$0.20-0.40 per 500 chunks)
    python kb_builder_v2.py --input ./kb_output --output ./pipeline_out \
        --mode hybrid --llm-key $DEEPSEEK_API_KEY

Dependencies:
    pip install sentence-transformers numpy scikit-learn aiohttp
"""

import argparse
import asyncio
import hashlib
import json
import logging
import os
import re
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

try:
    import aiohttp
except ImportError:
    aiohttp = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s"
)
logger = logging.getLogger("kb_builder")


# =============================================================================
# CONFIGURATION
# =============================================================================

@dataclass
class Config:
    input_dir: str = "./kb_output"
    output_dir: str = "./pipeline_out"
    mode: str = "local"                     # local | hybrid | llm

    # Subtopic taxonomy (customise for your domain)
    taxonomy: Dict[str, str] = field(default_factory=lambda: {
        "protocol_flows": (
            "Authorization code flow, credential offer, presentation exchange, "
            "token endpoint, pushed authorization request (PAR), wallet activation, "
            "OID4VCI issuance protocol, OID4VP presentation protocol, OAuth 2.0 flows."
        ),
        "cryptography_security": (
            "Digital signatures, key management, SD-JWT selective disclosure, "
            "JWS, JWE, JWK, ECDSA, EdDSA, RSA, certificates, PKI, post-quantum crypto, "
            "hashing, encryption, integrity protection."
        ),
        "data_schemas_formats": (
            "JWT claims structure, mdoc CBOR encoding, JSON schema definitions, "
            "credential metadata, authorization details, data types, fields, "
            "ISO 18013-5, mobile driving licence encoding."
        ),
        "trust_framework_compliance": (
            "eIDAS trust framework, qualified electronic signature, attestation mechanisms, "
            "certification, conformance testing, PID provider requirements, "
            "wallet provider accreditation, trust anchors."
        ),
        "implementation_api": (
            "REST endpoints, HTTP methods, status codes, error handling, "
            "API paths, request/response payloads, implementation examples, "
            "SDK usage, library integration, developer guides."
        ),
        "architecture_concepts": (
            "Wallet architecture, issuer and verifier roles, relying party interactions, "
            "ecosystem interoperability, ARF architecture reference framework, "
            "component diagrams, system boundaries, role definitions."
        ),
        "regulatory_legal": (
            "PSD2 payment services, GDPR data protection, legal obligations, "
            "directive and regulation text, compliance requirements, "
            "jurisdiction, legislation articles, strong customer authentication (SCA)."
        ),
    })

    routing_threshold: float = 0.18
    max_subtopics_per_chunk: int = 2

    # Density filtering
    min_density_score: float = 0.25          # drop chunks below this
    max_list_ratio: float = 0.70             # drop if >70% lines are list items
    min_unique_word_ratio: float = 0.15      # drop if <15% unique words
    max_proper_noun_ratio: float = 0.55      # drop if >55% capitalised words (name lists)

    # Deduplication
    dedup_threshold: float = 0.92            # cosine similarity threshold for merge

    # LLM compression (optional)
    compress_via_llm: bool = False
    compress_threshold: float = 0.35         # compress chunks with density 0.25-0.35
    llm_base_url: str = "https://api.deepseek.com"
    llm_api_key: str = ""
    llm_model: str = "deepseek-chat"
    qa_model: str = "deepseek-chat"
    qa_temperature: float = 0.2
    qa_max_tokens: int = 1500
    qa_concurrency: int = 8
    qa_per_chunk: int = 2

    checkpoint_file: str = "kb_builder_state.json"


# =============================================================================
# DATA LOADING
# =============================================================================

class CrawlerLoader:
    """Loads chunks + metadata produced by kb_crawler.py."""

    def __init__(self, input_dir: str):
        self.input_dir = Path(input_dir)
        self.manifest_path = self.input_dir / "manifest.jsonl"

    def load_all(self) -> List[Dict]:
        if not self.manifest_path.exists():
            logger.error(f"Manifest not found: {self.manifest_path}")
            return []

        chunks: List[Dict] = []
        with open(self.manifest_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue

                page_dir = self.input_dir / record.get("page_dir", "")
                chunks_file = page_dir / "chunks.jsonl"
                meta_file = page_dir / "meta.json"

                if not chunks_file.exists():
                    continue

                meta = json.loads(meta_file.read_text(encoding="utf-8")) if meta_file.exists() else {}

                with open(chunks_file, "r", encoding="utf-8") as cf:
                    for c_line in cf:
                        c_line = c_line.strip()
                        if not c_line:
                            continue
                        try:
                            chunk = json.loads(c_line)
                        except json.JSONDecodeError:
                            continue

                        chunk["_page_meta"] = meta
                        chunk["_source_title"] = meta.get("title", "") or record.get("title", "")
                        chunk["_source_url"] = meta.get("url", "") or record.get("url", "")
                        chunk["_domain"] = meta.get("domain", "") or record.get("domain", "")
                        chunk["_depth"] = record.get("depth", 0)
                        chunks.append(chunk)

        logger.info(f"Loaded {len(chunks)} raw chunks from {self.input_dir}")
        return chunks


# =============================================================================
# DENSITY FILTER
# =============================================================================

class DensityFilter:
    """
    Heuristic filter that drops low-information chunks:
      - Name lists (high proper-noun ratio)
      - TOC / nav pages (high list ratio)
      - Repetitive boilerplate (low unique-word ratio)
      - Very short fragments
    """

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def score(self, text: str) -> Tuple[float, Dict]:
        """Return density score ∈ [0,1] and diagnostic dict."""
        if not text or len(text) < 150:
            return 0.0, {"reason": "too_short"}

        words = re.findall(r"\b\w+\b", text)
        if not words:
            return 0.0, {"reason": "no_words"}

        lines = [l.strip() for l in text.splitlines() if l.strip()]

        # 1. Unique word ratio (vocabulary richness)
        unique = set(w.lower() for w in words)
        unique_ratio = len(unique) / len(words)

        # 2. List-like line ratio (TOC, nav, name lists)
        list_patterns = [
            r"^[-•\*]\s",           # bullet
            r"^\d+[.\)]\s",        # numbered
            r"^\w+\s+\w+\s+(Contribution|Agreement|WG|Working Group)",  # name lists
        ]
        list_lines = sum(1 for l in lines if any(re.search(p, l) for p in list_patterns))
        list_ratio = list_lines / len(lines) if lines else 0

        # 3. Proper noun ratio (capitalised words that aren't sentence-start)
        # Simple heuristic: words with uppercase first letter after a space or newline
        proper = re.findall(r"(?<=\s)[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*", text)
        proper_ratio = len(proper) / len(words)

        # 4. Sentence density (avg words per sentence)
        sentences = re.split(r"[.!?]+", text)
        sentence_density = len(words) / len(sentences) if sentences else 0

        # 5. Punctuation / structure ratio (indicates prose vs lists)
        punct_ratio = sum(1 for c in text if c in ".,;:") / len(text)

        # Composite score (higher = denser, more valuable)
        score = (
            0.30 * unique_ratio +
            0.25 * (1 - list_ratio) +
            0.20 * (1 - min(proper_ratio * 2, 1)) +  # penalise name lists
            0.15 * min(sentence_density / 20, 1) +
            0.10 * min(punct_ratio * 30, 1)
        )

        diagnostics = {
            "unique_ratio": round(unique_ratio, 3),
            "list_ratio": round(list_ratio, 3),
            "proper_ratio": round(proper_ratio, 3),
            "sentence_density": round(sentence_density, 1),
            "punct_ratio": round(punct_ratio, 4),
            "score": round(score, 3),
        }
        return score, diagnostics

    def filter_chunks(self, chunks: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
        kept, dropped = [], []
        for c in chunks:
            text = c.get("text", "")
            score, diag = self.score(text)
            c["_density"] = score
            c["_density_diag"] = diag

            if score < self.cfg.min_density_score:
                dropped.append(c)
                continue
            if diag["list_ratio"] > self.cfg.max_list_ratio:
                dropped.append(c)
                continue
            if diag["unique_ratio"] < self.cfg.min_unique_word_ratio:
                dropped.append(c)
                continue
            if diag["proper_ratio"] > self.cfg.max_proper_noun_ratio:
                dropped.append(c)
                continue

            kept.append(c)

        logger.info(f"Density filter: {len(kept)} kept, {len(dropped)} dropped")
        if dropped:
            top_drop_reasons = defaultdict(int)
            for d in dropped:
                top_drop_reasons[d["_density_diag"].get("reason", "low_score")] += 1
            for reason, cnt in sorted(top_drop_reasons.items(), key=lambda x: -x[1])[:5]:
                logger.info(f"  Drop reason '{reason}': {cnt} chunks")
        return kept, dropped


# =============================================================================
# EMBEDDING DEDUPLICATOR
# =============================================================================

class EmbeddingDedup:
    """
    Merges near-duplicate chunks using cosine similarity on sentence embeddings.
    Keeps the longest / most complete version as the survivor.
    """

    def __init__(self, cfg: Config):
        self.cfg = cfg
        logger.info("Loading embedding model for deduplication...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        logger.info("Model loaded")

    def deduplicate(self, chunks: List[Dict]) -> List[Dict]:
        if not chunks:
            return []

        texts = [c.get("text", "")[:2000] for c in chunks]
        embeddings = self.model.encode(texts, show_progress_bar=False, convert_to_numpy=True)

        n = len(chunks)
        keep = [True] * n
        merge_log = []

        # Greedy clustering: sort by length (prefer longer), mark duplicates
        lengths = [len(c.get("text", "")) for c in chunks]
        order = sorted(range(n), key=lambda i: lengths[i], reverse=True)

        for idx, i in enumerate(order):
            if not keep[i]:
                continue
            # Compare against all remaining unprocessed chunks
            for j in order[idx+1:]:
                if not keep[j]:
                    continue
                sim = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
                if sim >= self.cfg.dedup_threshold:
                    keep[j] = False
                    merge_log.append((chunks[i].get("id", i), chunks[j].get("id", j), round(float(sim), 3)))

        survivors = [chunks[i] for i in range(n) if keep[i]]
        logger.info(f"Deduplication: {len(survivors)} survivors from {len(chunks)} chunks")
        logger.info(f"  Merged {len(merge_log)} near-duplicate pairs (threshold {self.cfg.dedup_threshold})")
        if merge_log:
            logger.info(f"  Example merge: {merge_log[0]}")
        return survivors


# =============================================================================
# LLM COMPRESSOR (optional, cheap)
# =============================================================================

class LLMCompressor:
    """
    Sends verbose but relevant chunks to an LLM for distillation.
    Much cheaper than generating Q&A for every chunk — only compresses
    chunks with marginal density scores.
    """

    SYSTEM = (
        "You are a technical documentation compressor. "
        "Rewrite the provided text into dense, information-rich markdown. "
        "Rules:\n"
        "1. Remove redundant examples, name lists, TOC entries, and boilerplate.\n"
        "2. Preserve ALL technical details: protocol steps, field names, requirements, MUST/SHALL statements.\n"
        "3. Use concise bullet points and tables where appropriate.\n"
        "4. Do NOT add information not present in the original.\n"
        "5. Output only the compressed markdown, no preamble."
    )

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.semaphore = asyncio.Semaphore(cfg.qa_concurrency)
        self.session: Optional[Any] = None
        self.compressed_count = 0
        self.skipped_count = 0

    async def _get_session(self):
        if self.session is None and aiohttp is not None:
            self.session = aiohttp.ClientSession()
        return self.session

    async def compress(self, chunk: Dict) -> Optional[str]:
        if not self.cfg.compress_via_llm or not self.cfg.llm_api_key:
            return None

        text = chunk.get("text", "")
        if len(text) < 300:
            return None  # not worth the API call

        # Only compress marginal-density chunks
        density = chunk.get("_density", 1.0)
        if density >= self.cfg.compress_threshold:
            self.skipped_count += 1
            return None

        async with self.semaphore:
            session = await self._get_session()
            payload = {
                "model": self.cfg.llm_model,
                "messages": [
                    {"role": "system", "content": self.SYSTEM},
                    {"role": "user", "content": f"Compress this text:\n\n{text[:4000]}"},
                ],
                "temperature": 0.1,
                "max_tokens": 2000,
            }
            headers = {
                "Authorization": f"Bearer {self.cfg.llm_api_key}",
                "Content-Type": "application/json",
            }
            try:
                async with session.post(
                    f"{self.cfg.llm_base_url}/v1/chat/completions",
                    headers=headers,
                    json=payload,
                ) as resp:
                    if resp.status != 200:
                        text_err = await resp.text()
                        raise RuntimeError(f"HTTP {resp.status}: {text_err[:200]}")
                    data = await resp.json()
                    compressed = data["choices"][0]["message"]["content"].strip()
                    self.compressed_count += 1
                    return compressed
            except Exception as e:
                logger.warning(f"Compression failed for {chunk.get('id')}: {e}")
                return None

    async def close(self):
        if self.session:
            await self.session.close()


# =============================================================================
# SUBTOPIC ROUTER (local embeddings)
# =============================================================================

class SubtopicRouter:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.subtopics = list(cfg.taxonomy.keys())
        self.descriptions = list(cfg.taxonomy.values())
        logger.info("Loading embedding model for routing...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.desc_embeddings = self.model.encode(
            self.descriptions, show_progress_bar=False, convert_to_numpy=True
        )
        logger.info(f"Router ready for {len(self.subtopics)} subtopics")

    def route(self, chunk: Dict) -> List[Tuple[str, float]]:
        text = chunk.get("text", "")
        headings = " ".join(chunk.get("headings", []))
        preview = f"{headings} {text}"[:3000]
        emb = self.model.encode([preview], convert_to_numpy=True)
        sims = cosine_similarity(emb, self.desc_embeddings)[0]
        matches = []
        for idx, score in enumerate(sims):
            if score >= self.cfg.routing_threshold:
                matches.append((self.subtopics[idx], float(score)))
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[: self.cfg.max_subtopics_per_chunk]


# =============================================================================
# LLM CLIENT (for Q&A)
# =============================================================================

class LLMClient:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.semaphore = asyncio.Semaphore(cfg.qa_concurrency)
        self.session: Optional[Any] = None

    async def _get_session(self):
        if self.session is None and aiohttp is not None:
            self.session = aiohttp.ClientSession()
        return self.session

    async def complete(self, system: str, user: str, temperature: Optional[float] = None) -> str:
        if not aiohttp:
            raise RuntimeError("aiohttp not installed")
        async with self.semaphore:
            session = await self._get_session()
            payload = {
                "model": self.cfg.qa_model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "temperature": temperature if temperature is not None else self.cfg.qa_temperature,
                "max_tokens": self.cfg.qa_max_tokens,
            }
            headers = {
                "Authorization": f"Bearer {self.cfg.llm_api_key}",
                "Content-Type": "application/json",
            }
            async with session.post(
                f"{self.cfg.llm_base_url}/v1/chat/completions",
                headers=headers,
                json=payload,
            ) as resp:
                if resp.status != 200:
                    text = await resp.text()
                    raise RuntimeError(f"LLM HTTP {resp.status}: {text[:200]}")
                data = await resp.json()
                return data["choices"][0]["message"]["content"]

    async def close(self):
        if self.session:
            await self.session.close()


# =============================================================================
# Q&A GENERATOR
# =============================================================================

class QAGenerator:
    SYSTEM_PROMPT = (
        "You are a technical documentation assistant. "
        "Given an excerpt from a technical specification, generate concise, accurate Q&A pairs. "
        "Each question should be something a developer or architect would ask. "
        "Each answer must be grounded strictly in the provided text. "
        "Include specific field names, protocol steps, or requirements when present. "
        "If the text contains no extractable technical knowledge, return an empty list."
        "\n\n"
        "Respond with valid JSON only: {\"qa_pairs\": [{\"question\": \"...\", \"answer\": \"...\"}]}"
    )

    def __init__(self, cfg: Config, llm: Optional[LLMClient] = None):
        self.cfg = cfg
        self.llm = llm

    async def generate(self, chunk: Dict) -> List[Dict]:
        if self.llm is None:
            return []
        text = chunk.get("text", "")[:4000]
        headings = chunk.get("headings", [])
        heading_ctx = f"Section headings: {headings}\n\n" if headings else ""
        user_prompt = f"{heading_ctx}Text excerpt:\n\n{text}"
        try:
            raw = await self.llm.complete(self.SYSTEM_PROMPT, user_prompt)
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.strip("`")
                if raw.lower().startswith("json"):
                    raw = raw[4:].strip()
            parsed = json.loads(raw)
            pairs = parsed.get("qa_pairs", [])
        except Exception as e:
            logger.debug(f"Q&A parse error: {e}")
            return []

        results = []
        for p in pairs:
            q = p.get("question", "").strip()
            a = p.get("answer", "").strip()
            if not q or not a:
                continue
            results.append({
                "question": q,
                "answer": a,
                "source_url": chunk.get("source_url", chunk.get("_source_url", "")),
                "source_title": chunk.get("source_title", chunk.get("_source_title", "")),
                "source_domain": chunk.get("source_domain", chunk.get("_domain", "")),
                "chunk_id": chunk.get("id", ""),
                "headings": chunk.get("headings", []),
            })
        return results


# =============================================================================
# KNOWLEDGE BASE BUILDER
# =============================================================================

class KnowledgeBaseBuilder:
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def build(self, subtopic: str, chunks: List[Dict]) -> str:
        lines = [
            f"# {subtopic.replace('_', ' ').title()}",
            "",
            f"> Auto-generated from {len(chunks)} source chunks.",
            f"> Generated: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}",
            "",
            "---",
            "",
        ]
        by_source: Dict[str, List[Dict]] = defaultdict(list)
        for c in chunks:
            url = c.get("source_url", c.get("_source_url", "unknown"))
            by_source[url].append(c)

        for url, src_chunks in by_source.items():
            title = src_chunks[0].get("source_title", src_chunks[0].get("_source_title", "Untitled"))
            lines.append(f"## [{title}]({url})")
            lines.append("")
            for c in src_chunks:
                headings = c.get("headings", [])
                if headings:
                    lines.append(f"### {' > '.join(headings[:3])}")
                lines.append("")
                lines.append(c.get("text", ""))
                lines.append("")
                lines.append(f"*Source: [{url}]({url}) | chunk `{c.get('id', 'n/a')}`*")
                lines.append("")
            lines.append("---")
            lines.append("")
        return "\n".join(lines)


# =============================================================================
# FINE-TUNING FORMATTER
# =============================================================================

class FTFormatter:
    SYSTEM_MSG = (
        "You are an expert assistant for European Digital Identity, eIDAS 2.0, "
        "OpenID4VCI, OpenID4VP, and related standards. Answer accurately and cite sources."
    )

    def to_alpaca(self, qa_list: List[Dict]) -> List[Dict]:
        return [{
            "instruction": qa["question"],
            "input": "",
            "output": qa["answer"],
            "metadata": {
                "source_url": qa.get("source_url", ""),
                "source_title": qa.get("source_title", ""),
                "chunk_id": qa.get("chunk_id", ""),
            }
        } for qa in qa_list]

    def to_chatml(self, qa_list: List[Dict]) -> List[Dict]:
        return [{
            "messages": [
                {"role": "system", "content": self.SYSTEM_MSG},
                {"role": "user", "content": qa["question"]},
                {"role": "assistant", "content": qa["answer"]},
            ],
            "metadata": {
                "source_url": qa.get("source_url", ""),
                "source_title": qa.get("source_title", ""),
                "chunk_id": qa.get("chunk_id", ""),
            }
        } for qa in qa_list]


# =============================================================================
# CHECKPOINT
# =============================================================================

class Checkpoint:
    def __init__(self, path: Path):
        self.path = path
        self.done_qa: Set[str] = set()
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                self.done_qa = set(data.get("done_qa", []))
                logger.info(f"Resumed: {len(self.done_qa)} Q&A chunks already done")
            except Exception:
                pass

    def is_qa_done(self, chunk_id: str) -> bool:
        return chunk_id in self.done_qa

    def mark_qa_done(self, chunk_id: str):
        self.done_qa.add(chunk_id)

    def save(self):
        self.path.write_text(json.dumps({"done_qa": list(self.done_qa)}), encoding="utf-8")


# =============================================================================
# ORCHESTRATOR
# =============================================================================

class Pipeline:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.loader = CrawlerLoader(cfg.input_dir)
        self.density = DensityFilter(cfg)
        self.dedup = EmbeddingDedup(cfg)
        self.compressor = LLMCompressor(cfg)
        self.router = SubtopicRouter(cfg)
        self.llm: Optional[LLMClient] = None
        if cfg.mode in ("hybrid", "llm"):
            if not cfg.llm_api_key:
                raise ValueError("LLM mode requires --llm-key")
            self.llm = LLMClient(cfg)
        self.qa_gen = QAGenerator(cfg, self.llm)
        self.kb_builder = KnowledgeBaseBuilder(cfg)
        self.ft_fmt = FTFormatter()
        self.ckpt = Checkpoint(Path(cfg.output_dir) / cfg.checkpoint_file)
        self.out_dir = Path(cfg.output_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)

    async def run(self):
        logger.info("=" * 60)
        logger.info("Knowledge-Base Builder v2 (with density filtering)")
        logger.info(f"Mode: {self.cfg.mode}")
        logger.info("=" * 60)

        # 1. Load
        chunks = self.loader.load_all()
        if not chunks:
            logger.error("No chunks loaded. Exiting.")
            return

        # 2. Density filter
        chunks, dropped = self.density.filter_chunks(chunks)
        if dropped:
            drop_dir = self.out_dir / "dropped_chunks"
            drop_dir.mkdir(exist_ok=True)
            with open(drop_dir / "dropped.jsonl", "w", encoding="utf-8") as f:
                for d in dropped:
                    f.write(json.dumps({
                        "id": d.get("id"),
                        "density": d.get("_density"),
                        "diag": d.get("_density_diag"),
                        "preview": d.get("text", "")[:300],
                    }, ensure_ascii=False) + "\n")
            logger.info(f"Wrote {len(dropped)} dropped chunks to {drop_dir}/dropped.jsonl for inspection")

        # 3. Deduplicate
        chunks = self.dedup.deduplicate(chunks)

        # 4. Optional LLM compression for marginal-density survivors
        if self.cfg.compress_via_llm and self.cfg.mode in ("hybrid", "llm"):
            logger.info("Running LLM compression on marginal-density chunks...")
            compress_tasks = [self.compressor.compress(c) for c in chunks]
            compressed_texts = await asyncio.gather(*compress_tasks, return_exceptions=True)
            for chunk, compressed in zip(chunks, compressed_texts):
                if isinstance(compressed, str) and compressed:
                    chunk["text"] = compressed
                    chunk["_compressed"] = True
            logger.info(f"Compressed {self.compressor.compressed_count} chunks, "
                        f"skipped {self.compressor.skipped_count} (already dense)")
            await self.compressor.close()

        # 5. Route to subtopics
        logger.info("Routing chunks to subtopics...")
        subtopic_chunks: Dict[str, List[Dict]] = defaultdict(list)
        unassigned: List[Dict] = []
        for chunk in chunks:
            routes = self.router.route(chunk)
            if routes:
                for subtopic, score in routes:
                    chunk["_route_score"] = score
                    subtopic_chunks[subtopic].append(chunk)
            else:
                unassigned.append(chunk)
        if unassigned:
            subtopic_chunks["general"].extend(unassigned)

        for st, chs in sorted(subtopic_chunks.items(), key=lambda x: -len(x[1])):
            logger.info(f"  {st}: {len(chs)} chunks")

        # 6. Build Knowledge Base
        kb_dir = self.out_dir / "knowledge_base"
        kb_dir.mkdir(exist_ok=True)
        logger.info("Building knowledge-base articles...")
        for subtopic, chs in subtopic_chunks.items():
            md = self.kb_builder.build(subtopic, chs)
            (kb_dir / f"{subtopic}.md").write_text(md, encoding="utf-8")
        logger.info(f"KB articles written to {kb_dir}")

        # 7. Generate Q&A (optional)
        qa_dir = self.out_dir / "qa_pairs"
        qa_dir.mkdir(exist_ok=True)
        qa_by_subtopic: Dict[str, List[Dict]] = defaultdict(list)
        all_qa: List[Dict] = []

        if self.cfg.mode in ("hybrid", "llm"):
            logger.info("Generating Q&A pairs via LLM...")
            tasks = []
            task_meta = []
            for subtopic, chs in subtopic_chunks.items():
                for c in chs:
                    cid = c.get("id", "")
                    if not cid or self.ckpt.is_qa_done(cid):
                        continue
                    tasks.append(self.qa_gen.generate(c))
                    task_meta.append((subtopic, c))

            batch_size = self.cfg.qa_concurrency * 2
            for i in range(0, len(tasks), batch_size):
                batch_tasks = tasks[i:i+batch_size]
                batch_meta = task_meta[i:i+batch_size]
                results = await asyncio.gather(*batch_tasks, return_exceptions=True)
                for (subtopic, chunk), result in zip(batch_meta, results):
                    cid = chunk.get("id", "")
                    if isinstance(result, list):
                        for qa in result:
                            qa["subtopic"] = subtopic
                        qa_by_subtopic[subtopic].extend(result)
                        all_qa.extend(result)
                    self.ckpt.mark_qa_done(cid)
                self.ckpt.save()
                logger.info(f"  Q&A progress: {min(i+batch_size, len(tasks))}/{len(tasks)}")

            with open(qa_dir / "all_qa_pairs.jsonl", "w", encoding="utf-8") as f:
                for qa in all_qa:
                    f.write(json.dumps(qa, ensure_ascii=False) + "\n")
            for subtopic, qas in qa_by_subtopic.items():
                with open(qa_dir / f"{subtopic}_qa.jsonl", "w", encoding="utf-8") as f:
                    for qa in qas:
                        f.write(json.dumps(qa, ensure_ascii=False) + "\n")
            logger.info(f"Q&A pairs written: {len(all_qa)} total")
        else:
            logger.info("Skipping Q&A generation (local mode).")

        # 8. Fine-tuning datasets
        ft_dir = self.out_dir / "fine_tuning"
        ft_dir.mkdir(exist_ok=True)
        if all_qa:
            alpaca = self.ft_fmt.to_alpaca(all_qa)
            chatml = self.ft_fmt.to_chatml(all_qa)
            with open(ft_dir / "alpaca.jsonl", "w", encoding="utf-8") as f:
                for row in alpaca:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
            with open(ft_dir / "chatml.jsonl", "w", encoding="utf-8") as f:
                for row in chatml:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
            logger.info(f"Fine-tuning datasets: {len(alpaca)} rows")
        else:
            logger.info("No Q&A generated; writing raw chunk datasets...")
            with open(ft_dir / "raw_chunks.jsonl", "w", encoding="utf-8") as f:
                for subtopic, chs in subtopic_chunks.items():
                    for c in chs:
                        f.write(json.dumps({
                            "text": c.get("text", ""),
                            "subtopic": subtopic,
                            "metadata": {
                                "source_url": c.get("source_url", c.get("_source_url", "")),
                                "source_title": c.get("source_title", c.get("_source_title", "")),
                                "chunk_id": c.get("id", ""),
                            }
                        }, ensure_ascii=False) + "\n")

        # 9. Summary
        summary = {
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "input_dir": self.cfg.input_dir,
            "raw_chunks": len(self.loader.load_all()),  # reload count is cheap enough
            "after_density_filter": sum(len(v) for v in subtopic_chunks.values()) + len(unassigned),
            "subtopic_distribution": {k: len(v) for k, v in subtopic_chunks.items()},
            "qa_pairs_generated": len(all_qa),
            "outputs": {
                "knowledge_base": str(kb_dir),
                "qa_pairs": str(qa_dir) if all_qa else None,
                "fine_tuning": str(ft_dir),
            }
        }
        (self.out_dir / "summary.json").write_text(
            json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
        )

        if self.llm:
            await self.llm.close()

        logger.info("=" * 60)
        logger.info("Pipeline complete")
        logger.info(f"  Final chunks  : {summary['after_density_filter']}")
        logger.info(f"  Q&A pairs     : {len(all_qa)}")
        logger.info(f"  Output dir    : {self.out_dir}")
        logger.info("=" * 60)


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="KB Builder with Density Filtering")
    parser.add_argument("--input", default="./kb_output", help="Crawler output directory")
    parser.add_argument("--output", default="./pipeline_out", help="Pipeline output directory")
    parser.add_argument("--mode", choices=["local", "hybrid", "llm"], default="local")
    parser.add_argument("--llm-base", default="https://api.deepseek.com")
    parser.add_argument("--llm-key", default=os.environ.get("LLM_API_KEY", ""))
    parser.add_argument("--llm-model", default="deepseek-chat")
    parser.add_argument("--qa-per-chunk", type=int, default=2)
    parser.add_argument("--qa-concurrency", type=int, default=8)
    parser.add_argument("--compress", action="store_true", help="Enable LLM compression for verbose chunks")
    parser.add_argument("--dedup-threshold", type=float, default=0.92, help="Cosine similarity threshold for dedup")
    parser.add_argument("--min-density", type=float, default=0.4, help="Minimum density score to keep chunk")
    args = parser.parse_args()

    cfg = Config(
        input_dir=args.input,
        output_dir=args.output,
        mode=args.mode,
        llm_base_url=args.llm_base,
        llm_api_key=args.llm_key,
        llm_model=args.llm_model,
        qa_model=args.llm_model,
        qa_per_chunk=args.qa_per_chunk,
        qa_concurrency=args.qa_concurrency,
        compress_via_llm=args.compress,
        dedup_threshold=args.dedup_threshold,
        min_density_score=args.min_density,
    )

    p = Pipeline(cfg)
    asyncio.run(p.run())


if __name__ == "__main__":
    main()