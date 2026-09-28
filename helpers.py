import collections.abc
from typing import Any, Dict, List, Union

def deep_flatten(items: Iterable[Any]) -> List[Any]:
    """Flatten nested lists or tuples into a single list."""
    result = []
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

def safe_get(data: Dict[Any, Any], keys: List[str], default: Any = None) -> Any:
    """Access nested dictionary values safely using a key path."""
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default

def merge_dicts(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merge two dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result