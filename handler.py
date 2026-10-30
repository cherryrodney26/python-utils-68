import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def with_retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """
    Decorator to retry network operations with exponential backoff.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            last_exception = None

            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            
            logger.error(f"Operation failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@with_retry(retries=3, delay=2.0)
def fetch_remote_resource(url: str):
    """
    Example network operation wrapper.
    """
    logger.info(f"Fetching data from {url}")
    # Simulate network instability
    raise ConnectionError("Server unreachable")