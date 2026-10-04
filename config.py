import os
import json
from typing import Any, Dict, Optional


class ConfigurationManager:
    """Centralized manager for loading and retrieving application settings."""

    def __init__(self, default_config: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = default_config.copy() if default_config else {}

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Populate configuration from environment variables matching a prefix."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                self._config[clean_key] = self._parse_value(value)

    def load_from_json(self, filepath: str) -> None:
        """Load and merge configuration options from a JSON file."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Configuration file not found: {filepath}")
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict):
                self._config.update(data)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key with an optional default."""
        return self._config.get(key.lower(), default)

    def set(self, key: str, value: Any) -> None:
        """Set a specific configuration key and value."""
        self._config[key.lower()] = value

    def as_dict(self) -> Dict[str, Any]:
        """Return a copy of the active configuration dictionary."""
        return self._config.copy()

    @staticmethod
    def _parse_value(val: str) -> Any:
        """Attempt to parse string values into boolean, integer, or float types."""
        val_lower = val.lower()
        if val_lower in ("true", "1", "yes"):
            return True
        if val_lower in ("false", "0", "no"):
            return False
        try:
            return int(val)
        except ValueError:
            pass
        try:
            return float(val)
        except ValueError:
            pass
        return val
