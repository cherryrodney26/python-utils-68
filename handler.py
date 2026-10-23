import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(retries=3, backoff=1, exceptions=(ConnectionError, TimeoutError)):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_backoff = backoff
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"Final attempt {attempt} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed, retrying in {current_backoff}s...")
                    time.sleep(current_backoff)
                    current_backoff *= 2
            return func(*args, **kwargs)
        return wrapper
    return decorator

@with_retry(retries=3, backoff=2)
def fetch_network_data(url):
    """Example network call wrapper."""
    # Simulating actual network logic here
    logger.info(f"Fetching data from {url}")
    return {"status": "success", "url": url}