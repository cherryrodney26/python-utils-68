"""General core utilities for data manipulation and function execution."""

import time
from functools import wraps
from typing import Any, Dict, List, Iterable, Generator, Callable, Type, Tuple


def deep_merge(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merge dict2 into dict1 and return a new dictionary."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def chunk_iterable(iterable: Iterable[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """Yield successive n-sized chunks from an iterable."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def retry(
    max_attempts: int = 3, 
    delay: float = 1.0, 
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """Decorator to retry a function call if specified exceptions occur."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    time.sleep(delay)
        return wrapper
    return decorator
