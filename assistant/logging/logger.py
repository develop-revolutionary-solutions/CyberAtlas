"""

## Responsibilities

This module should:

Create the logs/ directory if it doesn't exist.
Configure console logging.
Configure file logging.
Prevent duplicate handlers.
Return a logger for any module.
Hide all logging complexity from the rest of the application.

## It should not:

Know anything about the CLI.
Know anything about nmap, ffuf, AI, or plugins.
Perform business logic.

This keeps the module focused on one responsibility.

### What We'll Build

We'll expose exactly one public function:

get_logger(name: str) -> logging.Logger

Any future module will use it like this:

from assistant.logging.logger import get_logger

logger = get_logger(__name__)

That's the only API other parts of CyberAtlas need to know.

"""



from __future__ import annotations

import logging
from pathlib import Path

# Application-wide logger configuration
_LOGGER_NAME = "cyberatlas"
_LOG_FILE = Path("logs") / "cyberatlas.log"

# Ensure the logs directory exists
_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# Configure the application logger only once
_app_logger = logging.getLogger(_LOGGER_NAME)

if not _app_logger.handlers:
    _app_logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File output
    file_handler = logging.FileHandler(_LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    _app_logger.addHandler(console_handler)
    _app_logger.addHandler(file_handler)

    # Prevent duplicate messages from propagating to the root logger
    _app_logger.propagate = False


def get_logger(name: str) -> logging.Logger:
    """
    Return a child logger of the CyberAtlas application logger.

    Example:
        logger = get_logger(__name__)
    """
    return _app_logger.getChild(name)
