import os

class AppConstants:
    """
    Centralized application constants with robust retrieval.
    """
    
    MAX_RETRIES = 5
    TIMEOUT_DEFAULT = 30
    ENV_VAR_PREFIX = "PYUTILS_"

    @classmethod
    def get_setting(cls, key: str, default=None):
        """
        Safe lookup for environment configuration settings.
        Returns default if key is missing or invalid.
        """
        if not isinstance(key, str) or not key:
            return default

        full_key = f"{cls.ENV_VAR_PREFIX}{key.upper()}"
        value = os.environ.get(full_key)

        if value is None:
            return default

        try:
            # Handle basic type casting based on common patterns
            if value.lower() in ("true", "false"):
                return value.lower() == "true"
            if value.isdigit():
                return int(value)
            return value
        except (ValueError, TypeError):
            return default

# Pre-initialized constants for core system operations
MIN_BUFFER_SIZE = 1024
MAX_BUFFER_SIZE = 1024 * 1024 * 64
SUPPORTED_EXTENSIONS = {'.json', '.yaml', '.txt'}

# Exit codes mapping for consistent error handling
EXIT_SUCCESS = 0
EXIT_FAILURE_GENERAL = 1
EXIT_FAILURE_CONFIG = 2
EXIT_FAILURE_TIMEOUT = 3