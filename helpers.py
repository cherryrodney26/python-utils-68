from typing import Any, Dict, List, Optional
from collections.abc import Mapping

def flatten_dict(data: Mapping, parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary into a single level."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, Mapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_none_values(data: Dict[str, Any]) -> Dict[str, Any]:
    """Remove keys with None values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer")
    return [data[i:i + size] for i in range(0, len(data), size)]

def safe_get(data: Mapping, keys: List[str], default: Any = None) -> Any:
    """Access nested dictionary values safely using a key list."""
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default