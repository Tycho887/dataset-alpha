"""
EU Digital Software Knowledge Distillation Pipeline
====================================================
Modular, drag-and-drop pipeline for processing technical documentation
into structured prompt/response pairs for RAG fine-tuning.

Each stage is self-contained and can be enabled/disabled via config.
"""

import json
import logging
import os
import re
import asyncio
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field, asdict
from collections import defaultdict
import dotenv

import torch
import numpy as np
from transformers import pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from sklearn.metrics.pairwise import cosine_similarity
from openai import AsyncOpenAI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s"
)
logger = logging.getLogger("Pipeline")

# =============================================================================
# CONFIGURATION
# =============================================================================

@dataclass
class PipelineConfig:
    """Central configuration for all pipeline stages."""
    
    # Paths
    target_dir: str = "./data_lake"
    output_dir: str = "./pipeline_output"
    
    # Stage toggles (drag-and-drop control)
    enable_heuristic_filter: bool = True
    enable_zero_shot_filter: bool = True
    enable_data_cleaning: bool = True
    enable_smart_chunking: bool = True
    enable_deduplication: bool = True
    enable_importance_scoring: bool = True
    enable_dual_processing: bool = True
    enable_quality_filter: bool = True
    
    # Heuristic filter settings
    max_file_size_mb: float = 5.0
    ignored_extensions: set = field(default_factory=lambda: {
        ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
        ".lock", ".pyc", ".pyo", ".git", ".exe", ".bin",
        ".zip", ".tar", ".gz", ".rar", ".7z",
        ".mp4", ".mp3", ".wav", ".avi", ".mov",
        ".ttf", ".woff", ".woff2", ".eot"
    })
    ignored_names: set = field(default_factory=lambda: {
        "package-lock.json", ".gitignore", "yarn.lock", "pnpm-lock.yaml",
        "LICENSE", "LICENSE.md", "CHANGELOG.md", "CONTRIBUTORS.md"
    })
    
    # Zero-shot classifier settings
    classifier_model: str = "cross-encoder/nli-deberta-v3-base"
    classifier_labels: List[str] = field(default_factory=lambda: [
        "EU regulations and technical framework",
        "irrelevant boilerplate or noise"
    ])
    classifier_threshold: float = 0.70
    classifier_preview_chars: int = 2000
    
    # Data cleaning settings
    remove_markdown_toc: bool = True
    remove_license_headers: bool = True
    normalize_whitespace: bool = True
    extract_code_blocks: bool = True
    min_content_length: int = 100
    
    # Chunking settings
    embedder_model: str = "BAAI/bge-base-en-v1.5"
    chunk_size_target: int = 1500
    chunk_overlap: int = 150
    semantic_threshold_percentile: int = 95
    preserve_headings: bool = True
    
    # Deduplication settings
    dedup_threshold: float = 0.92
    min_chunk_length: int = 50
    
    # Importance scoring settings
    importance_model: str = "cross-encoder/nli-deberta-v3-small"
    importance_threshold: float = 0.65
    high_value_keywords: List[str] = field(default_factory=lambda: [
        "MUST", "REQUIRED", "SHALL", "MANDATORY",
        "cryptographic", "signature", "verification",
        "trust framework", "eIDAS", "qualified",
        "endpoint", "schema", "protocol", "flow",
        "authorization_details", "credential_offer",
        "SD-JWT", "presentation", "issuance"
    ])
    
    # Dual processing settings
    group_size: int = 3
    group_overlap: int = 1
    
    # LLM settings
    llm_api_key: str = ""
    llm_base_url: str = "https://api.deepseek.com"
    llm_model: str = "deepseek-chat"
    llm_concurrent_requests: int = 8
    llm_temperature: float = 0.1
    llm_max_tokens: int = 4096
    
    # Quality filter settings
    min_response_length: int = 80
    max_response_length: int = 3000
    required_question_words: List[str] = field(default_factory=lambda: [
        "what", "how", "why", "when", "where", "which", "who",
        "explain", "describe", "detail", "list", "compare",
        "what is", "how does", "why is", "when should"
    ])
    
    # Knowledge synthesis settings
    enable_knowledge_synthesis: bool = True
    knowledge_cluster_threshold: float = 0.82
    max_knowledge_block_tokens: int = 3000
    max_excerpts_per_block: int = 8


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class DocumentChunk:
    """Represents a processed chunk with full metadata."""
    id: str
    source_file: str
    content: str
    chunk_index: int = 0
    chunk_length: int = 0
    heading_path: List[str] = field(default_factory=list)
    doc_type: str = "unknown"
    language: str = "en"
    importance_score: float = 0.0
    is_important: bool = False
    processing_mode: str = "standard"  # "standard" or "dual"
    group_id: Optional[str] = None
    code_blocks: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    metadata: Dict[str, Any] = field(default_factory=dict)
    source_url: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class QAPair:
    """Represents a generated prompt/response pair."""
    prompt: str
    response: str
    source_id: str
    source_file: str
    chunk_index: int
    processing_mode: str
    group_id: Optional[str]
    quality_score: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class KnowledgeBlock:
    """A synthesized, non-repetitive topic block with source provenance."""
    block_id: str
    topic: str
    synthesized_text: str
    source_chunks: List[str] = field(default_factory=list)
    sources: List[Dict[str, str]] = field(default_factory=list)
    word_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

# =============================================================================
# STAGE 1: FILE LOADER
# =============================================================================

