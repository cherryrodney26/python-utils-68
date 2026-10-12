import time
import functools
import random
from typing import Callable, Any, Type, Tuple

class NetworkRetryError(Exception):
    """Exception raised when retries are exhausted."""
    pass

def retry_network_op(exceptions: Tuple[Type[Exception], ...] = (Exception,), 
                     max_retries: int = 3, 
                     backoff: float = 1.0):
    """Decorator to retry a function if specific network exceptions occur."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        sleep_time = backoff * (2 ** attempt) + random.uniform(0, 0.1)
                        time.sleep(sleep_time)
                        continue
            raise NetworkRetryError(f"Failed after {max_retries} attempts: {last_exception}")
        return wrapper
    return decorator