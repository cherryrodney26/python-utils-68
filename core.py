import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Execute function with robust error handling for edge cases."""
    if not callable(func):
        logger.error("Provided object is not callable")
        return default

    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError) as e:
        logger.warning(f"Validation or attribute error in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system failure in {func.__name__}: {e}", exc_info=True)
        return default

def validate_input(value: Any, expected_type: type) -> bool:
    """Check for null inputs and type consistency."""
    if value is None:
        return False
    return isinstance(value, expected_type)

class ExecutionContext:
    """Context manager for resource cleanup during operations."""
    def __init__(self, resource: Any):
        self.resource = resource

    def __enter__(self):
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.error(f"Cleanup triggered by error: {exc_val}")
        return False