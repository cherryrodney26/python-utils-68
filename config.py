import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    """
    config = defaults.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                if isinstance(file_data, dict):
                    config.update(file_data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config file {filepath}: {e}")
            
    return config

def get_env_config(prefix: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Overrides configuration values using environment variables with a specific prefix.
    Example: APP_PORT overrides 'port'.
    """
    config = defaults.copy()
    for key in config.keys():
        env_key = f"{prefix}_{key.upper()}"
        if env_key in os.environ:
            val = os.environ[env_key]
            # Attempt basic type casting
            if isinstance(config[key], bool):
                config[key] = val.lower() in ('true', '1', 'yes')
            elif isinstance(config[key], int):
                config[key] = int(val)
            else:
                config[key] = val
    return config