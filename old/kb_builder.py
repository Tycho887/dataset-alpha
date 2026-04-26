"""
Knowledge-Base Builder & Q/A Generator for Crawled Data
========================================================
Reads the output from kb_crawler.py and produces three artefacts:

1. knowledge_base/     – Markdown files per subtopic with inline source links
2. qa_pairs/           – JSONL of prompt/response pairs, one per chunk
3. fine_tuning/        – Combined datasets (Alpaca & ChatML formats)

Subtopic routing is done locally with sentence-transformers (free) or
optionally refined with a cheap LLM API (DeepSeek, OpenRouter, etc.).

Usage:
    # Local-only (zero API cost)
    python kb_builder.py --input ./kb_output --output ./pipeline_out --mode local

    # With LLM for Q&A generation (cheap API)
    python kb_builder.py --input ./kb_output --output ./pipeline_out \
        --mode hybrid --llm-base https://api.deepseek.com --llm-key $KEY

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

    routing_threshold: float = 0.18         # min cosine similarity to assign subtopic
    max_subtopics_per_chunk: int = 2

    # Chunking / QA
    qa_per_chunk: int = 2
    qa_model: str = "deepseek-chat"
    qa_temperature: float = 0.2
    qa_max_tokens: int = 1500
    qa_concurrency: int = 8

    # LLM connection (optional)
    llm_base_url: str = "https://api.deepseek.com"
    llm_api_key: str = ""

    # Checkpointing
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
        """Return list of chunk dicts enriched with metadata."""
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

                meta = {}
                if meta_file.exists():
                    meta = json.loads(meta_file.read_text(encoding="utf-8"))

                with open(chunks_file, "r", encoding="utf-8") as cf:
                    for c_line in cf:
                        c_line = c_line.strip()
                        if not c_line:
                            continue
                        try:
                            chunk = json.loads(c_line)
                        except json.JSONDecodeError:
                            continue

                        # Enrich with page-level metadata
                        chunk["_page_meta"] = meta
                        chunk["_source_title"] = meta.get("title", "") or record.get("title", "")
                        chunk["_source_url"] = meta.get("url", "") or record.get("url", "")
                        chunk["_domain"] = meta.get("domain", "") or record.get("domain", "")
                        chunk["_depth"] = record.get("depth", 0)
                        chunks.append(chunk)

        logger.info(f"Loaded {len(chunks)} chunks from {self.input_dir}")
        return chunks


# =============================================================================
# SUBTOPIC ROUTER (local embeddings, zero API cost)
# =============================================================================

class SubtopicRouter:
    """
    Routes chunks to subtopics using sentence-transformers.
    Zero API calls, runs entirely locally.
    """

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.subtopics = list(cfg.taxonomy.keys())
        self.descriptions = list(cfg.taxonomy.values())
        logger.info("Loading embedding model (local)...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.desc_embeddings = self.model.encode(
            self.descriptions, show_progress_bar=False, convert_to_numpy=True
        )
        logger.info(f"Router ready for {len(self.subtopics)} subtopics")

    def route(self, chunk: Dict) -> List[Tuple[str, float]]:
        """Return list of (subtopic, score) for this chunk."""
        text = chunk.get("text", "")
        headings = " ".join(chunk.get("headings", []))
        preview = f"{headings} {text}"[:3000]

        emb = self.model.encode([preview], convert_to_numpy=True)
        sims = cosine_similarity(emb, self.desc_embeddings)[0]

        # Get top matches above threshold
        matches = []
        for idx, score in enumerate(sims):
            if score >= self.cfg.routing_threshold:
                matches.append((self.subtopics[idx], float(score)))
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[: self.cfg.max_subtopics_per_chunk]


# =============================================================================
# LLM CLIENT (optional, for Q&A and optional routing refinement)
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
            raise RuntimeError("aiohttp not installed; install with: pip install aiohttp")

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
            try:
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
            except Exception as e:
                logger.warning(f"LLM call failed: {e}")
                raise

    async def close(self):
        if self.session:
            await self.session.close()


# =============================================================================
# Q&A GENERATOR
# =============================================================================

class QAGenerator:
    """Generates question-answer pairs for a chunk using an LLM."""

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
            # Extract JSON even if wrapped in markdown fences
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

        # Enrich with source metadata
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
    """
    Builds per-subtopic markdown files.
    Simple mode = organised concatenation (zero cost).
    Hybrid/LLM mode = optional synthesis per subtopic (costs tokens).
    """

    def __init__(self, cfg: Config, llm: Optional[LLMClient] = None):
        self.cfg = cfg
        self.llm = llm

    def build(self, subtopic: str, chunks: List[Dict]) -> str:
        """Return a markdown string for this subtopic."""
        lines = [
            f"# {subtopic.replace('_', ' ').title()}",
            "",
            f"> Auto-generated knowledge base article from {len(chunks)} source chunks.",
            f"> Generated: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}",
            "",
            "---",
            "",
        ]

        # Group by source URL for readability
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

    async def build_synthesized(self, subtopic: str, chunks: List[Dict]) -> str:
        """Optional: use LLM to synthesise a coherent article."""
        if self.llm is None:
            return self.build(subtopic, chunks)

        # Build a context window from top chunks (by word count)
        sorted_chunks = sorted(chunks, key=lambda x: len(x.get("text", "")), reverse=True)
        context_parts = []
        total_words = 0
        for c in sorted_chunks:
            text = c.get("text", "")[:800]
            url = c.get("source_url", c.get("_source_url", ""))
            ctx = f"[Source: {url}]\n{text}\n"
            if total_words + len(ctx.split()) > 6000:
                break
            context_parts.append(ctx)
            total_words += len(ctx.split())

        context = "\n\n".join(context_parts)
        system = (
            "You are a technical writer creating a knowledge-base article. "
            "Synthesise the provided source excerpts into a coherent markdown article. "
            "Use headers, bullet points, and code blocks where appropriate. "
            "Preserve all specific technical details (field names, requirements, steps). "
            "Cite sources inline with markdown links, e.g. [source](url). "
            "Do not invent facts not present in the excerpts."
        )
        user = f"Subtopic: {subtopic.replace('_', ' ').title()}\n\n{context}"

        try:
            article = await self.llm.complete(system, user, temperature=0.3)
            # Ensure header
            if not article.strip().startswith("#"):
                article = f"# {subtopic.replace('_', ' ').title()}\n\n{article}"
            return article
        except Exception as e:
            logger.warning(f"Synthesis failed for {subtopic}, falling back to simple build: {e}")
            return self.build(subtopic, chunks)


# =============================================================================
# FINE-TUNING DATASET FORMATTER
# =============================================================================

class FTFormatter:
    """Converts Q&A pairs into standard fine-tuning formats."""

    SYSTEM_MSG = (
        "You are an expert assistant for European Digital Identity, eIDAS 2.0, "
        "OpenID4VCI, OpenID4VP, and related standards. Answer accurately and cite sources."
    )

    def to_alpaca(self, qa_list: List[Dict]) -> List[Dict]:
        out = []
        for qa in qa_list:
            out.append({
                "instruction": qa["question"],
                "input": "",
                "output": qa["answer"],
                "metadata": {
                    "source_url": qa.get("source_url", ""),
                    "source_title": qa.get("source_title", ""),
                    "chunk_id": qa.get("chunk_id", ""),
                }
            })
        return out

    def to_chatml(self, qa_list: List[Dict]) -> List[Dict]:
        out = []
        for qa in qa_list:
            out.append({
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
            })
        return out


# =============================================================================
# CHECKPOINT / STATE
# =============================================================================

class Checkpoint:
    def __init__(self, path: Path):
        self.path = path
        self.done_qa: Set[str] = set()
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                self.done_qa = set(data.get("done_qa", []))
                logger.info(f"Resumed checkpoint: {len(self.done_qa)} Q&A chunks already processed")
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
        self.router = SubtopicRouter(cfg)
        self.llm: Optional[LLMClient] = None
        if cfg.mode in ("hybrid", "llm"):
            if not cfg.llm_api_key:
                raise ValueError("LLM mode requires --llm-key")
            self.llm = LLMClient(cfg)
        self.qa_gen = QAGenerator(cfg, self.llm)
        self.kb_builder = KnowledgeBaseBuilder(cfg, self.llm)
        self.ft_fmt = FTFormatter()
        self.ckpt = Checkpoint(Path(cfg.output_dir) / cfg.checkpoint_file)

        self.out_dir = Path(cfg.output_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)

    async def run(self):
        logger.info("=" * 60)
        logger.info("Knowledge-Base Builder Starting")
        logger.info(f"Mode: {self.cfg.mode}")
        logger.info("=" * 60)

        # 1. Load
        chunks = self.loader.load_all()
        if not chunks:
            logger.error("No chunks loaded. Exiting.")
            return

        # 2. Route to subtopics
        logger.info("Routing chunks to subtopics (local embeddings)...")
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

        # 3. Build Knowledge Base (markdown per subtopic)
        kb_dir = self.out_dir / "knowledge_base"
        kb_dir.mkdir(exist_ok=True)
        logger.info("Building knowledge-base articles...")
        for subtopic, chs in subtopic_chunks.items():
            if self.cfg.mode == "llm":
                md = await self.kb_builder.build_synthesized(subtopic, chs)
            else:
                md = self.kb_builder.build(subtopic, chs)
            (kb_dir / f"{subtopic}.md").write_text(md, encoding="utf-8")
        logger.info(f"KB articles written to {kb_dir}")

        # 4. Generate Q&A pairs (optional, API cost)
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

            # Process in batches to show progress
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

            # Write Q&A files
            with open(qa_dir / "all_qa_pairs.jsonl", "w", encoding="utf-8") as f:
                for qa in all_qa:
                    f.write(json.dumps(qa, ensure_ascii=False) + "\n")
            for subtopic, qas in qa_by_subtopic.items():
                with open(qa_dir / f"{subtopic}_qa.jsonl", "w", encoding="utf-8") as f:
                    for qa in qas:
                        f.write(json.dumps(qa, ensure_ascii=False) + "\n")
            logger.info(f"Q&A pairs written: {len(all_qa)} total")
        else:
            logger.info("Skipping Q&A generation (local mode). Use --mode hybrid to enable.")

        # 5. Build Fine-Tuning datasets
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
            # If no Q&A, write a dataset from raw chunks (useful for pre-training / embeddings)
            logger.info("No Q&A generated; writing raw chunk datasets for embedding fine-tuning...")
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

        # 6. Write manifest summary
        summary = {
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "input_dir": self.cfg.input_dir,
            "total_chunks": len(chunks),
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
        logger.info(f"  KB articles : {len(subtopic_chunks)}")
        logger.info(f"  Q&A pairs   : {len(all_qa)}")
        logger.info(f"  Output dir  : {self.out_dir}")
        logger.info("=" * 60)


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Knowledge-Base Builder for Crawled Data")
    parser.add_argument("--input", default="./kb_output", help="Crawler output directory")
    parser.add_argument("--output", default="./pipeline_out", help="Pipeline output directory")
    parser.add_argument("--mode", choices=["local", "hybrid", "llm"], default="local",
                        help="local=zero API cost; hybrid=local routing + LLM Q&A; llm=LLM for everything")
    parser.add_argument("--llm-base", default="https://api.deepseek.com", help="LLM base URL")
    parser.add_argument("--llm-key", default=os.environ.get("LLM_API_KEY", ""), help="LLM API key")
    parser.add_argument("--llm-model", default="deepseek-chat", help="LLM model name")
    parser.add_argument("--qa-per-chunk", type=int, default=2, help="Q&A pairs to generate per chunk")
    parser.add_argument("--qa-concurrency", type=int, default=8, help="Concurrent LLM calls")
    args = parser.parse_args()

    cfg = Config(
        input_dir=args.input,
        output_dir=args.output,
        mode=args.mode,
        llm_base_url=args.llm_base,
        llm_api_key=args.llm_key,
        qa_model=args.llm_model,
        qa_per_chunk=args.qa_per_chunk,
        qa_concurrency=args.qa_concurrency,
    )

    p = Pipeline(cfg)
    asyncio.run(p.run())


if __name__ == "__main__":
    main()