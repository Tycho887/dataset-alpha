"""
Batch Orchestrator
==================
Ties the Source Manager to the Knowledge Distillation Pipeline.
Processes 100+ sources individually, each with its own output directory.
"""

import asyncio
import logging
import sys
from pathlib import Path
from typing import List, Optional
import dotenv

dotenv.load_dotenv()

from source_manager import SourceRegistry, SourceDownloader, Source

# Import the pipeline from the previous module
# Assumes pipeline.py is in the same directory
from pipeline import PipelineOrchestrator, PipelineConfig

logger = logging.getLogger("BatchOrchestrator")


class BatchOrchestrator:
    """
    Orchestrates the full end-to-end pipeline across multiple sources.
    Each source gets its own isolated output directory.
    """

    def __init__(
        self,
        registry_path: str = "source_registry.json",
        data_lake_root: str = "./data_lake",
        pipeline_output_root: str = "./pipeline_output",
        max_concurrent_downloads: int = 5,
        llm_concurrent_requests: int = 8,
        request_delay: float = 1.0
    ):
        self.registry = SourceRegistry(registry_path)
        self.data_lake_root = Path(data_lake_root)
        self.output_root = Path(pipeline_output_root)
        self.output_root.mkdir(parents=True, exist_ok=True)

        self.downloader = SourceDownloader(
            data_lake_root=data_lake_root,
            max_concurrent_downloads=max_concurrent_downloads,
            request_delay=request_delay
        )

        self.llm_concurrent = llm_concurrent_requests

    async def run_all(self, source_ids: Optional[List[str]] = None):
        """
        Process all pending sources, or specific ones if source_ids provided.

        Args:
            source_ids: If provided, only process these specific source IDs.
                       Overrides normal pending logic (but still respects force_reprocess).
        """
        if source_ids:
            sources = [self.registry.get_by_id(sid) for sid in source_ids]
            sources = [s for s in sources if s is not None]
            logger.info(f"Running {len(sources)} explicitly specified sources")
        else:
            sources = self.registry.get_pending()

        if not sources:
            logger.info("No sources to process.")
            self._print_summary()
            return

        logger.info("=" * 70)
        logger.info(f"BATCH PROCESSING: {len(sources)} sources")
        logger.info("=" * 70)

        async with self.downloader:
            for idx, source in enumerate(sources, 1):
                logger.info(f"\n[{idx}/{len(sources)}] Processing: {source.name}")
                logger.info(f"    URL: {source.url}")
                logger.info(f"    Type: {source.type} | Category: {source.category}")

                try:
                    await self._process_source(source)
                except Exception as e:
                    logger.error(f"    ✗ FAILED: {e}")
                    self.registry.mark_processed(source.id, success=False, error=str(e))
                    # Continue to next source — do not stop the batch

        self._print_summary()

    async def _process_source(self, source: Source):
        """Process a single source end-to-end."""

        # Step 1: Download
        source_dir = await self.downloader.download(source)

        # Step 2: Prepare source-specific output directory
        safe_name = SourceDownloader.sanitize_name(source.name)
        source_output = self.output_root / safe_name
        source_output.mkdir(parents=True, exist_ok=True)

        # If force_reprocess, clean old outputs
        if source.force_reprocess and source_output.exists():
            logger.info(f"    force_reprocess=True, clearing old outputs: {source_output}")
            import shutil
            for item in source_output.iterdir():
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()

        logger.info(f"    Output directory: {source_output}")

        # Step 3: Configure and run pipeline
        config = PipelineConfig(
            target_dir=str(source_dir),
            output_dir=str(source_output),

            # Model selections (tune as needed)
            classifier_model="cross-encoder/nli-deberta-v3-base",
            embedder_model="BAAI/bge-base-en-v1.5",

            # Thresholds
            classifier_threshold=0.70,
            importance_threshold=0.65,
            dedup_threshold=0.92,

            # LLM settings
            llm_api_key="",  # Will read from DEEPSEEK_API_KEY env var
            llm_model="deepseek-chat",
            llm_concurrent_requests=self.llm_concurrent,
            llm_temperature=0.1,

            # Enable all stages
            enable_heuristic_filter=True,
            enable_zero_shot_filter=True,
            enable_data_cleaning=True,
            enable_smart_chunking=True,
            enable_deduplication=True,
            enable_importance_scoring=True,
            enable_dual_processing=True,
            enable_quality_filter=True,
        )

        pipeline = PipelineOrchestrator(config)
        await pipeline.run()

        # Step 4: Mark success
        self.registry.mark_processed(source.id, success=True)
        logger.info(f"    ✓ SUCCESS: {source.name}")

    def _print_summary(self):
        """Print final batch summary."""
        summary = self.registry.get_summary()

        print("\n" + "=" * 70)
        print("BATCH SUMMARY")
        print("=" * 70)
        print(f"  Total sources:     {summary['total']}")
        print(f"  Processed:         {summary['processed']}")
        print(f"  Failed:            {summary['failed']}")
        print(f"  Pending:           {summary['pending']}")
        print("=" * 70)

        if summary["failed"] > 0:
            print("\nFailed sources:")
            for s in self.registry.sources:
                if s.status == "failed":
                    print(f"  - {s.name}: {s.error}")

        print(f"\nOutput root: {self.output_root.absolute()}")
        print("=" * 70)


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="EU Digital Software Knowledge Distillation Batch Orchestrator"
    )
    parser.add_argument(
        "--registry", "-r",
        default="source_registry.json",
        help="Path to source registry JSON file"
    )
    parser.add_argument(
        "--data-lake", "-d",
        default="./data_lake",
        help="Root directory for downloaded source content"
    )
    parser.add_argument(
        "--output", "-o",
        default="./pipeline_output",
        help="Root directory for pipeline outputs"
    )
    parser.add_argument(
        "--source-ids", "-s",
        nargs="+",
        help="Process only specific source IDs (space-separated)"
    )
    parser.add_argument(
        "--download-concurrency",
        type=int,
        default=5,
        help="Max concurrent downloads (default: 5)"
    )
    parser.add_argument(
        "--llm-concurrency",
        type=int,
        default=8,
        help="Max concurrent LLM API calls per source (default: 8)"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay between HTTP requests in seconds (default: 1.0)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)-8s | %(name)-25s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("orchestrator.log", encoding="utf-8")
        ]
    )

    # Run orchestrator
    orchestrator = BatchOrchestrator(
        registry_path=args.registry,
        data_lake_root=args.data_lake,
        pipeline_output_root=args.output,
        max_concurrent_downloads=args.download_concurrency,
        llm_concurrent_requests=args.llm_concurrency,
        request_delay=args.delay
    )

    asyncio.run(orchestrator.run_all(source_ids=args.source_ids))


if __name__ == "__main__":
    main()
