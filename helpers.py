from typing import Any, Dict, List, Optional
from collections.abc import Mapping

def deep_flatten(data: Any, prefix: str = '', separator: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary with keys joined by separator."""
    items = {}
    if isinstance(data, Mapping):
        for key, value in data.items():
            new_key = f"{prefix}{separator}{key}" if prefix else key
            if isinstance(value, Mapping):
                items.update(deep_flatten(value, new_key, separator))
            else:
                items[new_key] = value
    else:
        items[prefix] = data
    return items

def batch_process(items: List[Any], batch_size: int = 10) -> List[List[Any]]:
    """Split a list into smaller chunks for batch processing."""
    if batch_size <= 0:
        raise ValueError("Batch size must be a positive integer")
    return [items[i:i + batch_size] for i in range(0, len(items), batch_size)]

def safe_get(data: Dict[str, Any], keys: List[str], default: Any = None) -> Any:
    """Access nested dictionary values safely using a list of keys."""
    current = data
    for key in keys:
        if isinstance(current, Mapping) and key in current:
            current = current[key]
        else:
            return default
    return current