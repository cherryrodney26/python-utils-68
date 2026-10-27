import functools
import logging
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry a network function with exponential backoff.

    :param max_retries: Maximum number of attempts before raising exception.
    :param backoff_factor: Multiplier applied to exponential delay.
    :param exceptions: Tuple of exception classes to catch and retry.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    attempts += 1
                    if attempts >= max_retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {max_retries} attempts: {err}"
                        )
                        raise err

                    sleep_time = backoff_factor * (2 ** (attempts - 1))
                    logger.warning(
                        f"Attempt {attempts}/{max_retries} for '{func.__name__}' failed ({err}). "
                        f"Retrying in {sleep_time:.2f}s..."
                    )
                    time.sleep(sleep_time)

        return wrapper
    return decorator
