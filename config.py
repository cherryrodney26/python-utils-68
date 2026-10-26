import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging application configuration."""

    def __init__(self, defaults: Dict[str, Any]):
        self._defaults = defaults

    def load(self, path: str) -> Dict[str, Any]:
        """Merges file config into defaults."""
        config = self._defaults.copy()
        
        if not os.path.exists(path):
            return config

        try:
            with open(path, 'r') as f:
                file_data = json.load(f)
                config.update(file_data)
        except (json.JSONDecodeError, IOError):
            pass
            
        return config

# Usage example:
defaults = {"host": "localhost", "port": 8080, "debug": False}
loader = ConfigLoader(defaults)
config = loader.load("config.json")

def get_config_value(key: str, default_map: Dict[str, Any] = None) -> Any:
    """Helper for quick access to config items."""
    loader = ConfigLoader(default_map or {})
    return loader.load("config.json").get(key)