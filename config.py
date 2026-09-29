import os
import json
from typing import Any, Dict

def load_config(file_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads configuration from a JSON file with provided defaults."""
    config = defaults.copy()

    if not os.path.exists(file_path):
        return config

    try:
        with open(file_path, 'r') as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def get_env_variable(key: str, default: Any = None) -> Any:
    """Fetches environment variable with fallback default value."""
    return os.environ.get(key, default)

# Example usage demonstration
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080, 'debug': False}
    current_config = load_config('settings.json', defaults)
    print(f'Active configuration: {current_config}')