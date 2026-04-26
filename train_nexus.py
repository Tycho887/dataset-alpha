#!/usr/bin/env python3
"""
EUDI Nexus MCP - Training Pipeline
==================================

This script processes downloaded EUDI Nexus documents (PDF/HTML/TXT)
and builds the embedding + graph infrastructure for MCP inference.

Prerequisites:
    pip install sentence-transformers numpy scipy scikit-learn beautifulsoup4 lxml pdfplumber

Usage:
    python train_nexus.py [--model MODEL_NAME] [--output-dir OUTPUT_DIR]

After npm run build:full, run:
    python train_nexus.py

Outputs (in output_dir/):
    - document_embeddings.npy      : (N, D) float32 array of document embeddings
    - document_metadata.json       : List of {id, title, source, path, chunks, pagerank}
    - adjacency_matrix.npz         : Sparse adjacency matrix (N x N) of reference graph
    - pagerank_scores.npy          : (N,) float64 PageRank scores
    - chunk_embeddings.npy         : (M, D) float32 array of chunk embeddings
    - chunk_index.json             : Mapping from chunk index to document id
    - training_config.json         : Config used for this training run
"""

import argparse
import json
import os
import re
import sys
import time
import warnings
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigs

warnings.filterwarnings("ignore")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

@dataclass
class Config:
    """Training configuration."""
    # Paths
    downloads_dir: str = "./downloads"
    output_dir: str = "./mcp_index"
    references_json: str = "./downloads/references.json"

    # Embedding model (open-weight from HuggingFace)
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    # Alternative high-quality models:
    #   "sentence-transformers/all-mpnet-base-v2"
    #   "BAAI/bge-large-en-v1.5"
    #   "nomic-ai/nomic-embed-text-v1.5"

    # Chunking
    chunk_size: int = 512          # tokens (approximate via characters)
    chunk_overlap: int = 128       # overlap between chunks
    max_chunks_per_doc: int = 32   # safety limit

    # PageRank
    damping: float = 0.85          # standard PageRank damping
    max_iter: int = 100
    tol: float = 1e-6

    # Processing
    batch_size: int = 32
    device: Optional[str] = None   # None = auto, "cpu", "cuda", "mps"

    def to_dict(self):
        return asdict(self)


# ---------------------------------------------------------------------------
# Document Loading
# ---------------------------------------------------------------------------

class DocumentLoader:
    """Load and extract text from PDF, HTML, and TXT files."""

    def __init__(self):
        self._pdf_available = False
        self._bs4_available = False
        self._lxml_available = False
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

    def load(self, file_path: str) -> Optional[str]:
        """Load text from a file based on extension."""
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
            # Remove script/style tags
            for tag in soup(["script", "style", "nav", "header", "footer"]):
                tag.decompose()
            text = soup.get_text(separator="\n")
            # Clean up whitespace
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
        # DOCX text extraction requires python-docx; we skip if unavailable
        try:
            import docx
            doc = docx.Document(path)
            return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        except ImportError:
            print(f"  [WARN] python-docx not installed, skipping DOCX: {path}")
            return None
        except Exception as e:
            print(f"  [WARN] Failed to parse DOCX {path}: {e}")
            return None


# ---------------------------------------------------------------------------
# Text Chunking
# ---------------------------------------------------------------------------

