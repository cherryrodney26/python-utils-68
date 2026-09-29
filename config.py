import os
from typing import Any, Dict, Optional

class ConfigManager:
    """Handles application settings from environment variables."""
    def __init__(self, prefix: str = "APP_") -> None:
        self.prefix = prefix
        self._settings: Dict[str, Any] = {}

    def load(self) -> None:
        """Populates settings dictionary from environment."""
        for key, value in os.environ.items():
            if key.startswith(self.prefix):
                clean_key = key[len(self.prefix):].lower()
                self._settings[clean_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a setting by key."""
        return self._settings.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        """Returns all loaded configurations."""
        return self._settings.copy()

# Global instance for project-wide access
config = ConfigManager()
config.load()