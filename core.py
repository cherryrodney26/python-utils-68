import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

class OperationError(Exception):
    """Base exception for utility operations."""
    pass

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Executes a function with safety wrappers for common edge cases."""
    try:
        if not callable(func):
            raise ValueError(f"Expected callable, got {type(func).__name__}")
        
        return func(*args, **kwargs)
    
    except (TypeError, ValueError, AttributeError) as e:
        logger.error(f"Argument or attribute error in {func.__name__}: {e}")
        return default
    
    except Exception as e:
        logger.critical(f"Unexpected failure during execution: {e}")
        raise OperationError(f"Critical failure in {func.__name__}") from e

def validate_input(data: Optional[Any]) -> bool:
    """Checks input for null or empty edge cases."""
    if data is None:
        return False
    if isinstance(data, (str, list, dict)) and len(data) == 0:
        return False
    return True