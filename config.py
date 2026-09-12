import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Configuration manager that merges custom settings with default values."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self.config: Dict[str, Any] = self._deep_copy(defaults) if defaults else {}

    def load_dict(self, values: Dict[str, Any]) -> None:
        """Merge a dictionary into the existing configuration."""
        self.config = self._deep_merge(self.config, values)

    def load_json(self, filepath: Union[str, Path]) -> bool:
        """Load and merge configuration from a JSON file if it exists."""
        path = Path(filepath)
        if not path.is_file():
            return False

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                self.load_dict(data)
                return True
        return False

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value by dot-notation key path or return default."""
        keys = key.split(".")
        current = self.config
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default
        return current

    def _deep_merge(self, base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
        result = self._deep_copy(base)
        for key, value in update.items():
            if isinstance(value, dict) and key in result and isinstance(result[key], dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = self._deep_copy(value)
        return result

    def _deep_copy(self, value: Any) -> Any:
        if isinstance(value, dict):
            return {k: self._deep_copy(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [self._deep_copy(v) for v in value]
        return value
