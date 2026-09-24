import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging application configurations with defaults."""
    
    def __init__(self, default_config: Dict[str, Any]):
        self._defaults = default_config

    def load_from_file(self, filepath: str) -> Dict[str, Any]:
        """Load config from json file, merging with defaults."""
        config = self._defaults.copy()

        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    user_config = json.load(f)
                    config.update(user_config)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load config file {filepath}: {e}")
        
        return config

    def get_env_override(self, key: str, value: Any) -> Any:
        """Override config value using environment variables."""
        return os.getenv(key, value)

# Example usage:
if __name__ == '__main__':
    defaults = {"host": "localhost", "port": 8080, "debug": False}
    loader = ConfigLoader(defaults)
    
    # Load merged configuration
    final_cfg = loader.load_from_file('config.json')
    
    # Apply environment overrides
    final_cfg['port'] = int(loader.get_env_override('APP_PORT', final_cfg['port']))
    print(f"Configuration loaded: {final_cfg}")