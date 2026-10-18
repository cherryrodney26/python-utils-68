from typing import Any, Iterable, Dict, List, Optional

def chunk_data(data: Iterable[Any], size: int) -> List[List[Any]]:
    """Splits an iterable into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer.")
    
    result = []
    current_chunk = []
    for item in data:
        current_chunk.append(item)
        if len(current_chunk) == size:
            result.append(current_chunk)
            current_chunk = []
    if current_chunk:
        result.append(current_chunk)
    return result

def deep_merge(base: Dict[Any, Any], update: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merges two dictionaries."""
    for key, value in update.items():
        if isinstance(value, dict) and key in base and isinstance(base[key], dict):
            deep_merge(base[key], value)
        else:
            base[key] = value
    return base

def get_nested(data: Dict[Any, Any], keys: List[str], default: Any = None) -> Any:
    """Retrieves a value from a nested dictionary using a list of keys."""
    curr = data
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError):
        return default