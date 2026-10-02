class BaseUtilityError(Exception):
    """Base exception for python-utils-68 operations."""
    pass

class ConfigurationError(BaseUtilityError):
    """Raised when configuration values are invalid or missing."""
    pass

class ProcessingError(BaseUtilityError):
    """Raised when a data transformation task fails."""
    pass

def raise_if_none(value, message: str):
    """Check if value is None and raise configuration error."""
    if value is None:
        raise ConfigurationError(message)
    return value

def handle_execution(func):
    """Decorator for catching and wrapping processing exceptions."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise ProcessingError(f"Task failed: {str(e)}") from e
    return wrapper

class ValidationError(BaseUtilityError):
    """Raised during schema or input validation failures."""
    pass