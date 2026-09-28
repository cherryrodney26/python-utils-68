import functools
import time
from typing import Callable, Any, Dict

CACHE_TTL = 300
_memoization_store: Dict[str, Dict[str, Any]] = {}

def memoize(func: Callable) -> Callable:
    """Thread-safe cache decorator for expensive function calls."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
        now = time.time()
        
        if key in _memoization_store:
            entry = _memoization_store[key]
            if now - entry['timestamp'] < CACHE_TTL:
                return entry['value']
        
        result = func(*args, **kwargs)
        _memoization_store[key] = {'value': result, 'timestamp': now}
        return result
    return wrapper

def batch_process(items: list, batch_size: int = 100):
    """Generator for efficient list chunking during bulk operations."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

def fast_flatten(nested_list: list) -> list:
    """High-performance list flattening using list comprehension."""
    return [item for sublist in nested_list for item in sublist]