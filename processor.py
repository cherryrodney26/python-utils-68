import functools
from typing import Callable, Any

# Cache for compute-intensive transformations to reduce CPU overhead
_memoization_cache = {}

def memoize_processor(func: Callable) -> Callable:
    """Decorator for caching repetitive processor output."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

class DataProcessor:
    """Core processor with performance-oriented batch handling."""
    def __init__(self, buffer_size: int = 1000):
        self.buffer_size = buffer_size

    def batch_process(self, data: list) -> list:
        """Generator-based approach for memory-efficient iteration."""
        for i in range(0, len(data), self.buffer_size):
            chunk = data[i:i + self.buffer_size]
            yield self._apply_transformations(chunk)

    @memoize_processor
    def _apply_transformations(self, chunk: list) -> list:
        """Heavy computation performed on chunks."""
        return [x * 2 for x in chunk if isinstance(x, (int, float))]

def clear_processor_cache() -> None:
    """Manual memory reclamation for static cache."""
    _memoization_cache.clear()