import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.0,
    max_backoff: float = 60.0,
    jitter: bool = True,
    retryable_exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """Decorator to retry network operations with exponential backoff and optional jitter."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as exc:
                    retries += 1
                    if retries > max_retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {max_retries} retries."
                        )
                        raise exc

                    sleep_time = min(max_backoff, backoff_factor * (2 ** (retries - 1)))
                    if jitter:
                        sleep_time += random.uniform(0, 0.1 * sleep_time)

                    logger.warning(
                        f"Retry {retries}/{max_retries} for '{func.__name__}' after error: {exc}. "
                        f"Waiting {sleep_time:.2f}s..."
                    )
                    time.sleep(sleep_time)

        return wrapper

    return decorator