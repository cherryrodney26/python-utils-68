import functools
import time
from typing import Callable, Any, Dict

# internal cache for performance optimization
_cache: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Thread-safe-like caching decorator for intensive calculations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = f"{func.__name__}:{args}:{kwargs}"
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

def bulk_process(data: list, batch_size: int = 100) -> list:
    """Optimized batch generator for large list traversal."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

class PerformanceTracker:
    """Simple context manager for execution time tracking."""
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"[Performance] {self.name} took {elapsed:.4f} seconds")