class FileLoader:
    """Discovers and loads raw text from files."""
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.target_dir = Path(config.target_dir)
        
    def load(self) -> List[Dict[str, Any]]:
        """Discover all files and extract raw text."""
        documents = []
        
        if not self.target_dir.exists():
            logger.error(f"Target directory not found: {self.target_dir}")
            return documents
            
        for file_path in self.target_dir.rglob("*"):
            if not file_path.is_file():
                continue
                
            # Quick size check before reading
            if file_path.stat().st_size > self.config.max_file_size_mb * 1024 * 1024:
                logger.warning(f"Skipping large file: {file_path.name}")
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            except Exception as e:
                logger.debug(f"Cannot read {file_path}: {e}")
                continue
                
            if not content.strip():
                continue
    
                # Attempt to recover original URL from crawler meta.json
            source_url = ""
            meta_path = file_path.parent / "meta.json"
            if meta_path.exists():
                try:
                    meta = json.loads(meta_path.read_text(encoding='utf-8'))
                    source_url = meta.get("url", "")
                except Exception:
                    pass
    
            doc = {
                "id": f"doc_{hashlib.md5(str(file_path).encode()).hexdigest()[:8]}",
                "file_path": str(file_path),
                "relative_path": str(file_path.relative_to(self.target_dir)),
                "content": content,
                "size": len(content),
                "source_url": source_url,
            }
            documents.append(doc)
            
        logger.info(f"Loaded {len(documents)} documents from {self.target_dir}")
        return documents


# =============================================================================
# STAGE 2: HEURISTIC PRE-FILTER
# =============================================================================

