import json
import os
from typing import Any, Dict, Optional

def load_json_file(filepath: str) -> Dict[str, Any]:
    """Reads and parses a JSON file into a dictionary."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(filepath: str, data: Dict[str, Any]) -> None:
    """Serializes a dictionary to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback default."""
    return os.environ.get(key, default or '')

def chunk_list(data: list, size: int):
    """Splits a list into smaller chunks of defined size."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_path(path: str) -> str:
    """Normalizes and cleans filesystem paths."""
    return os.path.normpath(path.strip())