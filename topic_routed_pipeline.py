"""
Topic-Routed Knowledge Distillation Pipeline
=============================================
Extends the base pipeline with hierarchical topic classification.
Routes chunks to topic-specific distillation streams, producing
partitioned JSON outputs per subtopic instead of one monolithic file.

Designed for large OpenID/eIDAS datasets (600+ files, 1M+ lines).

Usage:
    python topic_routed_pipeline.py
"""

import json
import logging
import os
import re
import asyncio
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass, field, asdict
from collections import defaultdict
import time

import torch
import numpy as np
from transformers import pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from sklearn.metrics.pairwise import cosine_similarity
from openai import AsyncOpenAI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s"
)
logger = logging.getLogger("TopicPipeline")


# =============================================================================
# TOPIC TAXONOMY
# =============================================================================

@dataclass
class TopicConfig:
    """Defines the topic taxonomy and routing rules."""

    # Hierarchical topics: parent -> list of children
    # A chunk can match multiple leaf topics
    taxonomy: Dict[str, List[str]] = field(default_factory=lambda: {
        "protocol_flows": [
            "authorization_code_flow",
            "credential_offer_flow", 
            "presentation_exchange_flow",
            "token_endpoint_flow",
            "par_flow",
            "wallet_activation_flow"
        ],
        "cryptography_security": [
            "digital_signatures",
            "key_management",
            "sd_jwt_selective_disclosure",
            "encryption_jwe",
            "hashing_integrity",
            "post_quantum_crypto"
        ],
        "data_schemas_formats": [
            "jwt_claims_structure",
            "mdoc_cbor_encoding",
            "json_schema_definitions",
            "credential_metadata",
            "authorization_details"
        ],
        "trust_framework_compliance": [
            "eidas_trust_framework",
            "qualified_electronic_signature",
            "attestation_mechanisms",
            "certification_conformance",
            "pid_provider_requirements"
        ],
        "implementation_api": [
            "rest_endpoints",
            "error_handling",
            "http_methods_status_codes",
            "implementation_examples",
            "sdk_library_usage"
        ],
        "architecture_concepts": [
            "wallet_architecture",
            "issuer_verifier_roles",
            "relying_party_interactions",
            "ecosystem_interoperability",
            "reference_framework_arf"
        ],
        "regulatory_legal": [
            "psd2_payment_services",
            "gdpr_data_protection",
            "legal_obligations",
            "directive_regulation_text"
        ]
    })

    # Thresholds
    min_topic_score: float = 0.55
    max_topics_per_chunk: int = 3
    enable_multi_label: bool = True

    # Topic-specific prompt suffixes (injected into system prompt)
    topic_prompts: Dict[str, str] = field(default_factory=lambda: {
        "protocol_flows": "Focus on sequence diagrams, message exchanges, state transitions, and protocol step ordering.",
        "cryptography_security": "Focus on algorithm specifications, key formats, signature schemes, and security requirements.",
        "data_schemas_formats": "Focus on field names, data types, required vs optional fields, and encoding rules.",
        "trust_framework_compliance": "Focus on trust levels, qualified status, attestation requirements, and compliance checks.",
        "implementation_api": "Focus on endpoint URLs, HTTP methods, request/response payloads, and error codes.",
        "architecture_concepts": "Focus on role definitions, component interactions, and system boundaries.",
        "regulatory_legal": "Focus on legal obligations, directive articles, and regulatory requirements."
    })


# =============================================================================
# HIERARCHICAL TOPIC CLASSIFIER
# =============================================================================

