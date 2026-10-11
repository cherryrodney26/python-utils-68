class UtilsError(Exception):
    """Base exception for python-utils-68."""

class ValidationError(UtilsError):
    """Raised when input fails validation checks."""

class ConfigurationError(UtilsError):
    """Raised when system configuration is invalid."""

def handle_exception(e: Exception) -> None:
    """Centralized error reporting for edge cases."""
    if isinstance(e, (ValidationError, ConfigurationError)):
        print(f"[Handled] {type(e).__name__}: {e}")
    else:
        print(f"[Critical] Unexpected error: {e}")
        raise e

def validate_input(data: any) -> bool:
    """Practical validation with edge case handling."""
    if data is None:
        raise ValidationError("Input data cannot be null")
    if not isinstance(data, (dict, list)):
        raise ValidationError("Data must be dictionary or list")
    return True