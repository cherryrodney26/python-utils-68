from typing import Final, Dict, Any

# Configuration settings for system components
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Standard HTTP status mapping for internal services
STATUS_CODES: Final[Dict[str, int]] = {
    "SUCCESS": 200,
    "CREATED": 201,
    "BAD_REQUEST": 400,
    "UNAUTHORIZED": 401,
    "NOT_FOUND": 404,
    "SERVER_ERROR": 500
}

# Global application configuration defaults
APP_CONFIG: Final[Dict[str, Any]] = {
    "version": "1.0.0",
    "environment": "production",
    "debug_mode": False
}

def get_status_message(code: int) -> str:
    """Return a descriptive message for a given status code."""
    mapping: Dict[int, str] = {v: k for k, v in STATUS_CODES.items()}
    return mapping.get(code, "UNKNOWN_STATUS")

class AppConstants:
    """Container for application-wide immutable settings."""
    def __init__(self) -> None:
        self.timeout: int = DEFAULT_TIMEOUT
        self.retries: int = MAX_RETRIES