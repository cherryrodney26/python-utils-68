import functools
import time
from typing import Callable, Any, Dict

# Cache for computed expensive function results
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching results of expensive operations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100) -> list:
    """Generator for memory-efficient batch processing."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceOptimizer:
    """Utility class for execution time tracking."""
    def __init__(self):
        self.start_time = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start_time
        print(f"Execution completed in {elapsed:.4f} seconds")

@memoize
def heavy_computation(n: int) -> int:
    """Simulated intensive mathematical operation."""
    result = 0
    for i in range(n):
        result += i * i
    return result