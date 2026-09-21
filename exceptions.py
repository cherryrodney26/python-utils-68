import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class UtilityError(Exception):
    """Base exception for python-utils-68 package."""
    pass

class ConfigurationError(UtilityError):
    """Raised when config values are invalid or missing."""
    pass

class ProcessingError(UtilityError):
    """Raised when data transformation fails unexpectedly."""
    pass

def handle_exception(exc: Exception, context: Optional[str] = None) -> None:
    """
    Centralized error logger for utility operations.
    Logs the error with stack trace and optional context.
    """
    msg = f"Error occurred in {context}: " if context else "Error: "
    logger.error(f"{msg}{str(exc)}", exc_info=True)

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Any:
    """
    Wraps function execution with error handling.
    Returns None if an exception is caught.
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        handle_exception(e, func.__name__)
        return None