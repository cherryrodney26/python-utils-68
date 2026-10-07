import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Utility class to load JSON configurations with default values and env overrides."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self.defaults = defaults or {}
        self.config: Dict[str, Any] = self.defaults.copy()

    def load_from_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Merge a dictionary into default settings."""
        merged = self.defaults.copy()
        merged.update(data)
        self.config = merged
        return self.config

    def load_from_file(self, filepath: Union[str, Path]) -> Dict[str, Any]:
        """Load configuration from a JSON file, falling back to defaults if missing."""
        path = Path(filepath)
        merged = self.defaults.copy()

        if path.is_file():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    if isinstance(file_data, dict):
                        merged.update(file_data)
            except (json.JSONDecodeError, OSError):
                pass

        self.config = merged
        return self.config

    def apply_env_overrides(self, prefix: str = "APP_") -> Dict[str, Any]:
        """Override configuration values using environment variables matching a prefix."""
        for key in list(self.config.keys()):
            env_var = f"{prefix}{key.upper()}"
            if env_var in os.environ:
                val = os.environ[env_var]
                if val.lower() in ("true", "false"):
                    self.config[key] = val.lower() == "true"
                elif val.isdigit():
                    self.config[key] = int(val)
                else:
                    self.config[key] = val
        return self.config

    def get(self, key: str, fallback: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.config.get(key, fallback)
