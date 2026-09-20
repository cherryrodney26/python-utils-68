import json
import os
from typing import Any, Dict, Optional

def ensure_dir(path: str) -> None:
    """Creates directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def load_json(filepath: str) -> Dict[str, Any]:
    """Reads and parses a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], filepath: str) -> None:
    """Serializes data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with default."""
    return os.environ.get(key, default) or ''

def chunk_list(data: list, size: int):
    """Yields successive chunks from list."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    """Flattens nested dictionary structure."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)