import functools
from typing import Callable, Any, Dict

# Cache for compiled validation patterns to improve performance
_VALIDATION_CACHE: Dict[str, bool] = {}

def memoized_validator(func: Callable) -> Callable:
    """Decorator to cache results of expensive validation checks."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> bool:
        key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
        if key not in _VALIDATION_CACHE:
            _VALIDATION_CACHE[key] = func(*args, **kwargs)
        return _VALIDATION_CACHE[key]
    return wrapper

@memoized_validator
def validate_schema(data: Dict, schema_keys: tuple) -> bool:
    """Perform structural validation with cached schema checking."""
    if not isinstance(data, dict):
        return False
    return all(key in data for key in schema_keys)

def clear_validation_cache() -> None:
    """Manual invalidation of the validator cache."""
    _VALIDATION_CACHE.clear()

def validate_input_bounds(value: int, min_val: int, max_val: int) -> bool:
    """Performance-optimized boundary check for integers."""
    return min_val <= value <= max_val