class HierarchicalTopicClassifier:
    """
    Two-stage classifier:
    1. Broad domain classification (parent topics)
    2. Fine-grained subtopic classification (leaf topics)

    Uses lightweight local models. Zero API cost.
    """

    def __init__(self, config: TopicConfig, device: str = "auto"):
        self.config = config
        self.device = self._resolve_device(device)

        # Stage 1: Broad domain classifier (fast, lightweight)
        logger.info("Loading domain classifier...")
        self.domain_classifier = pipeline(
            "zero-shot-classification",
            model="cross-encoder/nli-deberta-v3-small",
            device=self.device
        )
        self.domain_labels = list(config.taxonomy.keys())

        # Stage 2: Subtopic classifiers (one per domain, lazy-loaded)
        self.subtopic_classifiers: Dict[str, Any] = {}
        self._load_all_subtopic_classifiers()

        # Keyword-based pre-scoring for speed
        self.topic_keywords = self._build_keyword_index()

    def _resolve_device(self, device: str) -> int:
        if device == "auto":
            if torch.cuda.is_available():
                return 0
            return -1
        return device

    def _load_all_subtopic_classifiers(self):
        """Load subtopic classifiers for all domains."""
        for domain, subtopics in self.config.taxonomy.items():
            if not subtopics:
                continue
            logger.info(f"Loading subtopic classifier for {domain} ({len(subtopics)} topics)...")
            self.subtopic_classifiers[domain] = pipeline(
                "zero-shot-classification",
                model="cross-encoder/nli-deberta-v3-small",
                device=self.device
            )

    def _build_keyword_index(self) -> Dict[str, List[str]]:
        """Build keyword index for fast pre-filtering."""
        keywords = {
            "protocol_flows": [
                "flow", "sequence", "step", "request", "response", "exchange",
                "redirect", "callback", "authorize", "token endpoint", "credential offer",
                "presentation", "issuance", "par", "pushed authorization"
            ],
            "cryptography_security": [
                "signature", "sign", "verify", "key", "private", "public",
                "sd-jwt", "selective disclosure", "hash", "digest", "encrypt",
                "decrypt", "jwk", "jws", "jwe", "ecdsa", "eddsa", "rsa",
                "certificate", "pki", "post-quantum", "quantum-resistant"
            ],
            "data_schemas_formats": [
                "schema", "field", "property", "attribute", "claim",
                "json", "cbor", "mdoc", "credential", "metadata",
                "type", "format", "encoding", "structure", "array", "object",
                "authorization_details", "credential_definition"
            ],
            "trust_framework_compliance": [
                "trust", "qualified", "eidas", "attestation", "certificate",
                "conformance", "compliance", "certification", "accreditation",
                "pid", "person identification", "wallet provider", "trust anchor"
            ],
            "implementation_api": [
                "endpoint", "api", "http", "post", "get", "url", "path",
                "status code", "error", "response code", "implementation",
                "example", "sdk", "library", "client", "server"
            ],
            "architecture_concepts": [
                "architecture", "component", "role", "actor", "wallet",
                "issuer", "verifier", "holder", "relying party", "ecosystem",
                "interoperability", "framework", "reference", "arf"
            ],
            "regulatory_legal": [
                "regulation", "directive", "legal", "law", "article",
                "psd2", "gdpr", "obligation", "requirement", "shall", "must",
                "compliance", "legislation", "jurisdiction"
            ]
        }
        return keywords

    def classify(self, chunk_text: str, chunk_heading: str = "") -> List[Tuple[str, float]]:
        """
        Classify chunk into topics. Returns list of (topic, score) tuples.
        """
        preview = (chunk_heading + " " + chunk_text)[:2500].lower()

        # Fast keyword pre-filtering
        keyword_scores = self._keyword_score(preview)

        # Stage 1: Domain classification
        domain_results = self._classify_domains(preview)

        # Stage 2: Subtopic classification for high-scoring domains
        all_topics = []
        for domain, domain_score in domain_results:
            if domain_score < self.config.min_topic_score * 0.7:
                continue

            subtopics = self.config.taxonomy.get(domain, [])
            if not subtopics:
                all_topics.append((domain, domain_score))
                continue

            sub_results = self._classify_subtopics(preview, domain, subtopics)
            for subtopic, sub_score in sub_results:
                # Blend domain and subtopic scores
                blended = (domain_score * 0.4) + (sub_score * 0.6)
                if blended >= self.config.min_topic_score:
                    all_topics.append((subtopic, blended))

        # If no topics matched, fall back to keyword-only best match
        if not all_topics and keyword_scores:
            best = max(keyword_scores.items(), key=lambda x: x[1])
            if best[1] > 0.3:
                all_topics.append((best[0], best[1]))

        # Sort by score, take top N
        all_topics.sort(key=lambda x: x[1], reverse=True)

        if self.config.enable_multi_label:
            return all_topics[:self.config.max_topics_per_chunk]
        else:
            return [all_topics[0]] if all_topics else [("general", 0.5)]

    def _keyword_score(self, text: str) -> Dict[str, float]:
        """Fast keyword-based scoring."""
        scores = {}
        for topic, keywords in self.topic_keywords.items():
            matches = sum(1 for kw in keywords if kw in text)
            if matches > 0:
                scores[topic] = min(matches * 0.15, 0.8)
        return scores

    def _classify_domains(self, text: str) -> List[Tuple[str, float]]:
        """Classify into broad domains."""
        try:
            result = self.domain_classifier(
                text[:2000],
                self.domain_labels,
                hypothesis_template="This text is about {}."
            )
            return list(zip(result["labels"], result["scores"]))
        except Exception as e:
            logger.warning(f"Domain classification failed: {e}")
            return []

    def _classify_subtopics(self, text: str, domain: str, 
                            subtopics: List[str]) -> List[Tuple[str, float]]:
        """Classify into subtopics within a domain."""
        classifier = self.subtopic_classifiers.get(domain)
        if not classifier:
            return []

        try:
            result = classifier(
                text[:2000],
                subtopics,
                hypothesis_template="This text specifically discusses {}."
            )
            return list(zip(result["labels"], result["scores"]))
        except Exception as e:
            logger.warning(f"Subtopic classification failed for {domain}: {e}")
            return []


