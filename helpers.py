"""General utility helper functions for sequence and dictionary operations."""

from typing import Any, Dict, Generator, List, Sequence, Tuple


def deep_get(data: dict, path: str, default: Any = None, sep: str = ".") -> Any:
    """Retrieve nested dictionary values using a dot-separated path string."""
    keys = path.split(sep)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def chunk_sequence(sequence: Sequence[Any], chunk_size: int) -> Generator[Sequence[Any], None, None]:
    """Yield successive n-sized chunks from a sequence."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    for i in range(0, len(sequence), chunk_size):
        yield sequence[i : i + chunk_size]


def flatten_dict(data: dict, parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary with delimited keys."""
    items: List[Tuple[str, Any]] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def safe_cast(val: Any, to_type: type, default: Any = None) -> Any:
    """Safely cast a value to a target type, returning default on failure."""
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default
