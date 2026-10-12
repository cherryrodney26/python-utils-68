import json
import logging
from typing import Any, Dict, Optional

def sanitize_input(data: str) -> str:
    """Removes extra whitespace and cleans input string."""
    return data.strip()

def safe_load_json(json_str: str) -> Optional[Dict[str, Any]]:
    """Parses JSON string safely returning None on failure."""
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        logging.error("invalid json input provided")
        return None

def chunk_list(items: list, size: int):
    """Splits a list into smaller chunks of defined size."""
    for i in range(0, len(items), size):
        yield items[i:i + size]

def get_nested_key(data: dict, keys: list, default: Any = None) -> Any:
    """Navigates deep dictionaries using list of keys."""
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default