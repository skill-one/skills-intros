"""Logging configuration."""

import logging
import sys


def setup_logging(verbose: bool = False) -> None:
    """Configure logging: INFO by default, DEBUG with --verbose."""
    level = logging.DEBUG if verbose else logging.INFO
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logging.basicConfig(level=level, handlers=[handler], force=True)
    logging.getLogger("httpx").setLevel(logging.WARNING)
