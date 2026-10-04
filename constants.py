import os

# Application default settings and constants

APP_NAME = "python-utils-68"
VERSION = "1.0.0"

# Directory and Path defaults
DEFAULT_LOG_DIR = os.getenv("LOG_DIR", "logs")
DEFAULT_TEMP_DIR = os.getenv("TEMP_DIR", "/tmp/utils_cache")

# Validation thresholds
MAX_RETRY_ATTEMPTS = 3
TIMEOUT_SECONDS = 30

# Common status codes
STATUS_SUCCESS = 0
STATUS_FAILURE = 1
STATUS_WARNING = 2

# File handling configurations
ALLOWED_EXTENSIONS = {".txt", ".json", ".csv", ".yaml"}
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10MB limit

# Time formatting
ISO_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
DEFAULT_ENCODING = "utf-8"

# Environment checks
IS_PRODUCTION = os.getenv("ENV", "development").lower() == "production"