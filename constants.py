import enum
from typing import Final, Dict, Any

# general status codes for data operations
class DataStatus(enum.IntEnum):
    SUCCESS = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500

# default processing configurations
DEFAULT_CHUNK_SIZE: Final[int] = 1024
DEFAULT_TIMEOUT: Final[float] = 30.0
MAX_RETRIES: Final[int] = 3

# registry for supported data types
SUPPORTED_MIME_TYPES: Final[Dict[str, str]] = {
    'json': 'application/json',
    'csv': 'text/csv',
    'xml': 'application/xml'
}

def get_error_message(status_code: int) -> str:
    """maps status codes to human-readable strings"""
    messages = {
        DataStatus.SUCCESS: "operation completed successfully",
        DataStatus.BAD_REQUEST: "invalid data structure provided",
        DataStatus.NOT_FOUND: "requested resource does not exist",
        DataStatus.SERVER_ERROR: "internal processing failure"
    }
    return messages.get(status_code, "unknown error occurred")

# environmental constraint markers
IS_DEBUG_MODE: Final[bool] = False
VERSION_INFO: Final[str] = "1.0.0"