from typing import Final, Dict, List

# Configuration settings for system components
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 5

# Standard HTTP status mapping
STATUS_CODES: Final[Dict[int, str]] = {
    200: "OK",
    400: "BAD_REQUEST",
    404: "NOT_FOUND",
    500: "INTERNAL_SERVER_ERROR"
}

# Default supported file extensions
SUPPORTED_EXTENSIONS: Final[List[str]] = [".json", ".yaml", ".yml", ".toml"]

class AppConstants:
    """Container class for static application constants."""

    VERSION: Final[str] = "1.0.0"
    ENV_PROD: Final[str] = "production"
    ENV_DEV: Final[str] = "development"

    @classmethod
    def get_supported_formats(cls) -> List[str]:
        """Return list of supported file formats."""
        return SUPPORTED_EXTENSIONS

    @classmethod
    def is_success(cls, code: int) -> bool:
        """Check if the provided status code indicates success."""
        return code == 200