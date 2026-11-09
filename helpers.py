"""General utility helpers for data manipulation and safe execution."""

import time
from typing import Any, Callable, Dict, Iterable, List, Optional, TypeVar

T = TypeVar("T")


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merges dict2 into dict1 without mutating input dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> List[List[T]]:
    """Splits an iterable collection into fixed-size chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    items = list(iterable)
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def safe_execute(
    func: Callable[..., T],
    *args: Any,
    default: Optional[T] = None,
    retries: int = 0,
    delay: float = 0.5,
    **kwargs: Any,
) -> Optional[T]:
    """Executes a callable safely, retrying on failure before returning default."""
    attempts = 0
    while attempts <= retries:
        try:
            return func(*args, **kwargs)
        except Exception:
            attempts += 1
            if attempts > retries:
                return default
            time.sleep(delay)
    return default


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncates text to specified maximum length appending suffix if needed."""
    if len(text) <= max_length:
        return text
    trim_len = max(0, max_length - len(suffix))
    return text[:trim_len] + suffix
