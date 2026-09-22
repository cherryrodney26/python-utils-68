import functools
from typing import Callable, Any

# internal cache for intensive transformation tasks
_MEMOIZATION_CACHE = {}

def memoize(func: Callable) -> Callable:
    """decorator for caching function results to improve throughput"""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _MEMOIZATION_CACHE:
            _MEMOIZATION_CACHE[key] = func(*args, **kwargs)
        return _MEMOIZATION_CACHE[key]
    return wrapper

class DataProcessor:
    """core processor for high-frequency data operations"""
    
    def __init__(self, batch_size: int = 1000):
        self.batch_size = batch_size

    @memoize
    def transform(self, value: int) -> int:
        """simulates expensive compute operation"""
        result = 0
        for i in range(1000):
            result += (value * i) % 7
        return result

    def process_batch(self, data: list[int]) -> list[int]:
        """optimized batch processing utilizing local cache"""
        results = []
        # using list comprehension for faster iteration
        results = [self.transform(item) for item in data]
        return results

def clear_processor_cache() -> None:
    """manual memory management for the global cache"""
    _MEMOIZATION_CACHE.clear()