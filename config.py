import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles configuration loading from JSON files with defaults."""

    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_file(self, filepath: str) -> None:
        """Updates config dictionary with values from a JSON file."""
        if not os.path.exists(filepath):
            return

        try:
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                self.config.update(file_data)
        except (json.JSONDecodeError, IOError):
            pass

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key."""
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Sets a configuration value."""
        self.config[key] = value

def create_config(defaults: Dict[str, Any], path: str = None) -> ConfigLoader:
    """Factory function for standardized config initialization."""
    loader = ConfigLoader(defaults)
    if path:
        loader.load_from_file(path)
    return loader