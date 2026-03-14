# scraper.py
import hashlib
import json
import os
import time
from datetime import datetime
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup
from git import Repo


class DocumentScraper:
    def __init__(self, config_path="sources.yaml", data_dir="data_lake"):
        with open(config_path, "r") as f:
            self.sources = yaml.safe_load(f)["sources"]
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)

    def download_html(self, source):
        """Download and parse HTML content."""
        print(f"Downloading HTML: {source['name']}")
        response = requests.get(source["url"], headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Try to extract main content (often in <main>, <article>, or specific divs)
        main_content = (
            soup.find("main")
            or soup.find("article")
            or soup.find("div", class_="content")
        )
        if main_content:
            text_content = main_content.get_text(separator="\n", strip=True)
        else:
            text_content = soup.get_text(separator="\n", strip=True)

        # Save both raw HTML and clean text
        source_dir = self.data_dir / source["name"]
        source_dir.mkdir(exist_ok=True)

        with open(
            source_dir
            / f"{source['name']}_{source.get('version_date', 'latest')}.html",
            "w",
        ) as f:
            f.write(response.text)

        with open(
            source_dir / f"{source['name']}_{source.get('version_date', 'latest')}.txt",
            "w",
        ) as f:
            f.write(text_content)

        # Save metadata
        self.save_metadata(source, source_dir)

    def clone_repository(self, source):
        """Clone or update a git repository."""
        print(f"Cloning repository: {source['name']}")
        source_dir = self.data_dir / source["name"]

        if source_dir.exists():
            # Pull latest changes if repo exists
            repo = Repo(source_dir)
            origin = repo.remotes.origin
            origin.pull()
        else:
            # Clone new repo
            repo = Repo.clone_from(
                source["repo_url"], source_dir, branch=source.get("branch", "main")
            )

        # Get commit hash for versioning
        commit_hash = repo.head.commit.hexsha

        # Save metadata
        self.save_metadata(source, source_dir, extra_info={"commit_hash": commit_hash})

    def download_pdf(self, source):
        """Download PDF file."""
        print(f"Downloading PDF: {source['name']}")
        response = requests.get(source["url"], stream=True)
        response.raise_for_status()

        source_dir = self.data_dir / source["name"]
        source_dir.mkdir(exist_ok=True)

        pdf_path = (
            source_dir / f"{source['name']}_{source.get('version_date', 'latest')}.pdf"
        )
        with open(pdf_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        self.save_metadata(source, source_dir)

    def save_metadata(self, source, source_dir, extra_info=None):
        """Save metadata about the downloaded document."""
        metadata = {
            "name": source["name"],
            "type": source["type"],
            "url": source.get("url", source.get("repo_url")),
            "download_date": datetime.now().isoformat(),
            "stability": source["stability"],
            "version_date": source.get("version_date", "unknown"),
            "original_source": source,
        }
        if extra_info:
            metadata.update(extra_info)

        with open(source_dir / "metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)

    def run(self):
        """Execute scraping for all sources."""
        for source in self.sources:
            try:
                if source["type"] == "html":
                    self.download_html(source)
                elif source["type"] == "github":
                    self.clone_repository(source)
                elif source["type"] == "pdf":
                    self.download_pdf(source)
                else:
                    print(f"Unknown source type: {source['type']}")

                # Be polite to servers
                time.sleep(2)

            except Exception as e:
                print(f"Error processing {source['name']}: {e}")


if __name__ == "__main__":
    scraper = DocumentScraper()
    scraper.run()
