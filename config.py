import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Handles loading configuration options with fallback defaults."""

    def __init__(self, default_config: Optional[Dict[str, Any]] = None) -> None:
        self.defaults = default_config or {}

    def _deep_merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively merges override dictionary into base dictionary."""
        result = base.copy()
        for key, value in override.items():
            if (
                key in result
                and isinstance(result[key], dict)
                and isinstance(value, dict)
            ):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        return result

    def load_from_dict(self, user_config: Dict[str, Any]) -> Dict[str, Any]:
        """Merges provided user configuration with default values."""
        return self._deep_merge(self.defaults, user_config)

    def load_from_file(self, filepath: str) -> Dict[str, Any]:
        """Loads JSON configuration file and merges it with default values."""
        if not os.path.exists(filepath):
            return self.defaults.copy()

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                user_config = json.load(file)
            return self.load_from_dict(user_config)
        except (json.JSONDecodeError, OSError):
            return self.defaults.copy()
