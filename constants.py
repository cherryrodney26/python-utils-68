import os
import logging
from typing import Final

# Application-wide configuration defaults and constants

APP_NAME: Final[str] = "python-utils-68"
VERSION: Final[str] = "1.0.0"

# Logging configuration constants
LOG_FORMAT: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL: Final[int] = logging.INFO

# Time and timeout defaults in seconds
DEFAULT_TIMEOUT: Final[float] = 30.0
RETRY_ATTEMPTS: Final[int] = 3
BACKOFF_FACTOR: Final[float] = 1.5

# Environment-based paths with fallback
DATA_DIR: Final[str] = os.getenv("DATA_DIR", "./data")
CACHE_DIR: Final[str] = os.getenv("CACHE_DIR", "./cache")

# Content type and encoding standards
DEFAULT_ENCODING: Final[str] = "utf-8"
JSON_MIME_TYPE: Final[str] = "application/json"

# Validator thresholds
MIN_PASSWORD_LENGTH: Final[int] = 12
MAX_RETRIES_LIMIT: Final[int] = 10

def get_app_metadata() -> dict:
    """Return common application metadata dictionary."""
    return {
        "app": APP_NAME,
        "version": VERSION,
        "default_encoding": DEFAULT_ENCODING
    }