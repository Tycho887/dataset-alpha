from src.parser import DoclingProcessor
from src.scraper import DocumentScraper
from src.verifier import DatasetVerifier

if __name__ == "__main__":
    # scraper = DocumentScraper()
    # scraper.run()
    processor = DoclingProcessor()
    processor.run()
    verifier = DatasetVerifier(
        jsonl_path="training_data.jsonl", data_lake_path="data_lake"
    )
    verifier.run()
