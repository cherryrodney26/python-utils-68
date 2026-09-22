import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading configuration from JSON files with fallback defaults."""

    def __init__(self, default_config: Dict[str, Any] = None):
        self._defaults = default_config or {}

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads configuration from a file, merging with default values."""
        config = self._defaults.copy()

        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                config.update(file_data)
        except (json.JSONDecodeError, IOError):
            return config

        return config

    @staticmethod
    def get_env_override(key: str, default: Any = None) -> Any:
        """Retrieves configuration from environment variables."""
        return os.getenv(key.upper(), default)

# Example usage:
# loader = ConfigLoader({"host": "localhost", "port": 8080})
# settings = loader.load("config.json")