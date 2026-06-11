#!/usr/bin/env python3
import argparse
import asyncio
import sqlite3
from lib.db import init_db, DB_PATH
# Updated import
from lib.util import process_and_register_repository, remove_and_cleanup_repository, process_local_directory
from lib.processing import process_files_batch

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Manual Git Repository Ingestion and Removal Utility Interface"
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--add-repo", 
        type=str, 
        metavar="URL",
        help="Git target clone endpoint URL to add/update tracking."
    )
    group.add_argument(
        "--remove-repo", 
        type=str, 
        metavar="URL",
        help="Git target clone endpoint URL to remove from database tracking."
    )
    # New argument added
    group.add_argument(
        "--add-directory", 
        type=str, 
        metavar="PATH",
        help="Local directory path representing a pre-cloned Git repository."
    )
    
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run processing pipeline but only send test.txt to the server."
    )
    
    args = parser.parse_args()
    init_db()

    if args.add_repo:
        print(f"Initiating registration pipeline for: {args.add_repo}")
        discovered_files = process_and_register_repository(args.add_repo)
        
        if discovered_files:
            if args.test:
                print("Test mode active: Bypassing standard payload and queueing test.txt.")
                discovered_files = ["test.txt"]
            asyncio.run(process_files_batch(discovered_files))
        else:
            print("No valid files found to process during ingestion.")

    # New execution block
    elif args.add_directory:
        print(f"Initiating registration pipeline for local directory: {args.add_directory}")
        discovered_files = process_local_directory(args.add_directory)
        
        if discovered_files:
            if args.test:
                print("Test mode active: Bypassing standard payload and queueing test.txt.")
                discovered_files = ["test.txt"]
            asyncio.run(process_files_batch(discovered_files))
        else:
            print("No valid files found to process during local directory ingestion.")
            
    elif args.remove_repo:
        # Existing removal logic remains unchanged...
        print(f"Initiating removal pipeline for: {args.remove_repo}")
        
        files_to_delete = []
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT file_path FROM tracked_files WHERE repo_url = ?", 
                (args.remove_repo,)
            )
            for row in cursor.fetchall():
                files_to_delete.append({
                    "repo_url": args.remove_repo,
                    "file_path": row[0],
                    "status": "deleted"
                })

        if files_to_delete:
            print(f"Purging {len(files_to_delete)} files from the LightRAG server...")
            asyncio.run(process_files_batch(files_to_delete))
        else:
            print("No active documents found in the vector database to purge.")

        remove_and_cleanup_repository(args.remove_repo)

if __name__ == "__main__":
    main()