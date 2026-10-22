import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    """Decorator to retry network-bound functions with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    if attempt < max_retries:
                        logger.warning(f"Retry {attempt + 1}/{max_retries} due to {e}")
                        time.sleep(current_delay)
                        current_delay *= 2
                    else:
                        logger.error("Max retries exceeded.")
            
            raise last_exception  # type: ignore
        return wrapper
    return decorator