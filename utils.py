import time
from functools import wraps
from threading import RLock
from typing import Callable, Any, Dict, Tuple

class TTLCache:
    """A thread-safe, time-to-live (TTL) cache for performance-critical lookups."""
    
    def __init__(self, ttl_seconds: float):
        self.ttl = ttl_seconds
        self._cache: Dict[Any, Tuple[Any, float]] = {}
        self._lock = RLock()

    def get(self, key: Any) -> Any:
        with self._lock:
            if key not in self._cache:
                return None
            val, expiry = self._cache[key]
            if time.time() > expiry:
                del self._cache[key]
                return None
            return val

    def set(self, key: Any, value: Any) -> None:
        with self._lock:
            expiry = time.time() + self.ttl
            self._cache[key] = (value, expiry)

    def clear(self) -> None:
        with self._lock:
            self._cache.clear()


def memoize_with_ttl(ttl_seconds: float) -> Callable:
    """Decorator to cache function results with a time-to-live limit."""
    cache = TTLCache(ttl_seconds)

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Create a cache key from args and sorted kwargs tuple
            key_kwargs = tuple(sorted(kwargs.items()))
            cache_key = (args, key_kwargs)
            
            cached_val = cache.get(cache_key)
            if cached_val is not None:
                return cached_val
                
            result = func(*args, **kwargs)
            cache.set(cache_key, result)
            return result
        return wrapper
    return decorator