class DocumentChunker:
    """Split documents into overlapping chunks."""

    def __init__(self, chunk_size: int = 512, chunk_overlap: int = 128,
                 max_chunks: int = 32):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.max_chunks = max_chunks

    def chunk(self, text: str) -> List[str]:
        """Split text into chunks. Uses approximate token counting via characters."""
        if not text:
            return []

        # Rough heuristic: 1 token ≈ 4 chars for English text
        chars_per_chunk = self.chunk_size * 4
        overlap_chars = self.chunk_overlap * 4

        # First, split into paragraphs/sentences to avoid breaking mid-sentence
        paragraphs = re.split(r"\n{2,}", text.strip())
        paragraphs = [p.strip() for p in paragraphs if p.strip()]

        chunks = []
        current_chunk = []
        current_len = 0

        for para in paragraphs:
            para_len = len(para)
            if current_len + para_len > chars_per_chunk and current_chunk:
                chunks.append("\n\n".join(current_chunk))
                # Start new chunk with overlap
                overlap_text = " ".join(current_chunk)
                overlap_words = overlap_text.split()
                overlap_start = max(0, len(overlap_text) - overlap_chars)
                overlap_para = overlap_text[overlap_start:]
                current_chunk = [overlap_para, para] if overlap_para else [para]
                current_len = len(current_chunk[0]) + para_len
            else:
                current_chunk.append(para)
                current_len += para_len

        if current_chunk:
            chunks.append("\n\n".join(current_chunk))

        # If still too large, force-split
        final_chunks = []
        for chunk in chunks:
            if len(chunk) > chars_per_chunk * 2:
                # Force split by character count
                for i in range(0, len(chunk), chars_per_chunk - overlap_chars):
                    final_chunks.append(chunk[i:i + chars_per_chunk])
            else:
                final_chunks.append(chunk)

        return final_chunks[:self.max_chunks]


# ---------------------------------------------------------------------------
# Embedding Engine
# ---------------------------------------------------------------------------

class EmbeddingEngine:
    """Local embedding using HuggingFace sentence-transformers."""

    def __init__(self, model_name: str, device: Optional[str] = None,
                 batch_size: int = 32):
        self.model_name = model_name
        self.batch_size = batch_size
        self.device = device
        self.model = None
        self._load_model()

    def _load_model(self):
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError:
            print("ERROR: sentence-transformers not installed.")
            print("  pip install sentence-transformers")
            sys.exit(1)

        print(f"Loading embedding model: {self.model_name}")
        start = time.time()
        self.model = SentenceTransformer(self.model_name, device=self.device)
        elapsed = time.time() - start
        print(f"  Model loaded in {elapsed:.1f}s on {self.model.device}")
        print(f"  Embedding dimension: {self.model.get_sentence_embedding_dimension()}")

    def encode(self, texts: List[str], show_progress: bool = True) -> np.ndarray:
        """Encode texts to embeddings."""
        if not texts:
            dim = self.model.get_sentence_embedding_dimension()
            return np.zeros((0, dim), dtype=np.float32)

        return self.model.encode(
            texts,
            batch_size=self.batch_size,
            show_progress_bar=show_progress,
            convert_to_numpy=True,
            normalize_embeddings=True,  # L2 normalize for cosine similarity
        )


# ---------------------------------------------------------------------------
# Graph & PageRank
# ---------------------------------------------------------------------------

