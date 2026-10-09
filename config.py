import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """Handles loading and retrieval of environment-based configuration settings."""

    def __init__(self, prefix: str = "APP_") -> None:
        """Initialize with an environment variable prefix."""
        self.prefix: str = prefix
        self._settings: Dict[str, Any] = {}

    def load_from_env(self) -> None:
        """Populate settings dictionary from environment variables."""
        for key, value in os.environ.items():
            if key.startswith(self.prefix):
                config_key = key[len(self.prefix):].lower()
                self._settings[config_key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a configuration value with an optional default."""
        return self._settings.get(key, default)

    def get_int(self, key: str, default: int = 0) -> int:
        """Retrieve a configuration value cast to integer."""
        try:
            return int(self._settings.get(key, default))
        except (ValueError, TypeError):
            return default

    def all(self) -> Dict[str, Any]:
        """Return a copy of the full configuration dictionary."""
        return self._settings.copy()