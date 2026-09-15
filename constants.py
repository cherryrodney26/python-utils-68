import os
import re

# Standard environmental configurations
DEFAULT_ENCODING = "utf-8"
MAX_RETRY_ATTEMPTS = 3
TIMEOUT_SECONDS = 30

# Common validation patterns
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Default file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
TEMP_DIR = os.path.join(BASE_DIR, "tmp")

# HTTP response codes for application logic
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_NOT_FOUND = 404
HTTP_SERVER_ERROR = 500

# System limits
BUFFER_SIZE = 1024 * 64
CHUNK_SIZE = 1024 * 1024

def get_app_constants():
    """Returns a dictionary of all defined application constants."""
    return {
        "encoding": DEFAULT_ENCODING,
        "retries": MAX_RETRY_ATTEMPTS,
        "timeout": TIMEOUT_SECONDS,
        "log_dir": LOG_DIR
    }