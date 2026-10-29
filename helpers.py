import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def safe_json_load(file_path: str) -> Dict[str, Any]:
    """Load and parse JSON file with error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"failed to read json at {file_path}: {e}")
        return {}

def chunk_list(data: list, size: int):
    """Split a list into chunks of specified size."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def dict_get_nested(data: Dict, path: str, default: Any = None) -> Any:
    """Retrieve nested dictionary value using dot notation."""
    keys = path.split('.')
    curr = data
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError):
        return default

def ensure_list(item: Any) -> list:
    """Convert single item to list if not iterable."""
    if item is None:
        return []
    if isinstance(item, (list, tuple, set)):
        return list(item)
    return [item]