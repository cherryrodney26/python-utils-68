from typing import List, Any, Dict, Optional


def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """
    Divide a list into smaller segments of a specified size.
    """
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer")
    return [data[i : i + size] for i in range(0, len(data), size)]


def format_dict_keys(data: Dict[str, Any], prefix: str = "item") -> Dict[str, Any]:
    """
    Prepend a prefix string to all keys in a dictionary.
    """
    return {f"{prefix}_{key}": value for key, value in data.items()}


def get_nested(data: Dict[str, Any], keys: List[str], default: Optional[Any] = None) -> Any:
    """
    Retrieve a value from a nested dictionary using a list of keys.
    """
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default