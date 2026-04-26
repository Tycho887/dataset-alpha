#!/usr/bin/env python3
"""
EUDI Nexus MCP - Retrieval Server
==================================

A Model Context Protocol (MCP) server that exposes EUDI document retrieval
to RAG-enabled agents. Uses hybrid search (embedding similarity + PageRank)
over the pre-built index, and returns token-compressed markdown documents.

Communication: stdio (JSON-RPC 2.0) per MCP specification.

Tools exposed:
  - search_documents: Hybrid search with keyword query, returns top-K compressed docs
  - get_document: Retrieve a specific document by ID
  - get_neighborhood: Explore reference graph neighborhood

Usage:
    # Add to your MCP client config (Claude Desktop, Cline, etc.)
    {
      "mcpServers": {
        "eudi-nexus": {
          "command": "python",
          "args": ["/path/to/mcp_server.py", "--index-dir", "./mcp_index", "--compressed-dir", "./compressed"]
        }
      }
    }

Prerequisites:
    pip install sentence-transformers numpy scipy scikit-learn

Deployment notes:
    - Embedding model runs locally (default: all-MiniLM-L6-v2, ~80MB)
    - Index files loaded once at startup (~50-200MB RAM depending on corpus size)
    - Suitable for edge deployment (Raspberry Pi 4/5, small VPS, etc.)
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np

# ---------------------------------------------------------------------------
# MCP Protocol Helpers
# ---------------------------------------------------------------------------

class MCPError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


def send_message(msg: Dict[str, Any]):
    """Send a JSON-RPC message over stdout."""
    payload = json.dumps(msg, ensure_ascii=False)
    sys.stdout.write(payload + "\n")
    sys.stdout.flush()


def log_stderr(msg: str):
    """Log to stderr (won't interfere with MCP stdio)."""
    print(f"[EUDI-Nexus] {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Inference Integration (adapted from inference_engine.py)
# ---------------------------------------------------------------------------

class NexusRetriever:
    """Lightweight wrapper around the trained index for MCP serving."""

    def __init__(self, index_dir: str, compressed_dir: str, device: Optional[str] = None):
        self.index_dir = Path(index_dir)
        self.compressed_dir = Path(compressed_dir)
        self.device = device

        # Lazy imports to fail fast if deps missing
        try:
            import scipy.sparse as sp
            self._sp = sp
        except ImportError:
            raise RuntimeError("scipy is required. pip install scipy")

        self.config: Dict = {}
        self.metadata: List[Dict] = []
        self.node_index: Dict[str, int] = {}
        self.index_to_node: Dict[int, str] = {}
        self.adj_matrix = None
        self.pagerank: Optional[np.ndarray] = None
        self.doc_embeddings: Optional[np.ndarray] = None
        self.chunk_embeddings: Optional[np.ndarray] = None
        self.chunk_index: List[Dict] = []
        self.metadata_by_id: Dict[str, Dict] = {}
        self._model = None

        self._load_artifacts()

    def _load_artifacts(self):
        log_stderr(f"Loading index from: {self.index_dir}")

        with open(self.index_dir / "training_config.json", "r", encoding="utf-8") as f:
            self.config = json.load(f)

        with open(self.index_dir / "document_metadata.json", "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        with open(self.index_dir / "node_index.json", "r", encoding="utf-8") as f:
            self.node_index = json.load(f)
        self.index_to_node = {int(v): k for k, v in self.node_index.items()}

        self.adj_matrix = self._sp.load_npz(self.index_dir / "adjacency_matrix.npz")
        self.pagerank = np.load(self.index_dir / "pagerank_scores.npy")
        self.doc_embeddings = np.load(self.index_dir / "document_embeddings.npy")
        self.chunk_embeddings = np.load(self.index_dir / "chunk_embeddings.npy")

        with open(self.index_dir / "chunk_index.json", "r", encoding="utf-8") as f:
            self.chunk_index = json.load(f)

        self.metadata_by_id = {doc["id"]: doc for doc in self.metadata}

        log_stderr(f"  Loaded {len(self.metadata)} documents")
        log_stderr(f"  Embedding dim: {self.doc_embeddings.shape[1]}")
        log_stderr(f"  Total chunks: {len(self.chunk_index)}")
        log_stderr(f"  Graph: {self.adj_matrix.shape[0]} nodes, {self.adj_matrix.nnz} edges")

    def _get_model(self):
        if self._model is None:
            from sentence_transformers import SentenceTransformer
            model_name = self.config.get("model_name", "sentence-transformers/all-MiniLM-L6-v2")
            log_stderr(f"Loading embedding model: {model_name}")
            self._model = SentenceTransformer(model_name, device=self.device)
        return self._model

    def embed_query(self, query: str) -> np.ndarray:
        model = self._get_model()
        embedding = model.encode([query], normalize_embeddings=True, convert_to_numpy=True)
        return embedding[0]

    def search(
        self,
        query: str,
        top_k: int = 5,
        alpha: float = 0.7,
        use_pagerank: bool = True,
        use_chunks: bool = True,
        min_pagerank: float = 0.0,
        source_filter: Optional[List[str]] = None,
    ) -> List[Dict]:
        query_emb = self.embed_query(query)

        # Semantic similarity
        if use_chunks:
            chunk_scores = self.chunk_embeddings @ query_emb
            doc_scores = {}
            for chunk_idx, score in enumerate(chunk_scores):
                doc_id = self.chunk_index[chunk_idx]["doc_id"]
                doc_scores[doc_id] = max(doc_scores.get(doc_id, -1), float(score))
        else:
            doc_scores_arr = self.doc_embeddings @ query_emb
            doc_scores = {
                self.metadata[i]["id"]: float(doc_scores_arr[i])
                for i in range(len(self.metadata))
            }

        # Combine with PageRank
        results = []
        for doc in self.metadata:
            doc_id = doc["id"]
            semantic_score = doc_scores.get(doc_id, 0.0)

            if source_filter and doc.get("source") not in source_filter:
                continue

            node_idx = self.node_index.get(doc_id)
            pr_score = float(self.pagerank[node_idx]) if node_idx is not None else 0.0

            if pr_score < min_pagerank:
                continue

            pr_max = self.pagerank.max()
            pr_normalized = pr_score / pr_max if pr_max > 0 else 0

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

        results.sort(key=lambda x: x["combined_score"], reverse=True)
        return results[:top_k]

    def get_compressed_content(self, doc_id: str) -> Optional[str]:
        """Read the compressed markdown file for a document."""
        meta = self.metadata_by_id.get(doc_id)
        if not meta:
            return None

        # Try to find compressed file by doc_id or by original path stem
        # Strategy 1: exact match in compressed dir
        candidates = list(self.compressed_dir.rglob(f"*{doc_id.replace(' ', '_')}*_compressed.md"))
        if not candidates:
            candidates = list(self.compressed_dir.rglob(f"*{doc_id.replace(' ', '')}*_compressed.md"))

        # Strategy 2: match by original filename stem
        if not candidates and meta.get("path"):
            orig_stem = Path(meta["path"]).stem
            candidates = list(self.compressed_dir.rglob(f"{orig_stem}_compressed.md"))

        # Strategy 3: any file containing doc_id
        if not candidates:
            for f in self.compressed_dir.rglob("*_compressed.md"):
                if doc_id.replace(" ", "_") in f.name or doc_id.replace(" ", "") in f.name:
                    candidates.append(f)

        if not candidates:
            return None

        try:
            with open(candidates[0], "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            log_stderr(f"Error reading compressed file for {doc_id}: {e}")
            return None

    def get_document(self, doc_id: str) -> Optional[Dict]:
        meta = self.metadata_by_id.get(doc_id)
        if not meta:
            return None
        content = self.get_compressed_content(doc_id)
        return {
            "id": doc_id,
            "title": meta.get("title", doc_id),
            "source": meta.get("source"),
            "type": meta.get("type"),
            "path": meta.get("path"),
            "pagerank": meta.get("pagerank"),
            "is_eudi_core": meta.get("is_eudi_core", False),
            "is_draft": meta.get("is_draft", False),
            "compressed_markdown": content,
        }

    def get_neighborhood(self, doc_id: str, depth: int = 1) -> Dict:
        idx = self.node_index.get(doc_id)
        if idx is None:
            return {"error": f"Document {doc_id} not found"}

        row = self.adj_matrix.getrow(idx)
        outgoing_indices = row.indices
        outgoing = [self.index_to_node[i] for i in outgoing_indices]

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
# MCP Server
# ---------------------------------------------------------------------------

class EudiNexusMCPServer:
    def __init__(self, retriever: NexusRetriever):
        self.retriever = retriever

    def handle_initialize(self, params: Dict) -> Dict:
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {},
            },
            "serverInfo": {
                "name": "eudi-nexus-retrieval",
                "version": "1.0.0",
            },
        }

    def handle_tools_list(self, params: Dict) -> Dict:
        return {
            "tools": [
                {
                    "name": "search_documents",
                    "description": "Search the EUDI Nexus document corpus using hybrid semantic + graph ranking. Returns compressed markdown documents.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search query, keywords, or natural language description of the information need."
                            },
                            "top_k": {
                                "type": "integer",
                                "description": "Number of documents to retrieve (default: 5, max: 10)",
                                "default": 5,
                                "minimum": 1,
                                "maximum": 10,
                            },
                            "alpha": {
                                "type": "number",
                                "description": "Weight for semantic similarity vs PageRank. 0.7 = 70% semantic, 30% graph centrality.",
                                "default": 0.7,
                                "minimum": 0.0,
                                "maximum": 1.0,
                            },
                            "source_filter": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "Optional filter by source authority, e.g. ['etsi', 'ietf', 'oidf']",
                            },
                        },
                        "required": ["query"],
                    },
                },
                {
                    "name": "get_document",
                    "description": "Retrieve a specific document by its ID, including the full compressed markdown content.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "doc_id": {
                                "type": "string",
                                "description": "Document ID, e.g. 'EN 319 403' or 'RFC 7515'"
                            },
                        },
                        "required": ["doc_id"],
                    },
                },
                {
                    "name": "get_neighborhood",
                    "description": "Get the reference graph neighborhood of a document (what it references and what references it).",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "doc_id": {
                                "type": "string",
                                "description": "Document ID"
                            },
                        },
                        "required": ["doc_id"],
                    },
                },
            ]
        }

    def handle_tools_call(self, params: Dict) -> Dict:
        name = params.get("name")
        arguments = params.get("arguments", {})

        if name == "search_documents":
            return self._tool_search(arguments)
        elif name == "get_document":
            return self._tool_get_document(arguments)
        elif name == "get_neighborhood":
            return self._tool_neighborhood(arguments)
        else:
            raise MCPError(-32601, f"Tool '{name}' not found")

    def _tool_search(self, args: Dict) -> List[Dict]:
        query = args["query"]
        top_k = min(args.get("top_k", 5), 10)
        alpha = args.get("alpha", 0.7)
        source_filter = args.get("source_filter")

        log_stderr(f"search_documents: query='{query}' top_k={top_k} alpha={alpha}")
        start = time.time()

        results = self.retriever.search(
            query=query,
            top_k=top_k,
            alpha=alpha,
            source_filter=source_filter,
        )

        # Enrich with compressed content
        enriched = []
        for r in results:
            doc = self.retriever.get_document(r["id"])
            if doc and doc.get("compressed_markdown"):
                enriched.append({
                    "id": r["id"],
                    "title": r["title"],
                    "source": r["source"],
                    "type": r["type"],
                    "score": r["combined_score"],
                    "semantic_score": r["semantic_score"],
                    "pagerank": r["pagerank"],
                    "is_eudi_core": r["is_eudi_core"],
                    "is_draft": r["is_draft"],
                    "compressed_markdown": doc["compressed_markdown"],
                    "original_path": r.get("path"),
                })
            else:
                # Fallback: return metadata without content if compressed file missing
                enriched.append({
                    "id": r["id"],
                    "title": r["title"],
                    "source": r["source"],
                    "type": r["type"],
                    "score": r["combined_score"],
                    "semantic_score": r["semantic_score"],
                    "pagerank": r["pagerank"],
                    "is_eudi_core": r["is_eudi_core"],
                    "is_draft": r["is_draft"],
                    "compressed_markdown": None,
                    "original_path": r.get("path"),
                    "note": "Compressed markdown not found. Run compress_legal_docs.py first.",
                })

        elapsed = time.time() - start
        log_stderr(f"  -> {len(enriched)} results in {elapsed:.2f}s")
        return enriched

    def _tool_get_document(self, args: Dict) -> Dict:
        doc_id = args["doc_id"]
        log_stderr(f"get_document: doc_id='{doc_id}'")
        doc = self.retriever.get_document(doc_id)
        if not doc:
            raise MCPError(-32602, f"Document '{doc_id}' not found")
        return doc

    def _tool_neighborhood(self, args: Dict) -> Dict:
        doc_id = args["doc_id"]
        log_stderr(f"get_neighborhood: doc_id='{doc_id}'")
        return self.retriever.get_neighborhood(doc_id)

    def run(self):
        log_stderr("EUDI Nexus MCP Server started")
        log_stderr("Waiting for JSON-RPC messages on stdin...")

        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break

                line = line.strip()
                if not line:
                    continue

                request = json.loads(line)
                req_id = request.get("id")
                method = request.get("method")
                params = request.get("params", {})

                response = {"jsonrpc": "2.0", "id": req_id}

                try:
                    if method == "initialize":
                        result = self.handle_initialize(params)
                    elif method == "tools/list":
                        result = self.handle_tools_list(params)
                    elif method == "tools/call":
                        result = self.handle_tools_call(params)
                    else:
                        raise MCPError(-32601, f"Method '{method}' not found")

                    response["result"] = result

                except MCPError as e:
                    response["error"] = {"code": e.code, "message": e.message}
                except Exception as e:
                    log_stderr(f"Internal error: {e}")
                    response["error"] = {"code": -32603, "message": f"Internal error: {str(e)}"}

                send_message(response)

            except json.JSONDecodeError as e:
                log_stderr(f"JSON decode error: {e}")
                send_message({
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32700, "message": "Parse error"}
                })
            except Exception as e:
                log_stderr(f"Fatal loop error: {e}")
                break

        log_stderr("Shutting down")


