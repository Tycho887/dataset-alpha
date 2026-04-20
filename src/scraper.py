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
from dotenv import load_dotenv
from git import Repo

load_dotenv()


class DocumentScraper:
    def __init__(self, config_path="sources.yaml", data_dir="data_lake"):
        with open(config_path, "r") as f:
            self.sources = yaml.safe_load(f)["sources"]
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.github_token = os.environ.get("github_api_key")

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

    def fetch_org_repositories(
        self, org_name: str, include_forks=False, include_archived=False
    ):
        """Fetch all repositories from a GitHub organization using the API."""
        repos = []
        page = 1
        per_page = 100  # Max per page

        print(f"Fetching repositories for organization: {org_name}")

        while True:
            url = f"https://api.github.com/orgs/{org_name}/repos"
            params = {
                "page": page,
                "per_page": per_page,
                "sort": "updated",
                "direction": "desc",
            }

            # Add authentication if you have a token (to avoid rate limits)
            headers = {}
            if hasattr(self, "github_token") and self.github_token:
                headers["Authorization"] = f"token {self.github_token}"

            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()

            page_repos = response.json()
            if not page_repos:
                break

            for repo in page_repos:
                # Apply filters
                if not include_forks and repo["fork"]:
                    continue
                if not include_archived and repo["archived"]:
                    continue

                repos.append(
                    {
                        "name": repo["name"],
                        "full_name": repo["full_name"],
                        "clone_url": repo["clone_url"],
                        "default_branch": repo["default_branch"],
                        "description": repo["description"],
                        "language": repo["language"],
                        "updated_at": repo["updated_at"],
                        "size": repo["size"],
                    }
                )

            print(f"  Fetched page {page}, {len(page_repos)} repos")
            page += 1
            time.sleep(0.5)  # Be polite to GitHub API

        print(f"Total repositories found: {len(repos)}")
        return repos

    def process_github_org(self, source):
        """Process all repositories in a GitHub organization."""
        org_name = source["org_name"]

        # Fetch all repos
        repos = self.fetch_org_repositories(
            org_name,
            include_forks=source.get("include_forks", False),
            include_archived=source.get("include_archived", False),
        )

        # Apply language filters if specified
        language_filters = source.get("language_filters", [])
        if language_filters:
            filtered_repos = [r for r in repos if r["language"] in language_filters]
            print(
                f"After language filter {language_filters}: {len(filtered_repos)} repos"
            )
            repos = filtered_repos

        # Create a parent directory for the organization
        org_dir = self.data_dir / org_name
        org_dir.mkdir(exist_ok=True)

        # Save the list of repositories as metadata
        with open(org_dir / "repositories.json", "w") as f:
            json.dump(repos, f, indent=2)

        # Process each repository
        for repo_info in repos:
            # Create a source entry for this specific repo
            repo_source = {
                "name": f"{org_name}_{repo_info['name']}",
                "type": "github",
                "repo_url": repo_info["clone_url"],
                "branch": repo_info["default_branch"],
                "stability": source["stability"],
                "file_pattern": source.get("extract", ["*.md", "*.txt"]),
                "parent_org": org_name,
            }

            # Clone or update this repository
            print(f"\nProcessing repository: {repo_info['name']}")
            self.clone_repository(repo_source)

            # Add org metadata to the repo's metadata.json
            repo_dir = self.data_dir / repo_source["name"]
            metadata_path = repo_dir / "metadata.json"
            if metadata_path.exists():
                with open(metadata_path, "r") as f:
                    metadata = json.load(f)
                metadata["org_name"] = org_name
                metadata["github_api_data"] = {
                    "description": repo_info["description"],
                    "language": repo_info["language"],
                    "updated_at": repo_info["updated_at"],
                    "size_kb": repo_info["size"],
                }
                with open(metadata_path, "w") as f:
                    json.dump(metadata, f, indent=2)

    def scrape_etsi_work_items(self, tb_id="607;ESI"):
        """Scrape ETSI work program portal for all published/active work items."""
        base_url = "https://portal.etsi.org/webapp/WorkProgram/Frame_WorkItemList.asp"
        headers = {"User-Agent": "Mozilla/5.0 (compatible; EUDI-Dataset/1.0)"}
        query_string = (
            f"?qSORT=HIGHVERSION&qETSI_ALL=&SearchPage=TRUE"
            f"&qTB_ID={requests.utils.quote(tb_id, safe='')}"
            f"&qINCLUDE_SUB_TB=True&qINCLUDE_MOVED_ON=&qSTOP_FLG="
            f"&qKEYWORD_BOOLEAN=&qCLUSTER_BOOLEAN=&qFREQUENCIES_BOOLEAN="
            f"&qSTOPPING_OUTDATED=&butSimple=Search&includeNonActiveTB=FALSE"
            f"&includeSubProjectCode=&qREPORT_TYPE=SUMMARY"
        )
        url = base_url + query_string

        work_items = []
        offset = 0

        while True:
            data = {"qOFFSET": str(offset), "qNB_TO_DISPLAY": "100"}
            if offset > 0:
                data["SubmitNext"] = " Next Page "

            response = requests.post(url, data=data, headers=headers, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            rows = soup.select("table tr")

            page_items = []
            for row in rows:
                cells = row.find_all("td")
                if len(cells) < 4:
                    continue

                # Cell 1: ETSI number as a bold link + detail URL
                doc_cell = cells[1]
                link = doc_cell.find("a", href=True)
                if not link:
                    continue

                etsi_number = link.get_text(strip=True)
                if not etsi_number:
                    continue

                href = link["href"]
                detail_url = (
                    href if href.startswith("http")
                    else "https://portal.etsi.org" + href
                )

                page_items.append({
                    "etsi_number": etsi_number,
                    "title": cells[2].get_text(strip=True),
                    "status": cells[3].get_text(strip=True),
                    "detail_url": detail_url,
                })

            if not page_items:
                break

            work_items.extend(page_items)
            print(f"  Scraped {len(work_items)} work items so far...")
            offset += 100
            time.sleep(1)

        return work_items

    def find_etsi_download_url(self, detail_url):
        """Fetch an ETSI work item detail page and return the PDF download URL."""
        headers = {"User-Agent": "Mozilla/5.0 (compatible; EUDI-Dataset/1.0)"}
        response = requests.get(detail_url, headers=headers, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            href = link["href"]
            if any(domain in href for domain in ("www.etsi.org/deliver/", "pda.etsi.org")):
                if href.lower().endswith((".pdf", ".zip")):
                    return href if href.startswith("http") else "https:" + href
        return None

    def process_etsi_portal(self, source):
        """Scrape ETSI portal and download all specs as PDFs."""
        tb_id = source.get("tb_id", "607;ESI")
        print(f"Scraping ETSI portal for TB: {tb_id}")

        source_dir = self.data_dir / source["name"]
        source_dir.mkdir(exist_ok=True)

        work_items = self.scrape_etsi_work_items(tb_id)

        spec_filter = source.get("spec_filter", [])
        if spec_filter:
            work_items = [
                item for item in work_items
                if any(s in item["etsi_number"] for s in spec_filter)
            ]

        print(f"Found {len(work_items)} work items to process")

        with open(source_dir / "work_items.json", "w") as f:
            json.dump(work_items, f, indent=2)

        downloaded, failed = [], []

        for item in work_items:
            safe_name = item["etsi_number"].replace(" ", "_").replace("/", "-")
            pdf_path = source_dir / f"{safe_name}.pdf"

            if pdf_path.exists():
                print(f"  Skipping (exists): {item['etsi_number']}")
                downloaded.append(item)
                continue

            try:
                download_url = self.find_etsi_download_url(item["detail_url"])
                if not download_url:
                    print(f"  No download URL: {item['etsi_number']}")
                    failed.append({**item, "reason": "no_download_url"})
                    continue

                response = requests.get(
                    download_url,
                    headers={"User-Agent": "Mozilla/5.0 (compatible; EUDI-Dataset/1.0)"},
                    stream=True,
                    timeout=60,
                )
                response.raise_for_status()

                with open(pdf_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                item["download_url"] = download_url
                downloaded.append(item)
                print(f"  Downloaded: {item['etsi_number']}")
                time.sleep(1)

            except Exception as e:
                print(f"  Failed {item['etsi_number']}: {e}")
                failed.append({**item, "reason": str(e)})

        self.save_metadata(source, source_dir, extra_info={
            "tb_id": tb_id,
            "total": len(work_items),
            "downloaded": len(downloaded),
            "failed": len(failed),
            "failed_items": failed,
        })
        print(f"ETSI complete: {len(downloaded)} downloaded, {len(failed)} failed")

    def run(self):
        """Execute scraping for all sources (updated to handle github_org)."""
        for source in self.sources:
            try:
                print(f"\n=== Processing source: {source['name']} ===")

                if source["type"] == "html":
                    self.download_html(source)
                elif source["type"] == "github":
                    self.clone_repository(source)
                elif source["type"] == "github_org":
                    self.process_github_org(source)
                elif source["type"] == "pdf":
                    self.download_pdf(source)
                elif source["type"] == "etsi_portal":
                    self.process_etsi_portal(source)
                else:
                    print(f"Unknown source type: {source['type']}")

                # Be polite to servers
                time.sleep(2)

            except Exception as e:
                print(f"Error processing {source['name']}: {e}")
                import traceback

                traceback.print_exc()


if __name__ == "__main__":
    scraper = DocumentScraper()
    scraper.run()
