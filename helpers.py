from typing import Any, Dict, List, Union
from collections.abc import Mapping

def deep_flatten(data: Union[List, Dict], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single-level dictionary.
    Uses dot notation or custom separator for keys.
    """
    items: List[tuple] = []
    for key, value in data.items() if isinstance(data, Mapping) else enumerate(data):
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, (dict, list)) and value:
            items.extend(deep_flatten(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)

def sanitize_keys(data: Dict[str, Any], allowed_chars: str = '_') -> Dict[str, Any]:
    """
    Replaces non-alphanumeric characters in keys with allowed_chars.
    Useful for database column mapping or clean config loading.
    """
    sanitized = {}
    for key, value in data.items():
        clean_key = ''.join(c if c.isalnum() else allowed_chars for c in str(key))
        if isinstance(value, dict):
            sanitized[clean_key] = sanitize_keys(value, allowed_chars)
        else:
            sanitized[clean_key] = value
    return sanitized

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """
    Splits a list into smaller chunks of specified size.
    Useful for batch processing large datasets.
    """
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [data[i:i + size] for i in range(0, len(data), size)]