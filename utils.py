import time
import random
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def retry(exceptions, tries=4, delay=1, backoff=2, jitter=True):
    """
    Decorator to retry a function call with exponential backoff and jitter.

    :param exceptions: Exception or tuple of exceptions to catch.
    :param tries: Maximum number of times to try the function.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to delay after each retry.
    :param jitter: Whether to apply a random jitter to the delay.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    current_delay = mdelay
                    if jitter:
                        # Apply random jitter to avoid thundering herd problem
                        current_delay *= random.uniform(0.5, 1.5)

                    logger.warning(
                        f"Execution failed: {e}. Retrying in {current_delay:.2f} seconds... "
                        f"({mtries - 1} attempts left)"
                    )
                    time.sleep(current_delay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator