from typing import Final, Dict, Any

# Configuration settings for general data operations
DEFAULT_ENCODING: Final[str] = 'utf-8'
CHUNK_SIZE: Final[int] = 1024 * 64

# HTTP status code mappings for data handlers
STATUS_SUCCESS: Final[int] = 200
STATUS_BAD_REQUEST: Final[int] = 400
STATUS_NOT_FOUND: Final[int] = 404
STATUS_SERVER_ERROR: Final[int] = 500

# Common MIME types for data processing
CONTENT_TYPES: Final[Dict[str, str]] = {
    'json': 'application/json',
    'csv': 'text/csv',
    'txt': 'text/plain',
    'xml': 'application/xml'
}

# Logging format constants
LOG_DATE_FORMAT: Final[str] = '%Y-%m-%d %H:%M:%S'
LOG_TEMPLATE: Final[str] = '[%(levelname)s] %(asctime)s - %(message)s'

# Validation constraints for data schemas
MAX_RECURSION_DEPTH: Final[int] = 10
SUPPORTED_VERSIONS: Final[list] = ['v1', 'v2']

def get_default_headers() -> Dict[str, str]:
    """Returns standard header configuration for data requests."""
    return {
        'Content-Type': CONTENT_TYPES['json'],
        'Accept-Encoding': DEFAULT_ENCODING
    }