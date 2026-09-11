import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with defaults."""
    
    def __init__(self, default_config: Dict[str, Any]):
        self.defaults = default_config

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads configuration from file, merging with defaults."""
        config = self.defaults.copy()
        
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    user_config = json.load(f)
                    config.update(user_config)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not read config {filepath}: {e}")
        
        return config

def get_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Helper function for quick config instantiation."""
    loader = ConfigLoader(defaults)
    return loader.load(filepath)

if __name__ == '__main__':
    # Example usage
    defaults = {"host": "localhost", "port": 8080}
    cfg = get_config("settings.json", defaults)
    print(f"Active configuration: {cfg}")