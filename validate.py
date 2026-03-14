# lcs_quality_check.py
import hashlib
import json
import re
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class LexicalContentScore:
    """
    Implements the Lexical Content Score (LCS) from the LEMUR paper
    to evaluate PDF-to-text conversion quality
    """

    def __init__(self):
        self.vectorizer = CountVectorizer(
            lowercase=True,
            token_pattern=r"(?u)\b\w+\b",  # Simple word tokenization
            stop_words=None,  # Keep all words for legal terminology
        )

    def normalize_text(self, text):
        """
        Normalize text for fair comparison as described in LEMUR:
        - Remove styling/HTML tags
        - Convert to lowercase
        - Normalize numeric formatting
        - Collapse repeated punctuation
        """
        # Remove HTML tags if present
        text = re.sub(r"<[^>]+>", " ", text)

        # Convert to lowercase
        text = text.lower()

        # Normalize numbers (replace all numbers with a placeholder or standardize format)
        text = re.sub(r"\d+", "NUM", text)

        # Collapse repeated punctuation
        text = re.sub(r"([.!?]){2,}", r"\1", text)

        # Remove extra whitespace
        text = " ".join(text.split())

        return text

    def compute_lcs(self, pdf_text, html_text):
        """
        Compute Lexical Content Score between PDF-extracted text and reference HTML

        Returns cosine similarity score (0-1) where 1 means perfect lexical preservation
        """
        # Normalize both texts
        pdf_norm = self.normalize_text(pdf_text)
        html_norm = self.normalize_text(html_text)

        # Create bag-of-words vectors
        try:
            # Fit on combined text to ensure same vocabulary
            combined = [pdf_norm, html_norm]
            X = self.vectorizer.fit_transform(combined)

            # Compute cosine similarity
            similarity = cosine_similarity(X[0:1], X[1:2])[0][0]
            return float(similarity)
        except Exception as e:
            print(f"Error computing LCS: {e}")
            return 0.0

    def batch_evaluate(self, pdf_dir, html_reference_dir):
        """
        Evaluate LCS for multiple documents
        """
        results = {}

        pdf_files = list(Path(pdf_dir).glob("*.txt"))  # Assuming converted PDFs as .txt

        for pdf_path in pdf_files:
            # Find corresponding HTML reference (assumes matching filenames)
            doc_id = pdf_path.stem
            html_path = Path(html_reference_dir) / f"{doc_id}.html"

            if not html_path.exists():
                print(f"No reference HTML found for {doc_id}")
                continue

            with open(pdf_path, "r", encoding="utf-8") as f:
                pdf_text = f.read()

            with open(html_path, "r", encoding="utf-8") as f:
                html_text = f.read()

            lcs_score = self.compute_lcs(pdf_text, html_text)
            results[doc_id] = {
                "lcs_score": lcs_score,
                "pdf_path": str(pdf_path),
                "html_path": str(html_path),
            }

            print(f"{doc_id}: LCS = {lcs_score:.4f}")

        # Summary statistics
        scores = [r["lcs_score"] for r in results.values()]
        if scores:
            print(f"\nSummary across {len(scores)} documents:")
            print(f"  Mean LCS: {np.mean(scores):.4f}")
            print(f"  Median LCS: {np.median(scores):.4f}")
            print(f"  Std Dev: {np.std(scores):.4f}")
            print(f"  Min: {np.min(scores):.4f}")
            print(f"  Max: {np.max(scores):.4f}")

        return results


# Usage example
if __name__ == "__main__":
    lcs = LexicalContentScore()

    # For a single document
    pdf_text = "Your PDF-extracted text here..."
    html_text = "Your reference HTML text here..."
    score = lcs.compute_lcs(pdf_text, html_text)
    print(f"LCS Score: {score:.4f}")

    # For batch evaluation
    # results = lcs.batch_evaluate("data_lake/pdfs_converted", "data_lake/html_references")
