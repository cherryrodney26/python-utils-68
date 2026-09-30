import os
from typing import Dict, Any, Optional

class ConfigManager:
    """Handles application settings from environment variables."""

    def __init__(self, prefix: str = "APP_") -> None:
        self.prefix = prefix
        self._settings: Dict[str, Any] = {}
        self._load_from_env()

    def _load_from_env(self) -> None:
        """Loads variables prefixed with the defined APP_ prefix."""
        for key, value in os.environ.items():
            if key.startswith(self.prefix):
                clean_key = key[len(self.prefix):].lower()
                self._settings[clean_key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a setting by key with a fallback default."""
        return self._settings.get(key, default)

    def get_int(self, key: str, default: int = 0) -> int:
        """Retrieves a setting as an integer."""
        try:
            return int(self.get(key, default))
        except (ValueError, TypeError):
            return default

    def all(self) -> Dict[str, Any]:
        """Returns all loaded configuration settings."""
        return self._settings.copy()

def get_config() -> ConfigManager:
    """Returns a singleton-like instance of the ConfigManager."""
    if not hasattr(get_config, "_instance"):
        get_config._instance = ConfigManager()
    return get_config._instance