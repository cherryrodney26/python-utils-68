class BaseUtilsError(Exception):
    """Base exception for the python-utils-68 package."""

class ConfigurationError(BaseUtilsError):
    """Raised when configuration values are invalid or missing."""

class ValidationError(BaseUtilsError):
    """Raised when data validation fails."""

class ResourceNotFoundError(BaseUtilsError):
    """Raised when a requested resource does not exist."""

class ExecutionTimeoutError(BaseUtilsError):
    """Raised when an operation exceeds allocated time."""

def raise_if_none(value, message="Value cannot be None"):
    """Validates that a value is not None, raises ValidationError otherwise."""
    if value is None:
        raise ValidationError(message)

def format_exception(exc):
    """Returns a string representation of an exception with its type."""
    return f"{type(exc).__name__}: {str(exc)}"

def catch_and_log(logger, message):
    """Decorator for simple exception logging wrapper."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"{message}: {format_exception(e)}")
                raise
        return wrapper
    return decorator