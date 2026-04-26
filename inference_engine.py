#!/usr/bin/env python3
"""
EUDI Nexus MCP - Inference Engine
=================================

Load trained artifacts and answer queries by combining:
  1. Semantic similarity (embedding-based retrieval)
  2. Graph centrality (PageRank on reference graph)
  3. Hybrid scoring

Usage:
    from inference_engine import NexusInference
    engine = NexusInference("./mcp_index")
    results = engine.search("OpenID4VP presentation exchange", top_k=10)
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import scipy.sparse as sp


class NexusInference:
    """
    Inference engine for EUDI Nexus MCP.

    Loads pre-computed embeddings, adjacency matrix, and PageRank scores.
    Ranks documents by combining semantic similarity with graph importance.
    """

    def __init__(self, index_dir: str, device: Optional[str] = None):
        self.index_dir = Path(index_dir)
        self.device = device

        # Loaded artifacts
        self.config: Dict = {}
        self.metadata: List[Dict] = []
        self.node_index: Dict[str, int] = {}
        self.index_to_node: Dict[int, str] = {}
        self.adj_matrix: Optional[sp.csr_matrix] = None
        self.pagerank: Optional[np.ndarray] = None
        self.doc_embeddings: Optional[np.ndarray] = None
        self.chunk_embeddings: Optional[np.ndarray] = None
        self.chunk_index: List[Dict] = []

        # Embedding model (lazy-loaded)
        self._model = None

        self._load_artifacts()

    def _load_artifacts(self):
        """Load all training artifacts from disk."""
        print(f"Loading index from: {self.index_dir}")

        # Config
        with open(self.index_dir / "training_config.json", "r", encoding="utf-8") as f:
            self.config = json.load(f)

        # Metadata
        with open(self.index_dir / "document_metadata.json", "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        # Node index
        with open(self.index_dir / "node_index.json", "r", encoding="utf-8") as f:
            self.node_index = json.load(f)
        self.index_to_node = {int(v): k for k, v in self.node_index.items()}

        # Adjacency matrix
        self.adj_matrix = sp.load_npz(self.index_dir / "adjacency_matrix.npz")

        # PageRank
        self.pagerank = np.load(self.index_dir / "pagerank_scores.npy")

        # Embeddings
        self.doc_embeddings = np.load(self.index_dir / "document_embeddings.npy")
        self.chunk_embeddings = np.load(self.index_dir / "chunk_embeddings.npy")

        # Chunk index
        with open(self.index_dir / "chunk_index.json", "r", encoding="utf-8") as f:
            self.chunk_index = json.load(f)

        # Build metadata lookup
        self.metadata_by_id = {doc["id"]: doc for doc in self.metadata}

        print(f"  Loaded {len(self.metadata)} documents")
        print(f"  Embedding dim: {self.doc_embeddings.shape[1]}")
        print(f"  Total chunks: {len(self.chunk_index)}")
        print(f"  Graph: {self.adj_matrix.shape[0]} nodes, {self.adj_matrix.nnz} edges")

    def _get_model(self):
        """Lazy-load the embedding model."""
        if self._model is None:
            from sentence_transformers import SentenceTransformer
            model_name = self.config.get("model_name", "sentence-transformers/all-MiniLM-L6-v2")
            print(f"Loading embedding model: {model_name}")
            self._model = SentenceTransformer(model_name, device=self.device)
        return self._model

    def embed_query(self, query: str) -> np.ndarray:
        """Embed a query string."""
        model = self._get_model()
        embedding = model.encode([query], normalize_embeddings=True, convert_to_numpy=True)
        return embedding[0]

    def search(
        self,
        query: str,
        top_k: int = 10,
        alpha: float = 0.7,
        use_pagerank: bool = True,
        use_chunks: bool = True,
        min_pagerank: float = 0.0,
        source_filter: Optional[List[str]] = None,
    ) -> List[Dict]:
        """
        Search for relevant documents.

        Args:
            query: Search query string
            top_k: Number of results to return
            alpha: Weight for semantic similarity (1-alpha for PageRank)
            use_pagerank: Whether to incorporate PageRank scores
            use_chunks: Whether to search at chunk level (more granular)
            min_pagerank: Minimum PageRank threshold for results
            source_filter: Only return docs from these sources (e.g., ["etsi", "ietf"])

        Returns:
            List of result dicts with keys: id, title, source, score, pagerank, path
        """
        query_emb = self.embed_query(query)

        # --- Semantic similarity ---
        if use_chunks:
            # Search chunks, then aggregate to documents
            chunk_scores = self.chunk_embeddings @ query_emb  # cosine similarity (already normalized)
            doc_scores = {}
            for chunk_idx, score in enumerate(chunk_scores):
                doc_id = self.chunk_index[chunk_idx]["doc_id"]
                doc_scores[doc_id] = max(doc_scores.get(doc_id, -1), float(score))
        else:
            # Search document-level embeddings
            doc_scores_arr = self.doc_embeddings @ query_emb
            doc_scores = {
                self.metadata[i]["id"]: float(doc_scores_arr[i])
                for i in range(len(self.metadata))
            }

        # --- Combine with PageRank ---
        results = []
        for doc in self.metadata:
            doc_id = doc["id"]
            semantic_score = doc_scores.get(doc_id, 0.0)

            # Source filter
            if source_filter and doc.get("source") not in source_filter:
                continue

            # PageRank component
            node_idx = self.node_index.get(doc_id)
            pr_score = float(self.pagerank[node_idx]) if node_idx is not None else 0.0

            if pr_score < min_pagerank:
                continue

            # Normalize PageRank to [0, 1] for combination
            pr_max = self.pagerank.max()
            pr_normalized = pr_score / pr_max if pr_max > 0 else 0

            # Hybrid score
            if use_pagerank:
                combined_score = alpha * semantic_score + (1 - alpha) * pr_normalized
            else:
                combined_score = semantic_score

            results.append({
                "id": doc_id,
                "title": doc.get("title", doc_id),
                "source": doc.get("source", "unknown"),
                "type": doc.get("type", "unknown"),
                "path": doc.get("path"),
                "semantic_score": round(semantic_score, 4),
                "pagerank": round(pr_score, 6),
                "pagerank_normalized": round(pr_normalized, 4),
                "combined_score": round(combined_score, 4),
                "is_eudi_core": doc.get("is_eudi_core", False),
                "is_draft": doc.get("is_draft", False),
            })

        # Sort by combined score descending
        results.sort(key=lambda x: x["combined_score"], reverse=True)
        return results[:top_k]

    def search_by_keywords(
        self,
        keywords: List[str],
        top_k: int = 10,
        alpha: float = 0.7,
        **kwargs
    ) -> List[Dict]:
        """
        Search using multiple keywords (as from an MCP tool call).

        Args:
            keywords: List of keywords/topics from the tool call
            top_k: Number of results
            alpha: Semantic vs PageRank weight
            **kwargs: Passed to search()

        Returns:
            Ranked list of documents
        """
        # Combine keywords into a single query
        query = ", ".join(keywords)
        return self.search(query, top_k=top_k, alpha=alpha, **kwargs)

    def get_document_context(self, doc_id: str, max_chunks: int = 3) -> Optional[Dict]:
        """
        Retrieve full context for a document including its top-matching chunks.
        Useful for feeding document content back to the LLM.
        """
        doc_meta = self.metadata_by_id.get(doc_id)
        if not doc_meta:
            return None

        # Find chunks belonging to this document
        doc_chunks = [
            (i, chunk) for i, chunk in enumerate(self.chunk_index)
            if chunk["doc_id"] == doc_id
        ]

        # Get chunk texts (would need to store them; here we just return previews)
        chunks = [
            {
                "chunk_idx": idx,
                "preview": chunk_info["text_preview"],
            }
            for idx, chunk_info in doc_chunks[:max_chunks]
        ]

        return {
            "id": doc_id,
            "title": doc_meta.get("title", doc_id),
            "source": doc_meta.get("source"),
            "path": doc_meta.get("path"),
            "pagerank": doc_meta.get("pagerank"),
            "referenced_by": doc_meta.get("referenced_by_count", 0),
            "references": doc_meta.get("references_count", 0),
            "chunks": chunks,
        }

    def get_neighborhood(self, doc_id: str, depth: int = 1) -> Dict:
        """
        Get the reference neighborhood of a document (documents it references
        and is referenced by). Useful for exploration.
        """
        idx = self.node_index.get(doc_id)
        if idx is None:
            return {"error": f"Document {doc_id} not found"}

        # Outgoing references (this doc -> others)
        row = self.adj_matrix.getrow(idx)
        outgoing_indices = row.indices
        outgoing = [self.index_to_node[i] for i in outgoing_indices]

        # Incoming references (others -> this doc)
        col = self.adj_matrix.getcol(idx)
        incoming_indices = col.indices
        incoming = [self.index_to_node[i] for i in incoming_indices]

        return {
            "document": doc_id,
            "depth": depth,
            "references": outgoing,
            "referenced_by": incoming,
        }


# ---------------------------------------------------------------------------
# CLI Demo
# ---------------------------------------------------------------------------

def demo():
    import argparse

    parser = argparse.ArgumentParser(description="EUDI Nexus MCP Inference Demo")
    parser.add_argument("--index-dir", default="./mcp_index", help="Path to index directory")
    parser.add_argument("--query", default="OpenID4VP presentation exchange", help="Search query")
    parser.add_argument("--top-k", type=int, default=10, help="Number of results")
    parser.add_argument("--alpha", type=float, default=0.7, help="Semantic weight")
    parser.add_argument("--device", default=None, help="Device for embeddings")
    parser.add_argument("--source", nargs="+", default=None, help="Filter by source (etsi ietf oidf)")
    args = parser.parse_args()

    engine = NexusInference(args.index_dir, device=args.device)

    print("\n" + "=" * 60)
    print(f"Query: {args.query}")
    print("=" * 60)

    results = engine.search(
        args.query,
        top_k=args.top_k,
        alpha=args.alpha,
        source_filter=args.source,
    )

    print(f"\nTop {len(results)} results:\n")
    for i, r in enumerate(results, 1):
        core_marker = " [CORE]" if r["is_eudi_core"] else ""
        draft_marker = " [DRAFT]" if r["is_draft"] else ""
        print(f"{i}. {r['id']}{core_marker}{draft_marker}")
        print(f"   Title: {r['title']}")
        print(f"   Source: {r['source']} | Type: {r['type']}")
        print(f"   Score: {r['combined_score']} (semantic={r['semantic_score']}, PR={r['pagerank']:.2e})")
        if r["path"]:
            print(f"   Path: {r['path']}")
        print()


if __name__ == "__main__":
    demo()
