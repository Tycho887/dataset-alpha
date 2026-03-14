# verify_dataset.py
import json
import logging
import re
from collections import Counter
from pathlib import Path

import html2text  # For normalizing HTML if needed
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatasetVerifier:
    def __init__(
        self,
        jsonl_path: str,
        data_lake_path: str,
        output_report: str = "verification_report.json",
    ):
        self.jsonl_path = Path(jsonl_path)
        self.data_lake_path = Path(data_lake_path)
        self.output_report = Path(output_report)
        self.results = []

    def normalize_text(self, text: str) -> str:
        """Lowercase, collapse whitespace, remove punctuation for bag-of-words."""
        text = re.sub(r"\s+", " ", text.lower())
        text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
        return text.strip()

    def compute_lcs(self, extracted_text: str, reference_text: str) -> float:
        """Lexical Content Score = cosine similarity of TF-IDF vectors."""
        # Use character n-grams to be robust to minor differences (as in LEMUR)
        vectorizer = TfidfVectorizer(
            analyzer="char_wb", ngram_range=(2, 4), max_features=10000
        )
        texts = [
            self.normalize_text(extracted_text),
            self.normalize_text(reference_text),
        ]
        try:
            tfidf = vectorizer.fit_transform(texts)
            sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
            return float(sim)
        except Exception as e:
            logger.warning(f"LCS computation failed: {e}")
            return 0.0

    def load_reference(self, entry: dict) -> str:
        """Attempt to locate a high-quality reference for the document."""
        doc_name = entry["document_name"]
        source_dir = self.data_lake_path / doc_name

        # Look for an HTML file (often the cleanest reference)
        html_files = list(source_dir.glob("*.html")) + list(source_dir.glob("*.htm"))
        if html_files:
            # Use the first HTML file as reference
            with open(html_files[0], "r", encoding="utf-8", errors="ignore") as f:
                # Convert HTML to plain text (strip tags)
                h = html2text.HTML2Text()
                h.ignore_links = True
                h.ignore_images = True
                return h.handle(f.read())

        # If no HTML, fall back to the original raw file (e.g., PDF) – not ideal, but better than nothing
        # In practice, you might skip LCS for documents without a clean reference.
        return None

    def keyword_check(self, text: str, entry: dict) -> list:
        """Return list of missing expected keywords based on document name."""
        # Define domain-specific keywords per document type
        keyword_map = {
            "openid4vci": ["openid", "credential", "issuance", "oauth"],
            "openid4vp": ["openid", "presentation", "verifier"],
            "haip": ["high", "assurance", "profile"],
            "sd-jwt": ["selective", "disclosure", "jwt"],
            "eidas": ["eidas", "regulation", "electronic", "identification"],
            "arf": ["architecture", "reference", "framework", "wallet"],
        }
        doc_name_lower = entry["document_name"].lower()
        missing = []
        for key, words in keyword_map.items():
            if key in doc_name_lower:
                for w in words:
                    if w not in text.lower():
                        missing.append(w)
        return missing

    def run(self):
        """Process each entry in the JSONL file."""
        with open(self.jsonl_path, "r", encoding="utf-8") as f:
            for line in f:
                entry = json.loads(line)
                extracted = entry["content"]
                doc_name = entry["document_name"]
                result = {
                    "id": entry["id"],
                    "document_name": doc_name,
                    "stability": entry.get("stability", "unknown"),
                    "content_length": len(extracted),
                    "quality_issues": [],
                }

                # --- Basic heuristic checks ---
                # Alphanumeric ratio
                alpha_num = sum(c.isalnum() for c in extracted)
                if extracted:
                    ratio = alpha_num / len(extracted)
                    result["alphanumeric_ratio"] = ratio
                    if ratio < 0.6:
                        result["quality_issues"].append("low_alphanumeric_ratio")
                else:
                    result["quality_issues"].append("empty_content")

                # Keyword presence
                missing_keywords = self.keyword_check(extracted, entry)
                if missing_keywords:
                    result["missing_keywords"] = missing_keywords
                    result["quality_issues"].append("missing_expected_keywords")

                # --- Lexical Content Score (if reference available) ---
                reference = self.load_reference(entry)
                if reference:
                    lcs = self.compute_lcs(extracted, reference)
                    result["lcs"] = lcs
                    if lcs < 0.85:  # threshold you can adjust
                        result["quality_issues"].append("low_lcs")

                self.results.append(result)

        # --- Aggregate statistics ---
        report = {
            "total_documents": len(self.results),
            "documents_with_issues": sum(
                1 for r in self.results if r["quality_issues"]
            ),
            "issue_counts": Counter(),
            "lcs_stats": {},
            "alphanumeric_stats": {},
            "details": self.results,
        }

        # Collect LCS values
        lcs_vals = [r["lcs"] for r in self.results if "lcs" in r]
        if lcs_vals:
            report["lcs_stats"] = {
                "mean": float(np.mean(lcs_vals)),
                "std": float(np.std(lcs_vals)),
                "min": float(np.min(lcs_vals)),
                "max": float(np.max(lcs_vals)),
                "quartiles": [float(q) for q in np.percentile(lcs_vals, [25, 50, 75])],
            }

        alpha_vals = [
            r["alphanumeric_ratio"] for r in self.results if "alphanumeric_ratio" in r
        ]
        if alpha_vals:
            report["alphanumeric_stats"] = {
                "mean": float(np.mean(alpha_vals)),
                "std": float(np.std(alpha_vals)),
            }

        for r in self.results:
            for issue in r["quality_issues"]:
                report["issue_counts"][issue] += 1

        with open(self.output_report, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        logger.info(f"Verification complete. Report saved to {self.output_report}")


if __name__ == "__main__":
    verifier = DatasetVerifier(
        jsonl_path="training_data.jsonl", data_lake_path="data_lake"
    )
    verifier.run()