class HeuristicFilter:
    """Fast rule-based filtering to drop obvious noise."""
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        
    def filter(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Apply heuristic rules to filter documents."""
        if not self.config.enable_heuristic_filter:
            return documents
            
        filtered = []
        dropped_count = 0
        
        for doc in documents:
            path = Path(doc["file_path"])
            
            # Check extension
            if path.suffix.lower() in self.config.ignored_extensions:
                dropped_count += 1
                continue
                
            # Check filename
            if path.name in self.config.ignored_names:
                dropped_count += 1
                continue
                
            # Check content length
            if len(doc["content"].strip()) < self.config.min_content_length:
                dropped_count += 1
                continue
                
            filtered.append(doc)
            
        logger.info(f"Heuristic filter: {len(filtered)} passed, {dropped_count} dropped")
        return filtered


# =============================================================================
# STAGE 3: ZERO-SHOT RELEVANCE FILTER
# =============================================================================

class ZeroShotFilter:
    """ML-based relevance classification using cross-encoder."""
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.device = self._get_device()
        
        if self.config.enable_zero_shot_filter:
            logger.info(f"Loading classifier: {config.classifier_model}")
            # self.classifier = pipeline(
            #     "zero-shot-classification",
            #     model=config.classifier_model,
            #     device=self.device
            # )
            self.classifier = pipeline(
                "zero-shot-classification",
                model=config.classifier_model,
                device=self.device,
                batch_size=16,  # internal GPU batching
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            )
            
    def _get_device(self) -> int:
        """Determine optimal compute device."""
        if torch.cuda.is_available():
            return 0
        elif torch.backends.mps.is_available():
            return -1  # MPS handled by device mapping
        return -1

    def filter(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Classify documents and filter by relevance."""
        if not self.config.enable_zero_shot_filter:
            return documents

        # Build batch
        previews = [
            doc["content"][:self.config.classifier_preview_chars]
            for doc in documents
        ]

        try:
            results = self.classifier(
                previews,
                self.config.classifier_labels,
                hypothesis_template="This text is about {}."
            )
        except Exception as e:
            logger.error(f"Batch zero-shot classification failed: {e}")
            # Conservative fallback: keep everything
            return documents

        filtered = []
        for doc, result in zip(documents, results):
            top_label = result['labels'][0]
            top_score = result['scores'][0]

            if (top_label == self.config.classifier_labels[0] and 
                top_score > self.config.classifier_threshold):
                doc["relevance_score"] = top_score
                filtered.append(doc)
            else:
                logger.debug(
                    f"Dropped {doc['relative_path']}: {top_label} ({top_score:.2f})"
                )

        logger.info(f"Zero-shot filter: {len(filtered)}/{len(documents)} relevant")
        return filtered
        
    # def filter(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    #     """Classify documents and filter by relevance."""
    #     if not self.config.enable_zero_shot_filter:
    #         return documents
            
    #     filtered = []
        
    #     for doc in documents:
    #         preview = doc["content"][:self.config.classifier_preview_chars]
            
    #         try:
    #             result = self.classifier(
    #                 preview,
    #                 self.config.classifier_labels,
    #                 hypothesis_template="This text is about {}."
    #             )
                
    #             top_label = result['labels'][0]
    #             top_score = result['scores'][0]
                
    #             if (top_label == self.config.classifier_labels[0] and 
    #                 top_score > self.config.classifier_threshold):
    #                 doc["relevance_score"] = top_score
    #                 filtered.append(doc)
    #             else:
    #                 logger.debug(f"Dropped {doc['relative_path']}: {top_label} ({top_score:.2f})")
                    
    #         except Exception as e:
    #             logger.error(f"Classification failed for {doc['relative_path']}: {e}")
    #             # Conservative: keep on failure
    #             filtered.append(doc)
                
    #     logger.info(f"Zero-shot filter: {len(filtered)}/{len(documents)} relevant")
    #     return filtered


# =============================================================================
# STAGE 4: DATA CLEANING
# =============================================================================

class DataCleaner:
    """
    Cleans and normalizes document content before chunking.
    Extracts structured metadata, removes boilerplate, normalizes formatting.
    """
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        
        # Pre-compile regex patterns
        self._toc_pattern = re.compile(r'^\s*#{1,6}\s*Table of Contents.*?(?=^\s*#{1,6}\s)', re.MULTILINE | re.DOTALL | re.IGNORECASE)
        self._license_pattern = re.compile(r'^(?:#+\s*)?License.*?(?=^#{1,6}\s|\Z)', re.MULTILINE | re.DOTALL | re.IGNORECASE)
        self._header_pattern = re.compile(r'^#{1,6}\s*(.+)$', re.MULTILINE)
        self._code_fence_pattern = re.compile(r'```[\w]*\n(.*?)```', re.DOTALL)
        self._whitespace_pattern = re.compile(r'\n{3,}')
        self._bom_pattern = re.compile(r'^\ufeff')
        
    def clean(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Apply cleaning operations to documents."""
        if not self.config.enable_data_cleaning:
            return documents
            
        cleaned = []
        
        for doc in documents:
            content = doc["content"]
            
            # Remove BOM
            content = self._bom_pattern.sub('', content)
            
            # Extract code blocks before cleaning
            code_blocks = []
            if self.config.extract_code_blocks:
                code_blocks = self._extract_code_blocks(content)
                doc["extracted_code_blocks"] = code_blocks
            
            # Remove markdown TOC
            if self.config.remove_markdown_toc:
                content = self._toc_pattern.sub('', content)
                
            # Remove license headers
            if self.config.remove_license_headers:
                content = self._license_pattern.sub('', content)
                
            # Extract heading hierarchy
            headings = self._extract_headings(content)
            doc["heading_path"] = headings
            
            # Detect document type
            doc["doc_type"] = self._detect_doc_type(content, doc["relative_path"])
            
            # Normalize whitespace
            if self.config.normalize_whitespace:
                content = self._whitespace_pattern.sub('\n\n', content)
                content = content.strip()
                
            # Final length check
            if len(content) < self.config.min_content_length:
                logger.debug(f"Too short after cleaning: {doc['relative_path']}")
                continue
                
            doc["content"] = content
            doc["cleaned_length"] = len(content)
            cleaned.append(doc)
            
        logger.info(f"Data cleaning: {len(cleaned)} documents retained")
        return cleaned
        
    def _extract_code_blocks(self, content: str) -> List[str]:
        """Extract fenced code blocks for separate processing."""
        blocks = []
        for match in self._code_fence_pattern.finditer(content):
            blocks.append(match.group(1).strip())
        return blocks
        
    def _extract_headings(self, content: str) -> List[str]:
        """Extract document heading hierarchy."""
        headings = []
        for match in self._header_pattern.finditer(content):
            level = match.group(0).count('#')
            text = match.group(1).strip()
            headings.append({"level": level, "text": text})
        return headings
        
    def _detect_doc_type(self, content: str, path: str) -> str:
        """Heuristic document type detection."""
        path_lower = path.lower()
        content_lower = content[:2000].lower()
        
        if any(x in path_lower for x in ["spec", "rfc", "standard"]):
            return "specification"
        elif any(x in path_lower for x in ["readme", "guide", "tutorial"]):
            return "guide"
        elif any(x in path_lower for x in ["api", "endpoint", "swagger", "openapi"]):
            return "api_reference"
        elif "eidas" in content_lower or "regulation" in content_lower:
            return "regulatory"
        elif "openid4vci" in content_lower or "openid4vp" in content_lower:
            return "protocol_spec"
        elif "implementation" in content_lower or "example" in content_lower:
            return "implementation"
        return "general"


# =============================================================================
# STAGE 5: SMART CHUNKING + DEDUPLICATION
# =============================================================================

class SmartChunker:
    """
    Hierarchical chunking: structure-first (by headings), then semantic chunking.
    Preserves heading context in each chunk.
    """
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        
        if self.config.enable_smart_chunking:
            logger.info(f"Loading embedder: {config.embedder_model}")
            self.embedder = HuggingFaceEmbeddings(
                model_name=config.embedder_model,
                model_kwargs={"device": self._get_device_str()}
            )
            self.semantic_splitter = SemanticChunker(
                self.embedder,
                breakpoint_threshold_type="percentile",
                breakpoint_threshold_amount=config.semantic_threshold_percentile
            )
            
    def _get_device_str(self) -> str:
        if torch.cuda.is_available():
            return "cuda"
        elif torch.backends.mps.is_available():
            return "mps"
        return "cpu"
        
    def chunk(self, documents: List[Dict[str, Any]]) -> List[DocumentChunk]:
        """Split documents into intelligent chunks."""
        if not self.config.enable_smart_chunking:
            # Fallback: simple fixed-size chunks
            return self._simple_chunk(documents)
            
        all_chunks = []
        
        for doc in documents:
            # Strategy: Split by headings first, then semantic within sections
            sections = self._split_by_headings(doc["content"], doc.get("heading_path", []))
            
            chunk_idx = 0
            for section in sections:
                # If section is small enough, keep as single chunk
                if len(section["text"]) <= self.config.chunk_size_target * 1.5:
                    chunk = self._create_chunk(doc, section, chunk_idx)
                    all_chunks.append(chunk)
                    chunk_idx += 1
                else:
                    # Apply semantic chunking to large sections
                    semantic_chunks = self.semantic_splitter.split_text(section["text"])
                    for sc_text in semantic_chunks:
                        if len(sc_text) < self.config.min_chunk_length:
                            continue
                        section["text"] = sc_text
                        chunk = self._create_chunk(doc, section, chunk_idx)
                        all_chunks.append(chunk)
                        chunk_idx += 1
                        
        logger.info(f"Smart chunking: {len(all_chunks)} chunks from {len(documents)} docs")
        
        # Deduplication
        if self.config.enable_deduplication:
            all_chunks = self._deduplicate(all_chunks)
            
        return all_chunks
        
    def _split_by_headings(self, content: str, headings: List[Dict]) -> List[Dict[str, Any]]:
        """Split content by heading boundaries."""
        if not headings:
            return [{"text": content, "heading_path": [], "level": 0}]
            
        sections = []
        lines = content.split('\n')
        current_section = []
        current_heading = []
        current_level = 0
        
        for line in lines:
            heading_match = re.match(r'^(#{1,6})\s*(.+)$', line)
            
            if heading_match:
                # Save previous section
                if current_section:
                    sections.append({
                        "text": '\n'.join(current_section).strip(),
                        "heading_path": current_heading.copy(),
                        "level": current_level
                    })
                    
                # Start new section
                level = len(heading_match.group(1))
                title = heading_match.group(2).strip()
                
                # Build heading path
                current_heading = [h["text"] for h in headings if h["level"] < level] + [title]
                current_level = level
                current_section = [line]
            else:
                current_section.append(line)
                
        # Don't forget last section
        if current_section:
            sections.append({
                "text": '\n'.join(current_section).strip(),
                "heading_path": current_heading.copy(),
                "level": current_level
            })
            
        return sections if sections else [{"text": content, "heading_path": [], "level": 0}]
        
    def _create_chunk(self, doc: Dict, section: Dict, idx: int) -> DocumentChunk:
        """Create a DocumentChunk with full context."""
        heading_prefix = ""
        if self.config.preserve_headings and section.get("heading_path"):
            heading_prefix = " > ".join(section["heading_path"]) + "\n\n"
            
        content = heading_prefix + section["text"]
        
        return DocumentChunk(
            id=f"{doc['id']}_chunk_{idx}",
            source_file=doc["relative_path"],
            content=content,
            chunk_index=idx,
            chunk_length=len(content),
            heading_path=section.get("heading_path", []),
            doc_type=doc.get("doc_type", "unknown"),
            code_blocks=doc.get("extracted_code_blocks", []),
            source_url=doc.get("source_url", ""),
        )
        
    def _deduplicate(self, chunks: List[DocumentChunk]) -> List[DocumentChunk]:
        """Remove near-duplicate chunks using embeddings."""
        if len(chunks) < 2:
            return chunks
            
        logger.info("Running deduplication...")
        texts = [c.content for c in chunks]
        embeddings = self.embedder.embed_documents(texts)
        
        to_remove = set()
        for i in range(len(embeddings)):
            if i in to_remove:
                continue
            for j in range(i + 1, len(embeddings)):
                if j in to_remove:
                    continue
                sim = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
                if sim > self.config.dedup_threshold:
                    # Keep the longer one
                    if chunks[i].chunk_length >= chunks[j].chunk_length:
                        to_remove.add(j)
                    else:
                        to_remove.add(i)
                        break
                        
        result = [c for i, c in enumerate(chunks) if i not in to_remove]
        logger.info(f"Deduplication: {len(result)}/{len(chunks)} retained ({len(chunks)-len(result)} removed)")
        return result
        
    def _simple_chunk(self, documents: List[Dict[str, Any]]) -> List[DocumentChunk]:
        """Fallback simple chunking."""
        chunks = []
        for doc in documents:
            text = doc["content"]
            size = self.config.chunk_size_target
            overlap = self.config.chunk_overlap
            
            for i in range(0, len(text), size - overlap):
                segment = text[i:i + size]
                if len(segment) < self.config.min_chunk_length:
                    continue
                chunks.append(DocumentChunk(
                    id=f"{doc['id']}_chunk_{i//(size-overlap)}",
                    source_file=doc["relative_path"],
                    content=segment,
                    chunk_index=i//(size-overlap)
                ))
        return chunks


# =============================================================================
# STAGE 6: IMPORTANCE SCORING & ROUTING
# =============================================================================

class ImportanceScorer:
    """
    Scores chunks by information density and routes important ones to dual processing.
    Uses keyword density + lightweight classifier for scoring.
    """
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.keywords = [kw.lower() for kw in config.high_value_keywords]
        
        # Optional: Load a lightweight model for importance scoring
        if self.config.enable_importance_scoring and self.config.importance_model:
            try:
                # self.classifier = pipeline(
                #     "zero-shot-classification",
                #     model=config.importance_model,
                #     device=0 if torch.cuda.is_available() else -1
                # )
                self.classifier = pipeline(
                    "zero-shot-classification",
                    model=config.importance_model,
                    device=0 if torch.cuda.is_available() else -1,
                    batch_size=32,
                    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                )
                self.importance_labels = [
                    "critical technical implementation detail",
                    "general explanatory text"
                ]
            except Exception as e:
                logger.warning(f"Could not load importance model: {e}")
                self.classifier = None
        else:
            self.classifier = None
            
    def score_and_route(self, chunks: List[DocumentChunk]) -> List[DocumentChunk]:
        """Score chunks and mark important ones for dual processing."""
        if not self.config.enable_importance_scoring:
            for chunk in chunks:
                chunk.processing_mode = "standard"
            return chunks
            
        for chunk in chunks:
            score = self._calculate_score(chunk)
            chunk.importance_score = score
            chunk.is_important = score > self.config.importance_threshold
            
            if chunk.is_important and self.config.enable_dual_processing:
                chunk.processing_mode = "dual"
            else:
                chunk.processing_mode = "standard"
                
        important_count = sum(1 for c in chunks if c.is_important)
        logger.info(f"Importance scoring: {important_count}/{len(chunks)} marked as important")
        return chunks
        
    def _calculate_score(self, chunk: DocumentChunk) -> float:
        """Calculate importance score from 0-1."""
        content_lower = chunk.content.lower()
        
        # Keyword density score (0-0.5)
        keyword_hits = sum(1 for kw in self.keywords if kw in content_lower)
        keyword_score = min(keyword_hits / 5, 0.5)  # Cap at 0.5
        
        # Normative language score (0-0.3)
        normative_terms = ["must", "shall", "required", "mandatory", "shall not", "must not"]
        normative_hits = sum(1 for term in normative_terms if term in content_lower)
        normative_score = min(normative_hits / 3, 0.3)
        
        # Code block presence (0-0.1)
        code_score = 0.1 if chunk.code_blocks else 0.0
        
        # Heading depth bonus (0-0.1)
        depth_score = 0.0
        if chunk.heading_path:
            # Deeper headings often contain more specific details
            avg_depth = sum(1 for h in chunk.heading_path) / len(chunk.heading_path)
            depth_score = min(avg_depth / 10, 0.1)
            
        total = keyword_score + normative_score + code_score + depth_score
        
        # If classifier available, blend with its prediction
        if self.classifier and len(chunk.content) > 200:
            try:
                preview = chunk.content[:1500]
                result = self.classifier(
                    preview,
                    self.importance_labels,
                    hypothesis_template="This text contains {}."
                )
                if result['labels'][0] == self.importance_labels[0]:
                    classifier_score = result['scores'][0] * 0.3
                    total = total * 0.7 + classifier_score
            except Exception:
                pass
                
        return min(total, 1.0)


# =============================================================================
# STAGE 7: DUAL PROCESSING GROUPER
# =============================================================================

class DualProcessingGrouper:
    """
    Groups important chunks thematically for dual processing.
    Important chunks are processed both independently AND as part of a group.
    """
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        
    def create_groups(self, chunks: List[DocumentChunk]) -> Tuple[List[DocumentChunk], List[List[DocumentChunk]]]:
        """
        Returns:
            - solo_chunks: All chunks that need individual processing
            - groups: Lists of chunk groups for thematic processing
        """
        if not self.config.enable_dual_processing:
            return chunks, []
            
        # Separate important and standard chunks
        important = [c for c in chunks if c.processing_mode == "dual"]
        standard = [c for c in chunks if c.processing_mode == "standard"]
        
        # Group important chunks by source file and heading proximity
        groups = self._group_by_proximity(important)
        
        # All chunks get solo processing
        # Important chunks ALSO get group processing
        solo_chunks = chunks  # Everyone gets solo
        
        logger.info(f"Dual processing: {len(solo_chunks)} solo + {len(groups)} groups")
        return solo_chunks, groups
        
    def _group_by_proximity(self, chunks: List[DocumentChunk]) -> List[List[DocumentChunk]]:
        """Group chunks by source file and semantic proximity."""
        # Group by source file first
        by_file = defaultdict(list)
        for chunk in chunks:
            by_file[chunk.source_file].append(chunk)
            
        all_groups = []
        
        for file_path, file_chunks in by_file.items():
            # Sort by chunk index to maintain document order
            file_chunks.sort(key=lambda c: c.chunk_index)
            
            # Create sliding window groups
            group_size = self.config.group_size
            overlap = self.config.group_overlap
            
            for i in range(0, len(file_chunks), group_size - overlap):
                group = file_chunks[i:i + group_size]
                if len(group) >= 2:  # Only create groups of 2+
                    group_id = f"group_{hashlib.md5((file_path + str(i)).encode()).hexdigest()[:8]}"
                    for chunk in group:
                        chunk.group_id = group_id
                    all_groups.append(group)
                    
        return all_groups


# =============================================================================
# STAGE 8: ASYNC LLM DISTILLATION
# =============================================================================

class AsyncLLMDistiller:
    """
    Async distillation with concurrent API calls.
    Supports both solo and group processing modes.
    """
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.client = AsyncOpenAI(
            api_key=config.llm_api_key or os.environ.get("DEEPSEEK_API_KEY", ""),
            base_url=config.llm_base_url
        )
        self.semaphore = asyncio.Semaphore(config.llm_concurrent_requests)
        
        self.system_prompt = (
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
Example 1 (Technical Spec):
Text: "The Wallet Unit MUST validate that the `iss` claim in the JWT matches the trusted issuer URL before processing the credential offer. The validation follows RFC 7519 section 4.1.1."
Output: {"qa_pairs": [{"prompt": "What validation must a Wallet Unit perform on the `iss` claim in an OpenID4VCI issuance response?", "response": "The Wallet Unit MUST validate that the `iss` claim matches the trusted issuer URL before processing the credential offer. This validation follows RFC 7519 section 4.1.1, which defines the issuer claim semantics in JWT."}]}

Example 2 (Boilerplate):
Text: "Table of Contents: 1. Introduction 2. Scope 3. References"
Output: {"qa_pairs": []}

Example 3 (Group Context):
Text: "Section 4.2: Authorization Details. The `authorization_details` parameter is used to convey fine-grained authorization data. It MUST be a JSON array containing objects with `type` and `locations` fields. Section 4.3: Token Endpoint. The token endpoint accepts POST requests with `grant_type` set to `authorization_code`."
Output: {"qa_pairs": [{"prompt": "What is the structure and purpose of the `authorization_details` parameter in OpenID4VCI?", "response": "The `authorization_details` parameter is used to convey fine-grained authorization data. It MUST be a JSON array containing objects with `type` and `locations` fields."}, {"prompt": "What grant type does the token endpoint accept in OpenID4VCI?", "response": "The token endpoint accepts POST requests with `grant_type` set to `authorization_code`."}]}
"""
        
    async def distill_solo(self, chunk: DocumentChunk) -> List[QAPair]:
        """Process a single chunk independently."""
        async with self.semaphore:
            try:
                response = await self.client.chat.completions.create(
                    model=self.config.llm_model,
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": f"{self.few_shot}\n\nExtract from this text:\n\n{chunk.content}"}
                    ],
                    response_format={"type": "json_object"},
                    temperature=self.config.llm_temperature,
                    max_tokens=self.config.llm_max_tokens
                )
                
                content = response.choices[0].message.content
                parsed = json.loads(content)
                qa_pairs = parsed.get("qa_pairs", [])
                
                return self._convert_to_qa(qa_pairs, chunk, "solo")
                
            except Exception as e:
                logger.error(f"Solo distillation failed for {chunk.id}: {e}")
                return []
                
    async def distill_group(self, group: List[DocumentChunk]) -> List[QAPair]:
        """
        Process a group of related chunks together.
        The LLM sees all chunks and can synthesize cross-cutting Q&A pairs.
        """
        if not group:
            return []
            
        async with self.semaphore:
            # Combine chunks with clear separators
            combined_text = ""
            for i, chunk in enumerate(group):
                combined_text += f"\n--- CHUNK {i+1} ---\n{chunk.content}\n"
                
            try:
                response = await self.client.chat.completions.create(
                    model=self.config.llm_model,
                    messages=[
                        {"role": "system", "content": self.system_prompt + "\n\nYou are processing MULTIPLE related chunks. Generate Q&A pairs that capture both specific details from individual chunks AND cross-cutting themes that span multiple chunks. Be comprehensive."},
                        {"role": "user", "content": f"{self.few_shot}\n\nExtract from these related chunks:\n\n{combined_text}"}
                    ],
                    response_format={"type": "json_object"},
                    temperature=self.config.llm_temperature,
                    max_tokens=self.config.llm_max_tokens * 2  # More tokens for groups
                )
                
                content = response.choices[0].message.content
                parsed = json.loads(content)
                qa_pairs = parsed.get("qa_pairs", [])
                
                # Attribute to primary chunk (first in group) but mark as group output
                return self._convert_to_qa(qa_pairs, group[0], "group", group_id=group[0].group_id)
                
            except Exception as e:
                logger.error(f"Group distillation failed for group {group[0].group_id}: {e}")
                return []
                
    def _convert_to_qa(self, qa_pairs: List[Dict], chunk: DocumentChunk, 
                       mode: str, group_id: Optional[str] = None) -> List[QAPair]:
        """Convert raw Q&A to structured objects."""
        results = []
        
        for qa in qa_pairs:
            prompt = qa.get("prompt", "").strip()
            response = qa.get("response", "").strip()
            
            if not prompt or not response:
                continue
                
            pair = QAPair(
                prompt=prompt,
                response=response,
                source_id=chunk.id,
                source_file=chunk.source_file,
                chunk_index=chunk.chunk_index,
                processing_mode=mode,
                group_id=group_id or chunk.group_id
            )
            results.append(pair)
            
        return results
    
    async def synthesize_knowledge(self, prompt: str, block_id: str) -> Optional[str]:
        """Run LLM synthesis for a knowledge block."""
        async with self.semaphore:
            try:
                resp = await self.client.chat.completions.create(
                    model=self.config.llm_model,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You synthesize technical documentation into coherent knowledge blocks. "
                                "Be concise but complete. Use inline citations [1], [2], etc. "
                                "Never invent facts not present in the excerpts."
                            ),
                        },
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.2,
                    max_tokens=self.config.max_knowledge_block_tokens,
                )
                return resp.choices[0].message.content
            except Exception as e:
                logger.error(f"Knowledge synthesis failed for {block_id}: {e}")
                return None

