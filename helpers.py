import functools
import time
from typing import Callable, Any, Dict

# Cache for storing expensive function results
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function return values to improve execution speed."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Generator for memory-efficient iteration over large datasets."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def timed_execution(func: Callable) -> Callable:
    """Performance monitoring wrapper for core module analysis."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"Execution of {func.__name__} took {duration:.4f}s")
        return result
    return wrapper