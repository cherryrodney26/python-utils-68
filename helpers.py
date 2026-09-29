from typing import Any, Dict, List, Optional

def deep_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve nested values from dictionaries using dot notation."""
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError, AttributeError):
        return default

def sanitize_dict(data: Dict[str, Any], keys_to_remove: List[str]) -> Dict[str, Any]:
    """Remove sensitive or unwanted keys from a dictionary."""
    return {k: v for k, v in data.items() if k not in keys_to_remove}

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Convert nested lists into a single flat list."""
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

def chunk_iterable(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of specific size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [items[i:i + size] for i in range(0, len(items), size)]