"""Core utility functions for data manipulation and functional helpers."""

from functools import wraps
import time
from typing import Any, Callable, Dict, Iterable, List, TypeVar

T = TypeVar("T")


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary by concatenating keys with a separator.

    Args:
        d: The nested dictionary to flatten.
        parent_key: Prefix for keys at current recursion depth.
        sep: Separator string between nested keys.

    Returns:
        A flat dictionary with string keys and primitive values.
    """
    items: List[tuple[str, Any]] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def chunk_iterable(iterable: Iterable[T], size: int) -> List[List[T]]:
    """Split an iterable into fixed-size chunks.

    Args:
        iterable: Sequence or iterable to divide into chunks.
        size: Maximum size of each chunk.

    Returns:
        List of lists containing elements grouped into chunks.

    Raises:
        ValueError: If chunk size is less than 1.
    """
    if size < 1:
        raise ValueError("Chunk size must be at least 1")
    items = list(iterable)
    return [items[i : i + size] for i in range(0, len(items), size)]


def measure_time(func: Callable[..., T]) -> Callable[..., T]:
    """Decorator that prints execution duration of a function.

    Args:
        func: Function to measure.

    Returns:
        Wrapped function with timing instrumentation.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[{func.__name__}] executed in {elapsed:.4f}s")
        return result

    return wrapper
