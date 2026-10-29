class BaseUtilsError(Exception):
    """Base exception class for python-utils-68."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when configuration validation fails."""
    pass

class ProcessingError(BaseUtilsError):
    """Raised during data transformation failures."""
    pass

class ValidationError(BaseUtilsError):
    """Raised when input validation fails."""
    pass

def handle_exception(exc: Exception) -> None:
    """Centralized exception reporting helper."""
    if isinstance(exc, BaseUtilsError):
        print(f"[Utils Error]: {exc}")
    else:
        print(f"[System Error]: {type(exc).__name__} - {exc}")