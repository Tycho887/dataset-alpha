# docling_processor.py
import hashlib
import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import OcrOptions, PdfPipelineOptions
from docling.document_converter import DocumentConverter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DoclingProcessor:
    def __init__(self, data_dir="data_lake", output_file="training_data.jsonl"):
        self.data_dir = Path(data_dir)
        self.output_file = output_file
        # Initialize the Docling converter
        self.converter = DocumentConverter()

        # Optional: Configure for better table and OCR handling
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = True
        pipeline_options.ocr_options = OcrOptions(
            lang=["en"],  # Add languages as needed, e.g., 'fr', 'de'
            force_full_page_ocr=True,
        )
        # For documents with complex structure, you might want to use a specific backend
        # self.converter = DocumentConverter(backend=PyPdfiumDocumentBackend)

    def process_document(
        self, file_path: Path, metadata: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """Process a single document with Docling and return a structured example."""
        logger.info(f"Processing: {file_path}")
        try:
            # Convert the document
            result = self.converter.convert(str(file_path))

            # Access the structured document
            doc = result.document

            # Export to different formats
            markdown_content = doc.export_to_markdown()
            # json_content = doc.export_to_dict()  # For lossless structured data if needed

            # Create a unique ID based on content
            content_hash = hashlib.sha256(markdown_content.encode()).hexdigest()[:16]

            page_count_attr = getattr(doc, "num_pages", None)
            if callable(page_count_attr):
                page_count = page_count_attr()
            else:
                page_count = page_count_attr

            # Structure for fine-tuning (JSONL format)
            example = {
                "id": f"{metadata['name']}_{file_path.stem}_{content_hash}",
                "document_name": metadata["name"],
                "stability": metadata["stability"],
                "version_date": metadata.get("version_date", "unknown"),
                "download_date": metadata.get("download_date"),
                "source_url": metadata.get("url", metadata.get("repo_url")),
                "content": markdown_content,
                "content_length": len(markdown_content),
                "processing_pipeline": "docling_v2.4+",
                "metadata": {  # Preserve original metadata
                    "file_name": file_path.name,
                    "page_count": page_count,
                },
            }
            return example

        except Exception as e:
            logger.error(f"Error processing {file_path} with Docling: {e}")
            return None

    def run(self):
        """Walk through the data lake and process all supported files."""
        with open(self.output_file, "w", encoding="utf-8") as out_f:
            for source_dir in self.data_dir.iterdir():
                if not source_dir.is_dir():
                    continue

                metadata_path = source_dir / "metadata.json"
                if not metadata_path.exists():
                    logger.warning(f"No metadata found in {source_dir}, skipping.")
                    continue

                with open(metadata_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)

                # Process all files in the source directory
                for file_path in source_dir.glob("*"):
                    if file_path.name in ["metadata.json"] or file_path.suffix in [
                        ".json"
                    ]:
                        continue

                    # Docling handles many formats automatically [citation:10]
                    if file_path.suffix.lower() in [
                        ".pdf",
                        ".html",
                        ".htm",
                        ".docx",
                        ".pptx",
                        ".xlsx",
                        ".txt",
                        ".md",
                    ]:
                        example = self.process_document(file_path, metadata)
                        if example:
                            out_f.write(json.dumps(example, ensure_ascii=False) + "\n")
                            out_f.flush()  # Ensure data is written incrementally


if __name__ == "__main__":
    processor = DoclingProcessor()
    processor.run()
