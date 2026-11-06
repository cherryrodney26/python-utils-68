from typing import List, Optional, Any, Callable

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Recursively flatten a nested list structure into a single list."""
    flat: List[Any] = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def chunk_iterable(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller sub-lists of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [data[i:i + size] for i in range(0, len(data), size)]

def filter_by_predicate(items: List[Any], predicate: Callable[[Any], bool]) -> List[Any]:
    """Filter a list based on a provided predicate function."""
    return [item for item in items if predicate(item)]

def get_safe(data: dict, keys: List[str], default: Optional[Any] = None) -> Any:
    """Retrieve a nested value from a dictionary safely."""
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default