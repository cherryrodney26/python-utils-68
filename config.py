import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with fallback defaults."""

    def __init__(self, defaults: Dict[str, Any]):
        self.defaults = defaults

    def load(self, filepath: str) -> Dict[str, Any]:
        """Load config from file and merge with defaults."""
        config = self.defaults.copy()

        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                if isinstance(file_data, dict):
                    config.update(file_data)
        except (json.JSONDecodeError, IOError):
            pass

        return config

def get_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Functional interface for config retrieval."""
    loader = ConfigLoader(defaults)
    return loader.load(filepath)