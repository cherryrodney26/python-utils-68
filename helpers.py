import functools
from typing import Callable, Any
import time

_memoization_cache = {}

def memoize_with_ttl(ttl_seconds: int = 300) -> Callable:
    """Decorator for caching function results with time-to-live."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (func.__name__, args, frozenset(kwargs.items()))
            now = time.time()
            
            if key in _memoization_cache:
                result, timestamp = _memoization_cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            _memoization_cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(data: list, chunk_size: int = 100):
    """Generator for memory-efficient chunked list processing."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def optimized_join(items: list[str]) -> str:
    """Efficient string concatenation for large datasets."""
    return ''.join(items)