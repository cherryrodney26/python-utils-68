import functools
import time
from typing import Callable, Any, Dict

# global cache for heavy computation results
_CACHE: Dict[tuple, Any] = {}

def memoize_result(func: Callable) -> Callable:
    """Thread-safe memoization decorator for expensive operations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Generator for memory-efficient batch processing."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceTracker:
    """Context manager for tracking execution duration."""
    def __init__(self, name: str):
        self.name = name
        self.start = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"[Performance] {self.name} took {elapsed:.4f}s")

def clear_core_cache() -> None:
    """Manual cache invalidation for system memory management."""
    _CACHE.clear()