# ---------------------------------------------------------------------------
# Standalone HTTP mode (optional, for non-MCP clients)
# ---------------------------------------------------------------------------

def run_http_server(retriever: NexusRetriever, host: str, port: int):
    """Optional FastAPI/HTTP mode if you prefer REST over stdio MCP."""
    try:
        from fastapi import FastAPI, HTTPException
        from fastapi.responses import JSONResponse
        import uvicorn
    except ImportError:
        log_stderr("FastAPI not installed. Run: pip install fastapi uvicorn")
        sys.exit(1)

    app = FastAPI(title="EUDI Nexus Retrieval API")

    @app.post("/search")
    def search(body: Dict[str, Any]):
        query = body.get("query", "")
        top_k = min(body.get("top_k", 5), 10)
        alpha = body.get("alpha", 0.7)
        source_filter = body.get("source_filter")

        results = retriever.search(query=query, top_k=top_k, alpha=alpha, source_filter=source_filter)
        enriched = []
        for r in results:
            doc = retriever.get_document(r["id"])
            enriched.append({
                "id": r["id"],
                "title": r["title"],
                "source": r["source"],
                "score": r["combined_score"],
                "compressed_markdown": doc.get("compressed_markdown") if doc else None,
            })
        return {"results": enriched}

    @app.get("/document/{doc_id}")
    def get_doc(doc_id: str):
        doc = retriever.get_document(doc_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return doc

    @app.get("/neighborhood/{doc_id}")
    def get_neighborhood(doc_id: str):
        return retriever.get_neighborhood(doc_id)

    log_stderr(f"Starting HTTP server on {host}:{port}")
    uvicorn.run(app, host=host, port=port, log_level="warning")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="EUDI Nexus MCP Retrieval Server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # MCP stdio mode (default, for Claude Desktop / Cline / etc.)
  python mcp_server.py --index-dir ./mcp_index --compressed-dir ./compressed

  # HTTP REST mode
  python mcp_server.py --http --host 0.0.0.0 --port 8000

  # CPU-only embedding (good for Raspberry Pi)
  python mcp_server.py --device cpu

  # Filter sources by default
  python mcp_server.py --source-filter etsi ietf
        """
    )
    parser.add_argument("--index-dir", default="./mcp_index", help="Path to mcp_index directory")
    parser.add_argument("--compressed-dir", default="./compressed", help="Path to compressed markdown directory")
    parser.add_argument("--device", default=None, help="Device for embeddings: cpu, cuda, mps, or auto")
    parser.add_argument("--http", action="store_true", help="Run HTTP server instead of MCP stdio")
    parser.add_argument("--host", default="127.0.0.1", help="HTTP host")
    parser.add_argument("--port", type=int, default=8000, help="HTTP port")
    parser.add_argument("--source-filter", nargs="+", default=None, help="Default source filter")
    args = parser.parse_args()

    retriever = NexusRetriever(
        index_dir=args.index_dir,
        compressed_dir=args.compressed_dir,
        device=args.device,
    )

    if args.http:
        run_http_server(retriever, args.host, args.port)
    else:
        server = EudiNexusMCPServer(retriever)
        server.run()


if __name__ == "__main__":
    main()
