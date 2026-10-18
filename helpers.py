import json
import os
from typing import Any, Dict, Optional

def load_json_file(filepath: str) -> Dict[str, Any]:
    """Loads data from a JSON file into a dictionary."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(data: Dict[str, Any], filepath: str) -> bool:
    """Saves dictionary data to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def chunk_list(data: list, size: int):
    """Splits a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieves environment variable with optional default value."""
    return os.environ.get(key, default)

def sanitize_string(value: str) -> str:
    """Removes whitespace and converts to lowercase."""
    return value.strip().lower()