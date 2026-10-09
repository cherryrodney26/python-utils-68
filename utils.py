from typing import Any, Dict, Generator, List, Optional, Sequence


def safe_get(data: Dict[str, Any], path: str, default: Optional[Any] = None) -> Any:
    """Retrieve nested dictionary value using a dot-separated key path."""
    keys = path.split(".")
    current = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries into a single updated dictionary."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def chunk_iterable(items: Sequence[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """Yield successive chunks of specified size from a sequence."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    for i in range(0, len(items), chunk_size):
        yield list(items[i : i + chunk_size])


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate string to max_length including suffix if truncated."""
    if len(text) <= max_length:
        return text
    if max_length < len(suffix):
        return suffix[:max_length]
    return text[: max_length - len(suffix)] + suffix
