class UtilsError(Exception):
    """Base exception for python-utils-68 operations."""
    pass

class ConfigurationError(UtilsError):
    """Raised when configuration values are invalid."""
    pass

class ValidationError(UtilsError):
    """Raised when data validation fails."""
    pass

def raise_if_none(value, message="Value cannot be None"):
    """Raises ValidationError if the provided value is None."""
    if value is None:
        raise ValidationError(message)

def ensure_type(value, expected_type, name="Value"):
    """Validates that a value matches the expected type."""
    if not isinstance(value, expected_type):
        raise ValidationError(f"{name} must be {expected_type.__name__}, got {type(value).__name__}")

def safe_execute(func, *args, **kwargs):
    """Executes a function and catches UtilsError exceptions."""
    try:
        return func(*args, **kwargs)
    except UtilsError as e:
        # Log error in real implementation
        return None
    except Exception as e:
        # Bubble up unexpected exceptions
        raise UtilsError(f"Unexpected error in {func.__name__}: {str(e)}") from e