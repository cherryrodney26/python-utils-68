import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_network_op(exceptions: Tuple[Type[Exception], ...] = (Exception,), 
                     tries: int = 3, 
                     delay: float = 1.0, 
                     backoff: float = 2.0):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(tries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries - 1:
                        logger.error(f"Final attempt {attempt + 1} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_op(exceptions=(ConnectionError, TimeoutError), tries=3)
def fetch_data(url: str):
    """Simulated network call that requires retry logic."""
    # Example implementation detail
    raise ConnectionError(f"Failed to connect to {url}")