class KnowledgeSynthesizer:
    """
    Clusters chunks into topical groups and prepares prompts for
    LLM-based synthesis into coherent knowledge blocks.
    """

    def __init__(self, config: PipelineConfig):
        self.config = config

    def cluster_chunks(self, chunks: List[DocumentChunk]) -> List[List[DocumentChunk]]:
        """Group chunks by (doc_type, top-heading) and preserve document flow."""
        if not chunks:
            return []

        buckets = defaultdict(list)
        for c in chunks:
            top = c.heading_path[0] if c.heading_path else "_general"
            buckets[(c.doc_type, top)].append(c)

        groups: List[List[DocumentChunk]] = []
        for bucket in buckets.values():
            # Keep each source file's chunks in reading order
            bucket.sort(key=lambda x: (x.source_file, x.chunk_index))

            # Split into contiguous sub-groups so we don't jump around
            current = [bucket[0]]
            for c in bucket[1:]:
                last = current[-1]
                same_file = c.source_file == last.source_file
                contiguous = same_file and (c.chunk_index - last.chunk_index <= 2)
                if contiguous:
                    current.append(c)
                else:
                    groups.append(current)
                    current = [c]
            if current:
                groups.append(current)

        return groups

    def prepare_prompt(self, group: List[DocumentChunk]) -> Tuple[str, List[Dict[str, str]], str]:
        """
        Build a synthesis prompt and source inventory for a topic group.
        Returns (prompt, sources, block_id).
        """
        # If group is huge, sample to stay within context limits
        g = group
        if len(g) > self.config.max_excerpts_per_block:
            n = self.config.max_excerpts_per_block
            # Keep first, last, and evenly spaced samples in between
            idxs = [0] + [int(i * (len(g) - 1) / (n - 1)) for i in range(1, n - 1)] + [len(g) - 1]
            g = [g[i] for i in sorted(set(idxs))]

        sources: List[Dict[str, str]] = []
        seen_urls: Set[str] = set()
        excerpts: List[str] = []

        for i, c in enumerate(g):
            excerpts.append(f"--- EXCERPT {i+1} [{c.source_file}] ---\n{c.content}")
            if c.source_url and c.source_url not in seen_urls:
                sources.append({
                    "file": c.source_file,
                    "url": c.source_url,
                    "title": c.heading_path[0] if c.heading_path else c.doc_type,
                    "chunk_id": c.id,
                })
                seen_urls.add(c.source_url)

        source_list = "\n".join(
            f"[{i+1}] {s['file']} — {s['url']}" for i, s in enumerate(sources)
        )

        prompt = (
            "You are a technical documentation synthesizer. Merge the excerpts below into a single, "
            "coherent, non-repetitive knowledge block.\n\n"
            "RULES:\n"
            "1. Preserve specific details: field names, endpoints, protocol steps, requirements (MUST/SHALL), and code snippets.\n"
            "2. Remove redundancy, boilerplate, and duplicate explanations.\n"
            "3. Organize by sub-topic with clear structure (paragraphs or bullet points).\n"
            "4. Cite sources using inline markers like [1], [2] that correspond to the SOURCE LIST below.\n"
            "5. If excerpts conflict, note the conflict explicitly.\n"
            "6. Output ONLY the synthesized text, with no preamble or summary.\n\n"
            f"SOURCE LIST:\n{source_list}\n\n"
            f"EXCERPTS:\n" + "\n\n".join(excerpts)
        )

        block_id = f"kb_{hashlib.md5(prompt.encode()).hexdigest()[:10]}"
        topic = g[0].heading_path[0] if g[0].heading_path else g[0].doc_type
        return prompt, sources, block_id, topic

