from typing import Any, Callable, Dict, List, TypeVar, Tuple
import time
import functools

T = TypeVar("T")


def flatten_dict(
    nested_dict: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary.

    Args:
        nested_dict: Dictionary containing potentially nested dictionaries.
        parent_key: Prefix for keys during recursion.
        sep: Separator string used between nested key names.

    Returns:
        A flattened dictionary with combined key paths.
    """
    items: List[Tuple[str, Any]] = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def retry_call(
    func: Callable[..., T],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[type[BaseException], ...] = (Exception,),
) -> Callable[..., T]:
    """Decorator that retries a function upon specified exceptions.

    Args:
        func: Callable function to execute with retries.
        retries: Maximum number of retry attempts.
        delay: Initial sleep delay between attempts in seconds.
        backoff: Multiplier applied to delay after each failure.
        exceptions: Tuple of exception classes to catch and retry.

    Returns:
        Wrapped function with automatic retry behavior.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        current_delay = delay
        for attempt in range(1, retries + 1):
            try:
                return func(*args, **kwargs)
            except exceptions as err:
                if attempt == retries:
                    raise err
                time.sleep(current_delay)
                current_delay *= backoff
        raise RuntimeError("Unreachable retry state")

    return wrapper
