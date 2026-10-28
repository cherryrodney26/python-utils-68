"""Centralized constants and default settings for python-utils-68."""

import os
from enum import Enum
from typing import Final


class Environment(str, Enum):
    """Supported execution environments."""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


class LogLevel(str, Enum):
    """Standard log severity levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


# System Defaults
DEFAULT_ENV: Final[Environment] = Environment(
    os.getenv("APP_ENV", Environment.DEVELOPMENT.value)
)
DEFAULT_LOG_LEVEL: Final[LogLevel] = LogLevel(
    os.getenv("LOG_LEVEL", LogLevel.INFO.value)
)
DEFAULT_TIMEOUT: Final[int] = int(os.getenv("DEFAULT_TIMEOUT", "30"))
DEFAULT_MAX_RETRIES: Final[int] = int(os.getenv("MAX_RETRIES", "3"))

# Buffer and I/O Constants
DEFAULT_BUFFER_SIZE: Final[int] = 8192
DEFAULT_ENCODING: Final[str] = "utf-8"

# Date and Time Formats
ISO_DATETIME_FORMAT: Final[str] = "%Y-%m-%dT%H:%M:%S%z"
DATE_FORMAT_YYYY_MM_DD: Final[str] = "%Y-%m-%d"


def get_constant_by_name(name: str, default: str | None = None) -> str | None:
    """Safe lookup for global constants by string name."""
    val = globals().get(name, default)
    return str(val) if val is not None else None
