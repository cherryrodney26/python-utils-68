import functools
import time
from typing import Callable, Any, Dict

# Cache for storing expensive function results to optimize execution
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function return values."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Memory-efficient generator for processing large lists."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class PerformanceOptimizer:
    """Utility class for executing functions with timing hooks."""
    @staticmethod
    def measure_execution(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"Execution of {func.__name__} took {end - start:.6f}s")
            return result
        return wrapper