# =============================================================================
# TOPIC-ROUTED DISTILLER
# =============================================================================

class TopicRoutedDistiller:
    """
    Distills Q&A pairs with topic-specific prompts.
    Writes output to separate JSONL files per topic.
    """

    def __init__(self, config: TopicConfig, llm_config: Dict[str, Any]):
        self.config = config
        self.llm_config = llm_config
        self.client = AsyncOpenAI(
            api_key=llm_config.get("api_key", os.environ.get("DEEPSEEK_API_KEY", "")),
            base_url=llm_config.get("base_url", "https://api.deepseek.com")
        )
        self.semaphore = asyncio.Semaphore(llm_config.get("concurrent_requests", 8))

        # Base system prompt
        self.base_prompt = (
            "You are an expert technical documentation extractor specializing in "
            "European digital identity, eIDAS 2.0, OpenID4VCI, OpenID4VP, and SD-JWT VC standards.\n\n"
            "EXTRACTION RULES:\n"
            "1. Focus ONLY on: protocol flows, cryptographic requirements, trust framework rules, "
            "   API endpoints, data schemas, compliance obligations, and implementation guidelines.\n"
            "2. IGNORE: Version history, contributor lists, formatting artifacts, TOC entries, "
            "   and purely narrative text without technical substance.\n"
            "3. If the chunk contains NO extractable technical knowledge, output an empty qa_pairs array.\n"
            "4. NEVER invent information not present in the text. If uncertain, prefer omission.\n"
            "5. Prompts should be specific, self-contained questions that a developer might ask.\n"
            "6. Responses must be technically precise and cite specific mechanisms.\n"
            "7. Prefer comprehensive responses with specific details over high-level summaries.\n"
            "8. Include concrete examples, field names, and protocol steps when present in text.\n\n"
            "OUTPUT FORMAT:\n"
            "Strict JSON with a single key 'qa_pairs' containing an array of objects. "
            "Each object has 'prompt' (string) and 'response' (string). "
            "Maximum 5 Q&A pairs per chunk. Prioritize quality over quantity."
        )

        self.few_shot = """
Example 1 (Protocol Flow):
Text: "The Wallet Unit MUST validate that the `iss` claim matches the trusted issuer URL before processing the credential offer."
Output: {"qa_pairs": [{"prompt": "What validation must a Wallet Unit perform on the `iss` claim in an OpenID4VCI issuance response?", "response": "The Wallet Unit MUST validate that the `iss` claim matches the trusted issuer URL before processing the credential offer."}]}

Example 2 (Cryptography):
Text: "The SD-JWT VC MUST be signed using ECDSA with curve P-256 as defined in FIPS 186-5."
Output: {"qa_pairs": [{"prompt": "What signature algorithm and curve must be used for SD-JWT VC signing?", "response": "The SD-JWT VC MUST be signed using ECDSA with curve P-256 as defined in FIPS 186-5."}]}

Example 3 (Data Schema):
Text: "The `authorization_details` parameter is a JSON array containing objects with `type` and `locations` fields."
Output: {"qa_pairs": [{"prompt": "What is the structure of the `authorization_details` parameter in OpenID4VCI?", "response": "The `authorization_details` parameter is a JSON array containing objects with `type` and `locations` fields."}]}

Example 4 (Boilerplate):
Text: "Table of Contents: 1. Introduction 2. Scope 3. References"
Output: {"qa_pairs": []}
"""

        # Track seen Q&A pairs for cross-topic deduplication
        self.seen_hashes: Set[str] = set()

    def _get_topic_prompt(self, topics: List[str]) -> str:
        """Build topic-specific prompt suffix."""
        if not topics:
            return ""

        # Use the highest-scoring topic's specific guidance
        primary_topic = topics[0]

        # Map subtopic back to domain for prompt lookup
        domain = None
        for d, subs in self.config.taxonomy.items():
            if primary_topic in subs or primary_topic == d:
                domain = d
                break

        if domain and domain in self.config.topic_prompts:
            return "\n\nTOPIC FOCUS:\n" + self.config.topic_prompts[domain]
        return ""

    def _hash_qa(self, prompt: str, response: str) -> str:
        """Hash for deduplication."""
        normalized = (prompt.lower().strip() + "|||" + response.lower().strip()[:200])
        return hashlib.md5(normalized.encode()).hexdigest()

    async def distill(self, chunk_text: str, chunk_id: str, topics: List[str],
                      source_file: str, chunk_index: int) -> Dict[str, List[Dict]]:
        """
        Distill Q&A for a chunk. Returns dict mapping topic -> list of Q&A pairs.
        """
        topic_prompt = self._get_topic_prompt(topics)
        system_prompt = self.base_prompt + topic_prompt

        async with self.semaphore:
            try:
                response = await self.client.chat.completions.create(
                    model=self.llm_config.get("model", "deepseek-chat"),
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"{self.few_shot}\n\nExtract from this text:\n\n{chunk_text}"}
                    ],
                    response_format={"type": "json_object"},
                    temperature=self.llm_config.get("temperature", 0.1),
                    max_tokens=self.llm_config.get("max_tokens", 4096)
                )

                content = response.choices[0].message.content
                parsed = json.loads(content)
                qa_pairs = parsed.get("qa_pairs", [])

                # Distribute to topics
                topic_results: Dict[str, List[Dict]] = defaultdict(list)

                for qa in qa_pairs:
                    prompt = qa.get("prompt", "").strip()
                    resp = qa.get("response", "").strip()

                    if not prompt or not resp:
                        continue

                    # Cross-topic deduplication
                    qa_hash = self._hash_qa(prompt, resp)
                    if qa_hash in self.seen_hashes:
                        continue
                    self.seen_hashes.add(qa_hash)

                    record = {
                        "prompt": prompt,
                        "response": resp,
                        "source_id": chunk_id,
                        "source_file": source_file,
                        "chunk_index": chunk_index,
                        "topics": topics,
                        "quality_score": 0.0
                    }

                    # Assign to all matched topics (multi-label)
                    if self.config.enable_multi_label:
                        for topic, _ in topics:
                            topic_results[topic].append(record)
                    else:
                        topic_results[topics[0][0]].append(record)

                return dict(topic_results)

            except Exception as e:
                logger.error(f"Distillation failed for {chunk_id}: {e}")
                return {}