class GraphBuilder:
    """Build adjacency matrix from references.json graph data."""

    def __init__(self, damping: float = 0.85, max_iter: int = 100, tol: float = 1e-6):
        self.damping = damping
        self.max_iter = max_iter
        self.tol = tol

    def build(self, nodes: List[Dict], edges: List[Dict]) -> Tuple[sp.csr_matrix, np.ndarray, Dict]:
        """
        Build adjacency matrix and compute PageRank.

        Returns:
            adj_matrix: Sparse CSR adjacency matrix (N x N)
            pagerank:   PageRank scores (N,)
            node_index: {doc_id -> matrix_index}
        """
        # Create ordered node list
        node_list = sorted([n["id"] for n in nodes])
        node_index = {doc_id: i for i, doc_id in enumerate(node_list)}
        N = len(node_list)

        print(f"Building graph: {N} nodes, {len(edges)} edges")

        # Build adjacency list
        adj_list = {i: [] for i in range(N)}
        edge_counts = {"normative": 0, "informative": 0}

        for edge in edges:
            src = edge.get("from")
            dst = edge.get("to")
            if src in node_index and dst in node_index:
                i = node_index[src]
                j = node_index[dst]
                adj_list[i].append(j)
                edge_counts[edge.get("type", "normative")] += 1

        print(f"  Normative edges: {edge_counts['normative']}")
        print(f"  Informative edges: {edge_counts['informative']}")

        # Build sparse matrix (row-normalized for PageRank)
        rows, cols, data = [], [], []
        for i in range(N):
            out_neighbors = adj_list[i]
            if out_neighbors:
                weight = 1.0 / len(out_neighbors)
                for j in out_neighbors:
                    rows.append(i)
                    cols.append(j)
                    data.append(weight)

        adj_matrix = sp.csr_matrix((data, (rows, cols)), shape=(N, N), dtype=np.float64)

        # Compute PageRank
        pagerank = self._compute_pagerank(adj_matrix, N)

        # Attach PageRank to nodes
        for node in nodes:
            idx = node_index.get(node["id"])
            if idx is not None:
                node["pagerank"] = float(pagerank[idx])

        return adj_matrix, pagerank, node_index

    def _compute_pagerank(self, M: sp.csr_matrix, N: int) -> np.ndarray:
        """Power iteration PageRank."""
        print("Computing PageRank...")
        start = time.time()

        # Dangling nodes: columns with no out-links get uniform distribution
        dangling = np.asarray(M.sum(axis=1)).flatten() == 0

        # Initialize
        pr = np.ones(N) / N

        for iteration in range(self.max_iter):
            pr_new = np.zeros(N)

            # Dangling node contribution
            dangling_sum = pr[dangling].sum() / N if dangling.any() else 0.0

            # Matrix-vector multiplication
            pr_new = self.damping * (M.T @ pr + dangling_sum) + (1 - self.damping) / N

            # Check convergence
            diff = np.linalg.norm(pr_new - pr, ord=1)
            pr = pr_new

            if diff < self.tol:
                elapsed = time.time() - start
                print(f"  Converged in {iteration + 1} iterations ({elapsed:.2f}s)")
                break
        else:
            elapsed = time.time() - start
            print(f"  Reached max iterations ({elapsed:.2f}s)")

        return pr


# ---------------------------------------------------------------------------
# Training Pipeline
# ---------------------------------------------------------------------------

