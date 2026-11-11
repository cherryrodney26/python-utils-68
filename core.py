import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None) -> Any:
    """
    Execute a function safely with comprehensive error trapping
    for common execution edge cases.
    """
    try:
        if not callable(func):
            raise ValueError(f"Provided object {func} is not callable")
        return func(*args)
    except (ValueError, TypeError, KeyError, IndexError) as e:
        logger.error(f"Data processing error in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system failure during {func.__name__}: {e}")
        return default

def validate_input(data: Any, expected_type: type) -> Optional[Any]:
    """
    Strict validation for data integrity across utilities.
    """
    if data is None:
        return None
    
    try:
        if not isinstance(data, expected_type):
            return None
        return data
    except Exception:
        return None