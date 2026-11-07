import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """Handles loading and merging of application configuration."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        """Initialize with optional default settings."""
        self._config: Dict[str, Any] = defaults or {}

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Update configuration from environment variables with matching prefix."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                self._config[clean_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def update(self, new_data: Dict[str, Any]) -> None:
        """Merge new configuration data into current settings."""
        self._config.update(new_data)

    def all(self) -> Dict[str, Any]:
        """Return the full configuration dictionary."""
        return self._config.copy()