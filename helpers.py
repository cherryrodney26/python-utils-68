import time
from functools import wraps
from typing import Any, Callable, Dict, TypeVar

T = TypeVar("T")


def deep_merge(dict_a: Dict[str, Any], dict_b: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merges two dictionaries.

    If keys conflict and both values are dictionaries, they are merged.
    Otherwise, the value from the second dictionary overwrites the first.
    """
    result = dict_a.copy()
    for key, value in dict_b.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def retry_on_exception(
    retries: int = 3, delay: float = 1.0
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator that retries a function execution upon encountering an exception.

    Args:
        retries: The number of times to retry the operation before raising.
        delay: The sleep interval in seconds between retry attempts.
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            last_exception = None
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < retries:
                        time.sleep(delay)
            if last_exception is not None:
                raise last_exception
            raise RuntimeError("Retry failed without captured exception")

        return wrapper

    return decorator