# =============================================================================
# STAGE 9: QUALITY FILTER
# =============================================================================

class QualityFilter:
    """Post-processing quality checks on generated Q&A pairs."""
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        
    def filter(self, qa_pairs: List[QAPair]) -> List[QAPair]:
        """Apply quality heuristics."""
        if not self.config.enable_quality_filter:
            return qa_pairs
            
        filtered = []
        
        for qa in qa_pairs:
            score = 0.0
            
            # Length checks
            if len(qa.response) < self.config.min_response_length:
                continue
            if len(qa.response) > self.config.max_response_length:
                # Truncate rather than drop
                qa.response = qa.response[:self.config.max_response_length] + "..."
                
            # Question quality
            prompt_lower = qa.prompt.lower()
            has_question_word = any(qw in prompt_lower for qw in self.config.required_question_words)
            if not has_question_word:
                score -= 0.2
                
            # Response quality heuristics
            response_lower = qa.response.lower()
            
            # Penalize generic responses
            generic_phrases = [
                "as an ai", "i don't have", "i cannot", "i'm not sure",
                "it depends", "there is no information"
            ]
            if any(gp in response_lower for gp in generic_phrases):
                continue
                
            # Reward specific technical content
            technical_indicators = ["`", "MUST", "SHALL", "endpoint", "JSON", "JWT", "request", "response"]
            for indicator in technical_indicators:
                if indicator in qa.response:
                    score += 0.1
                    
            # Reward concrete examples
            if "example" in response_lower or "e.g." in response_lower:
                score += 0.1
                
            qa.quality_score = min(max(score, 0.0), 1.0)
            
            # Only keep if meets minimum quality
            if qa.quality_score >= 0.0:  # Adjust threshold as needed
                filtered.append(qa)
                
        logger.info(f"Quality filter: {len(filtered)}/{len(qa_pairs)} passed")
        return filtered