# =============================================================================
# PARTITIONED STORAGE
# =============================================================================

class PartitionedStorage:
    """Writes Q&A pairs to separate files per topic."""

    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Open file handles per topic
        self.handles: Dict[str, Any] = {}
        self.counters: Dict[str, int] = defaultdict(int)

    def _get_handle(self, topic: str):
        if topic not in self.handles:
            safe_topic = re.sub(r'[^\w_-]', '_', topic)
            path = self.output_dir / f"distilled_{safe_topic}.jsonl"
            self.handles[topic] = open(path, 'w', encoding='utf-8')
            logger.info(f"Opened output: {path}")
        return self.handles[topic]

    def write(self, topic: str, records: List[Dict]):
        if not records:
            return
        handle = self._get_handle(topic)
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            self.counters[topic] += 1
        handle.flush()

    def close(self):
        for topic, handle in self.handles.items():
            handle.close()
            logger.info(f"Topic '{topic}': {self.counters[topic]} records written")

    def get_summary(self) -> Dict[str, int]:
        return dict(self.counters)


# =============================================================================
# ORCHESTRATOR
# =============================================================================

class TopicRoutedPipeline:
    """Full pipeline with topic routing."""

    def __init__(self, 
                 input_dir: str = "./data_lake/crawled/extracted",
                 output_dir: str = "./pipeline_output/topics",
                 topic_config: Optional[TopicConfig] = None,
                 llm_config: Optional[Dict] = None):
        self.input_dir = Path(input_dir)
        self.output_dir = output_dir
        self.topic_config = topic_config or TopicConfig()
        self.llm_config = llm_config or {
            "api_key": os.environ.get("DEEPSEEK_API_KEY", ""),
            "base_url": "https://api.deepseek.com",
            "model": "deepseek-chat",
            "concurrent_requests": 8,
            "temperature": 0.1,
            "max_tokens": 4096
        }

        self.classifier = HierarchicalTopicClassifier(self.topic_config)
        self.distiller = TopicRoutedDistiller(self.topic_config, self.llm_config)
        self.storage = PartitionedStorage(output_dir)

    def _load_chunks(self) -> List[Dict[str, Any]]:
        """Load all .md files from input directory."""
        chunks = []
        md_files = list(self.input_dir.rglob("*.md"))
        logger.info(f"Found {len(md_files)} markdown files")

        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Parse YAML frontmatter if present
                frontmatter = {}
                body = content
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        try:
                            frontmatter = json.loads(parts[1].strip())
                        except:
                            pass
                        body = parts[2].strip()

                # Simple chunking: split by headers for now
                # In production, use SmartChunker from previous pipeline
                sections = self._split_by_headers(body, str(md_file))

                for i, section in enumerate(sections):
                    if len(section["text"]) < 200:
                        continue
                    chunks.append({
                        "id": f"{md_file.stem}_sec_{i}",
                        "source_file": str(md_file.relative_to(self.input_dir)),
                        "content": section["text"],
                        "heading": section["heading"],
                        "metadata": frontmatter
                    })

            except Exception as e:
                logger.warning(f"Failed to load {md_file}: {e}")

        logger.info(f"Loaded {len(chunks)} chunks")
        return chunks

    def _split_by_headers(self, text: str, source: str) -> List[Dict]:
        """Split text by markdown headers."""
        pattern = re.compile(r'^(#{1,3}\s+.+)$', re.MULTILINE)
        matches = list(pattern.finditer(text))

        if not matches:
            return [{"heading": "", "text": text}]

        sections = []
        for i, match in enumerate(matches):
            start = match.start()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            section_text = text[start:end].strip()
            heading = match.group(1).strip()
            sections.append({"heading": heading, "text": section_text})

        return sections

    async def run(self):
        logger.info("=" * 60)
        logger.info("Topic-Routed Pipeline Starting")
        logger.info("=" * 60)

        # Load chunks
        chunks = self._load_chunks()

        # Classify all chunks
        logger.info("Classifying chunks into topics...")
        classified_chunks = []
        for chunk in chunks:
            topics = self.classifier.classify(chunk["content"], chunk["heading"])
            chunk["topics"] = topics
            classified_chunks.append(chunk)

        # Log topic distribution
        topic_counts = defaultdict(int)
        for chunk in classified_chunks:
            for topic, score in chunk["topics"]:
                topic_counts[topic] += 1
        logger.info("Topic distribution:")
        for topic, count in sorted(topic_counts.items(), key=lambda x: -x[1]):
            logger.info(f"  {topic}: {count} chunks")

        # Distill in batches
        logger.info("Starting distillation...")
        batch_size = self.llm_config.get("concurrent_requests", 8)

        for i in range(0, len(classified_chunks), batch_size):
            batch = classified_chunks[i:i + batch_size]
            tasks = [
                self.distiller.distill(
                    chunk["content"],
                    chunk["id"],
                    chunk["topics"],
                    chunk["source_file"],
                    0  # chunk_index
                )
                for chunk in batch
            ]

            results = await asyncio.gather(*tasks, return_exceptions=True)

            for result in results:
                if isinstance(result, dict):
                    for topic, records in result.items():
                        self.storage.write(topic, records)

            if (i // batch_size) % 5 == 0:
                logger.info(f"Progress: {i}/{len(classified_chunks)} chunks processed")

        self.storage.close()

        # Summary
        summary = self.storage.get_summary()
        total = sum(summary.values())
        logger.info("=" * 60)
        logger.info(f"Complete! {total} total Q&A pairs across {len(summary)} topics")
        for topic, count in sorted(summary.items(), key=lambda x: -x[1]):
            logger.info(f"  {topic}: {count}")
        logger.info("=" * 60)


# =============================================================================
# MAIN
# =============================================================================

def main():
    import dotenv
    dotenv.load_dotenv()

    pipeline = TopicRoutedPipeline(
        input_dir="./data_lake/crawled/extracted",
        output_dir="./pipeline_output/topics",
        topic_config=TopicConfig(
            min_topic_score=0.50,
            max_topics_per_chunk=2,
            enable_multi_label=True
        ),
        llm_config={
            "api_key": os.environ.get("DEEPSEEK_API_KEY", ""),
            "model": "deepseek-chat",
            "concurrent_requests": 8,
            "temperature": 0.1,
            "max_tokens": 4096
        }
    )

    asyncio.run(pipeline.run())


if __name__ == "__main__":
    main()
