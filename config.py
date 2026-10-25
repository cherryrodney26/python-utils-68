import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    Returns the resulting dictionary.
    """
    config = defaults.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                config.update(data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """
    Saves the configuration dictionary to a JSON file.
    """
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)

# Example usage:
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    settings = load_config('settings.json', defaults)
    print(f'Loaded settings: {settings}')