# =============================================================================
# ORCHESTRATOR
# =============================================================================

class PipelineOrchestrator:
    """Orchestrates the full pipeline with checkpointing."""
    
    def __init__(self, config: Optional[PipelineConfig] = None):
        self.config = config or PipelineConfig()
        self.output_dir = Path(self.config.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize stages
        self.loader = FileLoader(self.config)
        self.heuristic_filter = HeuristicFilter(self.config)
        self.zero_shot_filter = ZeroShotFilter(self.config)
        self.cleaner = DataCleaner(self.config)
        self.chunker = SmartChunker(self.config)
        self.importance_scorer = ImportanceScorer(self.config)
        self.grouper = DualProcessingGrouper(self.config)
        self.distiller = AsyncLLMDistiller(self.config)
        self.quality_filter = QualityFilter(self.config)
        self.grouper = DualProcessingGrouper(self.config)
        self.knowledge_synthesizer = KnowledgeSynthesizer(self.config)
        self.distiller = AsyncLLMDistiller(self.config)
        
    def save_checkpoint(self, data: Any, name: str):
        """Save intermediate results for debugging/resumability."""
        path = self.output_dir / f"checkpoint_{name}.jsonl"
        with open(path, 'w', encoding='utf-8') as f:
            if isinstance(data, list) and data:
                if isinstance(data[0], (DocumentChunk, QAPair)):
                    for item in data:
                        f.write(json.dumps(asdict(item), ensure_ascii=False) + "\n")
                else:
                    for item in data:
                        f.write(json.dumps(item, ensure_ascii=False) + "\n")
        logger.info(f"Checkpoint saved: {path}")
        
    async def run(self):
        """Execute the full pipeline."""
        logger.info("=" * 60)
        logger.info("Starting EU Digital Software Knowledge Pipeline")
        logger.info("=" * 60)
        
        # Stage 1: Load
        documents = self.loader.load()
        
        # Stage 2: Heuristic Filter
        documents = self.heuristic_filter.filter(documents)
        
        # Stage 3: Zero-Shot Filter
        documents = self.zero_shot_filter.filter(documents)
        
        # Stage 4: Data Cleaning
        documents = self.cleaner.clean(documents)
        self.save_checkpoint(documents, "04_cleaned")
        
        # Stage 5: Smart Chunking + Deduplication
        chunks = self.chunker.chunk(documents)
        self.save_checkpoint(chunks, "05_chunked")
        
        # Stage 6: Importance Scoring
        chunks = self.importance_scorer.score_and_route(chunks)
        self.save_checkpoint(chunks, "06_scored")
        
        # Stage 7: Dual Processing Groups
        # solo_chunks, groups = self.grouper.create_groups(chunks)
        
        solo_chunks, groups = self.grouper.create_groups(chunks)
        # ------------------------------------------------------------------
        # NEW: Stage 7b – Knowledge Synthesis (compressed topic blocks)
        # ------------------------------------------------------------------
        knowledge_blocks: List[KnowledgeBlock] = []
        if self.config.enable_knowledge_synthesis:
            topic_groups = self.knowledge_synthesizer.cluster_chunks(chunks)
            logger.info(f"Knowledge synthesis: formed {len(topic_groups)} topic groups")

            synth_tasks = []
            synth_meta = []
            for g in topic_groups:
                prompt, sources, block_id, topic = self.knowledge_synthesizer.prepare_prompt(g)
                synth_tasks.append(self.distiller.synthesize_knowledge(prompt, block_id))
                synth_meta.append((block_id, topic, sources, g))

            synth_results = await asyncio.gather(*synth_tasks, return_exceptions=True)

            for (block_id, topic, sources, group), result in zip(synth_meta, synth_results):
                if isinstance(result, str) and result.strip():
                    kb = KnowledgeBlock(
                        block_id=block_id,
                        topic=topic,
                        synthesized_text=result.strip(),
                        source_chunks=[c.id for c in group],
                        sources=sources,
                        word_count=len(result.split()),
                    )
                    knowledge_blocks.append(kb)

            self.save_checkpoint(knowledge_blocks, "07b_knowledge_blocks")

            kb_path = self.output_dir / "compressed_knowledge.jsonl"
            with open(kb_path, "w", encoding="utf-8") as f:
                for kb in knowledge_blocks:
                    f.write(json.dumps(asdict(kb), ensure_ascii=False) + "\n")
            logger.info(f"Saved {len(knowledge_blocks)} knowledge blocks -> {kb_path}")

        # Stage 8: Async LLM Distillation (existing Q&A generation)
        
        
        # Stage 8: Async LLM Distillation
        all_qa_pairs = []
        
        # Process solo chunks
        logger.info(f"Processing {len(solo_chunks)} solo chunks...")
        solo_tasks = [self.distiller.distill_solo(c) for c in solo_chunks]
        solo_results = await asyncio.gather(*solo_tasks, return_exceptions=True)
        
        for result in solo_results:
            if isinstance(result, list):
                all_qa_pairs.extend(result)
                
        # Process groups
        if groups:
            logger.info(f"Processing {len(groups)} groups...")
            group_tasks = [self.distiller.distill_group(g) for g in groups]
            group_results = await asyncio.gather(*group_tasks, return_exceptions=True)
            
            for result in group_results:
                if isinstance(result, list):
                    all_qa_pairs.extend(result)
                    
        logger.info(f"Generated {len(all_qa_pairs)} raw Q&A pairs")
        
        # Stage 9: Quality Filter
        final_qa = self.quality_filter.filter(all_qa_pairs)
        
        # Save final output
        output_path = self.output_dir / "distilled_knowledge.jsonl"
        with open(output_path, 'w', encoding='utf-8') as f:
            for qa in final_qa:
                f.write(json.dumps(asdict(qa), ensure_ascii=False) + "\n")
                
        logger.info("=" * 60)
        logger.info(f"Pipeline complete! {len(final_qa)} final Q&A pairs")
        logger.info(f"Output: {output_path}")
        logger.info("=" * 60)
        
        return final_qa


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Run the pipeline with default or custom configuration."""
    # Load environment variables
    dotenv.load_dotenv()
    
    # Create configuration (modify as needed)
    config = PipelineConfig(
        target_dir="./kb_output",
        output_dir="./pipeline_output",
        
        # Model selections
        classifier_model="cross-encoder/nli-deberta-v3-base",
        embedder_model="BAAI/bge-base-en-v1.5",
        
        # Thresholds
        classifier_threshold=0.70,
        importance_threshold=0.65,
        dedup_threshold=0.92,
        
        # LLM settings
        llm_api_key=os.environ.get("LLM_API_KEY", ""),
        llm_model="deepseek-chat",
        llm_concurrent_requests=8,
        
        # Toggle stages as needed
        enable_dual_processing=True,
        enable_importance_scoring=True,
    )
    
    # Run pipeline
    orchestrator = PipelineOrchestrator(config)
    asyncio.run(orchestrator.run())


if __name__ == "__main__":
    main()