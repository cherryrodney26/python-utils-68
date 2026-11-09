import json
import os
from typing import Any, Dict, Optional

def load_json(file_path: str) -> Dict[str, Any]:
    """Load and parse a JSON file safely."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Serialize data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieve environment variable with fallback."""
    return os.environ.get(key, default) or ''

def ensure_directory(path: str) -> None:
    """Create directory structure if missing."""
    if not os.path.exists(path):
        os.makedirs(path)

def chunk_list(data: list, size: int):
    """Yield successive chunks from list."""
    for i in range(0, len(data), size):
        yield data[i:i + size]