class TrainingPipeline:
    def __init__(self, config: Config):
        self.config = config
        self.loader = DocumentLoader()
        self.chunker = DocumentChunker(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            max_chunks=config.max_chunks_per_doc,
        )
        self.embedder = EmbeddingEngine(
            model_name=config.model_name,
            device=config.device,
            batch_size=config.batch_size,
        )
        self.graph_builder = GraphBuilder(
            damping=config.damping,
            max_iter=config.max_iter,
            tol=config.tol,
        )

    def run(self):
        os.makedirs(self.config.output_dir, exist_ok=True)

        # 1. Load references.json
        print("=" * 60)
        print("STEP 1: Load reference graph")
        print("=" * 60)
        graph_data = self._load_references_json()
        if not graph_data:
            print("ERROR: Could not load references.json")
            sys.exit(1)

        nodes = graph_data.get("nodes", [])
        edges = graph_data.get("edges", [])
        print(f"Loaded {len(nodes)} nodes, {len(edges)} edges")

        # 2. Build adjacency matrix & PageRank
        print("\n" + "=" * 60)
        print("STEP 2: Build adjacency matrix & PageRank")
        print("=" * 60)
        adj_matrix, pagerank, node_index = self.graph_builder.build(nodes, edges)

        # 3. Load document texts
        print("\n" + "=" * 60)
        print("STEP 3: Load & chunk documents")
        print("=" * 60)
        documents = self._load_documents(nodes)

        # 4. Generate embeddings
        print("\n" + "=" * 60)
        print("STEP 4: Generate embeddings")
        print("=" * 60)
        doc_embeddings, chunk_embeddings, chunk_index = self._generate_embeddings(documents)

        # 5. Save artifacts
        print("\n" + "=" * 60)
        print("STEP 5: Save artifacts")
        print("=" * 60)
        self._save_artifacts(
            nodes, adj_matrix, pagerank, node_index,
            doc_embeddings, chunk_embeddings, chunk_index
        )

        print("\n" + "=" * 60)
        print("Training complete!")
        print("=" * 60)

    def _load_references_json(self) -> Optional[Dict]:
        path = Path(self.config.references_json)
        if not path.exists():
            print(f"ERROR: {path} not found. Run 'npm run build:full' first.")
            return None
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("graph", data)

    def _load_documents(self, nodes: List[Dict]) -> List[Dict]:
        """Load text for each node that has a downloadable path."""
        documents = []
        specs_dir = Path(self.config.downloads_dir) / "specs"

        for node in nodes:
            doc_id = node["id"]
            file_path = node.get("path")

            if not file_path:
                # Try to find file by ID heuristic
                file_path = self._guess_file_path(doc_id, specs_dir)

            if not file_path or not Path(file_path).exists():
                continue

            print(f"Loading {doc_id} ...")
            text = self.loader.load(file_path)

            if text:
                chunks = self.chunker.chunk(text)
                documents.append({
                    "id": doc_id,
                    "title": node.get("title", doc_id),
                    "source": node.get("source", "unknown"),
                    "type": node.get("type", "unknown"),
                    "path": str(file_path),
                    "text": text,
                    "chunks": chunks,
                    "pagerank": node.get("pagerank", 0.0),
                    "referenced_by_count": node.get("referencedByCount", 0),
                    "references_count": node.get("referencesCount", 0),
                })
                print(f"  -> {len(text)} chars, {len(chunks)} chunks")
            else:
                print(f"  -> No text extracted")

        print(f"\nLoaded {len(documents)} documents with text")
        return documents

    # def _guess_file_path(self, doc_id: str, specs_dir: Path) -> Optional[str]:
    #     """Try to find a file matching the document ID."""
    #     # ETSI format: "EN 319 403" -> en_319403*.pdf
    #     etsi_match = re.match(r"(EN|TS|TR|ES|EG|SR)\s+(\d{3})\s+(\d{3})(?:-(\d+))?", doc_id, re.I)
    #     if etsi_match:
    #         type_prefix = etsi_match.group(1).lower()
    #         num = etsi_match.group(2) + etsi_match.group(3)
    #         part = etsi_match.group(4)
    #         if part:
    #             num += f"{int(part):02d}"
    #         pattern = f"{type_prefix}_{num}*.pdf"
    #         matches = list(specs_dir.rglob(pattern))
    #         if matches:
    #             return str(matches[0])

    #     # RFC format: "RFC 7515" -> rfc7515.txt
    #     rfc_match = re.match(r"RFC\s+(\d+)", doc_id, re.I)
    #     if rfc_match:
    #         pattern = f"rfc{rfc_match.group(1)}.txt"
    #         matches = list((specs_dir / "IETF").rglob(pattern))
    #         if matches:
    #             return str(matches[0])

    #     # OIDF format: "OpenID4VP" -> OpenID4VP.html
    #     oidf_match = re.match(r"OpenID.*|HAIP|SD-JWT.*", doc_id, re.I)
    #     if oidf_match:
    #         pattern = f"{doc_id.replace(' ', '_')}*.html"
    #         matches = list((specs_dir / "OIDF").rglob(pattern))
    #         if not matches:
    #             # Try exact match
    #             matches = list((specs_dir / "OIDF").rglob(f"{doc_id}*.html"))
    #         if matches:
    #             return str(matches[0])

    #     return None

    def _guess_file_path(self, doc_id: str, specs_dir: Path) -> Optional[str]:
        """Try to find a file matching the document ID."""

        # 1. ETSI format: "EN 319 403" -> en_319403*.pdf
        etsi_match = re.match(r"(EN|TS|TR|ES|EG|SR)\s+(\d{3})\s+(\d{3})(?:-(\d+))?", doc_id, re.I)
        if etsi_match:
            type_prefix = etsi_match.group(1).lower()
            num = etsi_match.group(2) + etsi_match.group(3)
            part = etsi_match.group(4)
            if part:
                num += f"{int(part):02d}"
            pattern = f"{type_prefix}_{num}*.pdf"
            matches = list(specs_dir.rglob(pattern))
            if matches:
                return str(matches[0])

        # 2. RFC format: "RFC 7515" -> rfc7515.txt
        rfc_match = re.match(r"RFC\s+(\d+)", doc_id, re.I)
        if rfc_match:
            pattern = f"rfc{rfc_match.group(1)}.txt"
            matches = list((specs_dir / "IETF").rglob(pattern))
            if matches:
                return str(matches[0])

        # 3. OIDF format: "OpenID4VP" -> OpenID4VP.html
        oidf_match = re.match(r"OpenID.*|HAIP|SD-JWT.*", doc_id, re.I)
        if oidf_match:
            pattern = f"{doc_id.replace(' ', '_')}*.html"
            matches = list((specs_dir / "OIDF").rglob(pattern))
            if not matches:
                matches = list((specs_dir / "OIDF").rglob(f"{doc_id}*.html"))
            if matches:
                return str(matches[0])

        # 4. IETF DRAFTS: "SD-JWT VC" -> search IETF/ for *sd-jwt-vc*.txt
        #    Handles drafts that aren't RFCs but are classified as ietf source
        ietf_draft_match = re.match(r"SD-JWT(?:\s+VC)?", doc_id, re.I)
        if ietf_draft_match:
            # Normalize: "SD-JWT VC" -> "sd-jwt-vc"
            normalized = doc_id.lower().replace(" ", "-")
            # Search IETF directory for any .txt containing the normalized name
            ietf_dir = specs_dir / "IETF"
            if ietf_dir.exists():
                for txt_file in ietf_dir.rglob("*.txt"):
                    if normalized in txt_file.name.lower():
                        return str(txt_file)
            # Also try broader match: any file with "sd-jwt" in the name
            for txt_file in ietf_dir.rglob("*.txt"):
                if "sd-jwt" in txt_file.name.lower():
                    return str(txt_file)

        return None

    def _generate_embeddings(self, documents: List[Dict]) -> Tuple[np.ndarray, np.ndarray, List[Dict]]:
        """Generate document-level and chunk-level embeddings."""
        # Document-level: embed concatenated title + first chunk
        doc_texts = []
        for doc in documents:
            title = doc["title"] if doc["title"] != doc["id"] else ""
            first_chunk = doc["chunks"][0] if doc["chunks"] else ""
            text = f"{title}\n{first_chunk}".strip() if title else first_chunk
            doc_texts.append(text)

        print(f"\nEncoding {len(doc_texts)} document summaries...")
        doc_embeddings = self.embedder.encode(doc_texts, show_progress=True)

        # Chunk-level: embed all chunks
        all_chunks = []
        chunk_index = []  # maps chunk idx -> {doc_id, chunk_idx}

        for doc in documents:
            for i, chunk in enumerate(doc["chunks"]):
                all_chunks.append(chunk)
                chunk_index.append({
                    "doc_id": doc["id"],
                    "chunk_idx": i,
                    "text_preview": chunk[:200],
                })

        print(f"\nEncoding {len(all_chunks)} chunks...")
        chunk_embeddings = self.embedder.encode(all_chunks, show_progress=True)

        return doc_embeddings, chunk_embeddings, chunk_index

    def _save_artifacts(self, nodes, adj_matrix, pagerank, node_index,
                        doc_embeddings, chunk_embeddings, chunk_index):
        out = Path(self.config.output_dir)

        # 1. Config
        config_path = out / "training_config.json"
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(self.config.to_dict(), f, indent=2)
        print(f"Saved: {config_path}")

        # 2. Document metadata (only nodes with embeddings)
        metadata = []
        for node in nodes:
            metadata.append({
                "id": node["id"],
                "title": node.get("title", node["id"]),
                "source": node.get("source", "unknown"),
                "type": node.get("type", "unknown"),
                "path": node.get("path"),
                "is_draft": node.get("isDraft", False),
                "is_eudi_core": node.get("isEudiCore", False),
                "pagerank": float(node.get("pagerank", 0.0)),
                "referenced_by_count": node.get("referencedByCount", 0),
                "references_count": node.get("referencesCount", 0),
            })

        meta_path = out / "document_metadata.json"
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)
        print(f"Saved: {meta_path} ({len(metadata)} documents)")

        # 3. Node index mapping
        index_path = out / "node_index.json"
        with open(index_path, "w", encoding="utf-8") as f:
            json.dump(node_index, f, indent=2)
        print(f"Saved: {index_path}")

        # 4. Adjacency matrix
        adj_path = out / "adjacency_matrix.npz"
        sp.save_npz(adj_path, adj_matrix)
        print(f"Saved: {adj_path} ({adj_matrix.shape}, {adj_matrix.nnz} non-zeros)")

        # 5. PageRank scores
        pr_path = out / "pagerank_scores.npy"
        np.save(pr_path, pagerank)
        print(f"Saved: {pr_path} ({pagerank.shape})")

        # 6. Document embeddings
        doc_emb_path = out / "document_embeddings.npy"
        np.save(doc_emb_path, doc_embeddings.astype(np.float32))
        print(f"Saved: {doc_emb_path} ({doc_embeddings.shape})")

        # 7. Chunk embeddings
        chunk_emb_path = out / "chunk_embeddings.npy"
        np.save(chunk_emb_path, chunk_embeddings.astype(np.float32))
        print(f"Saved: {chunk_emb_path} ({chunk_embeddings.shape})")

        # 8. Chunk index
        chunk_idx_path = out / "chunk_index.json"
        with open(chunk_idx_path, "w", encoding="utf-8") as f:
            json.dump(chunk_index, f, indent=2)
        print(f"Saved: {chunk_idx_path} ({len(chunk_index)} chunks)")

        # 9. Summary
        summary = {
            "total_nodes": len(nodes),
            "total_edges": adj_matrix.nnz,
            "documents_with_text": doc_embeddings.shape[0],
            "total_chunks": chunk_embeddings.shape[0],
            "embedding_dim": doc_embeddings.shape[1],
            "embedding_model": self.config.model_name,
        }
        summary_path = out / "summary.json"
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        print(f"Saved: {summary_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="EUDI Nexus MCP Training Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Default run (after npm run build:full)
  python train_nexus.py

  # Use a larger embedding model
  python train_nexus.py --model sentence-transformers/all-mpnet-base-v2

  # Custom output directory
  python train_nexus.py --output-dir ./my_index

  # CPU-only mode
  python train_nexus.py --device cpu
        """
    )
    parser.add_argument(
        "--downloads-dir", default="./downloads",
        help="Path to downloads directory (default: ./downloads)"
    )
    parser.add_argument(
        "--output-dir", default="./mcp_index",
        help="Path to output directory (default: ./mcp_index)"
    )
    parser.add_argument(
        "--model", default="sentence-transformers/all-MiniLM-L6-v2",
        help="HuggingFace model name for embeddings"
    )
    parser.add_argument(
        "--device", default=None,
        help="Device: cpu, cuda, mps, or auto (default: auto)"
    )
    parser.add_argument(
        "--chunk-size", type=int, default=512,
        help="Chunk size in approximate tokens (default: 512)"
    )
    parser.add_argument(
        "--chunk-overlap", type=int, default=128,
        help="Chunk overlap in approximate tokens (default: 128)"
    )
    parser.add_argument(
        "--batch-size", type=int, default=32,
        help="Embedding batch size (default: 32)"
    )

    args = parser.parse_args()

    config = Config(
        downloads_dir=args.downloads_dir,
        output_dir=args.output_dir,
        references_json=os.path.join(args.downloads_dir, "references.json"),
        model_name=args.model,
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
        batch_size=args.batch_size,
        device=args.device,
    )

    pipeline = TrainingPipeline(config)
    pipeline.run()


if __name__ == "__main__":
    main()
