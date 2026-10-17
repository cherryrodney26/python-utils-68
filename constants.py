import os
from pathlib import Path

# Global paths for file system operations
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

# Ensure default directories exist
for directory in [DATA_DIR, LOG_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Environment configuration constants
DEFAULT_ENCODING = "utf-8"
TIMEOUT_SECONDS = 30
MAX_RETRIES = 3

# Common regex patterns
EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# Default headers for API interactions
DEFAULT_HEADERS = {
    "User-Agent": "python-utils-68-agent/1.0",
    "Content-Type": "application/json"
}

def get_env_variable(key: str, default: str = None) -> str:
    """Retrieve environment variable with fallback value."""
    return os.getenv(key, default)

# System status codes
STATUS_OK = 200
STATUS_CREATED = 201
STATUS_BAD_REQUEST = 400
STATUS_NOT_FOUND = 404
STATUS_SERVER_ERROR = 500