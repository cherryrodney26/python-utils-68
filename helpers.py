import functools
import time
from typing import Any, Callable, Generator, Sequence, TypeVar

T = TypeVar("T")


def chunk_iterable(iterable: Sequence[T], chunk_size: int) -> Generator[Sequence[T], None, None]:
    """Yield successive n-sized chunks from a sequence."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i : i + chunk_size]


def flatten_dict(d: dict[str, Any], parent_key: str = "", sep: str = ".") -> dict[str, Any]:
    """Flatten a nested dictionary using key concatenation."""
    items: list[tuple[str, Any]] = []
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def human_readable_size(size_bytes: int) -> str:
    """Format a byte count into a human-readable string representation."""
    if size_bytes < 0:
        raise ValueError("size_bytes must be non-negative")
    if size_bytes == 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = 0
    size = float(size_bytes)
    while size >= 1024.0 and i < len(units) - 1:
        size /= 1024.0
        i += 1
    return f"{size:.2f} {units[i]}" if i > 0 else f"{int(size)} B"


def retry(max_attempts: int = 3, delay: float = 1.0, exceptions: tuple[type[BaseException], ...] = (Exception,)) -> Callable:
    """Decorator to retry a function call on specific exceptions."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    last_exception = err
                    if attempt < max_attempts and delay > 0:
                        time.sleep(delay)
            if last_exception:
                raise last_exception
        return wrapper
    return decorator
