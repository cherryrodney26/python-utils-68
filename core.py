import collections.abc
from typing import Any, Dict, List, Union

def deep_flatten(items: Iterable[Any]) -> List[Any]:
    """Flatten nested structures into a single list."""
    result = []
    for item in items:
        if isinstance(item, (list, tuple, set)) and not isinstance(item, (str, bytes)):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

def sanitize_dict(data: Dict[str, Any], keys_to_mask: List[str] = None) -> Dict[str, Any]:
    """Redact sensitive values in a dictionary."""
    keys_to_mask = keys_to_mask or ['password', 'token', 'secret']
    sanitized = data.copy()
    for key in sanitized:
        if key.lower() in keys_to_mask:
            sanitized[key] = '********'
        elif isinstance(sanitized[key], dict):
            sanitized[key] = sanitize_dict(sanitized[key], keys_to_mask)
    return sanitized

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks."""
    if size <= 0:
        raise ValueError("chunk size must be positive")
    return [data[i:i + size] for i in range(0, len(data), size)]