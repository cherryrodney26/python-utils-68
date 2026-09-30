import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(exceptions, tries=3, delay=1, backoff=2):
    """
    Retry decorator for handling transient network errors.

    :param exceptions: Tuple of exceptions to catch
    :param tries: Number of attempts to make
    :param delay: Initial delay between retries in seconds
    :param backoff: Multiplier for delay after each retry
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    msg = f"{e}, Retrying in {mdelay} seconds..."
                    logger.warning(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator