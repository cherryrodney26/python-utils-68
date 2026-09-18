class BaseUtilsError(Exception):
    """Base exception for python-utils-68."""

class ConfigurationError(BaseUtilsError):
    """Raised when configuration is invalid."""

class ProcessingError(BaseUtilsError):
    """Raised during data processing tasks."""

class ValidationError(BaseUtilsError):
    """Raised when validation constraints fail."""

def handle_exception(e: Exception) -> None:
    """Centralized exception logging and formatting."""
    if isinstance(e, BaseUtilsError):
        print(f"[Utils Error] {e.__class__.__name__}: {str(e)}")
    else:
        print(f"[Unexpected Error] {type(e).__name__}: {str(e)}")

if __name__ == '__main__':
    try:
        raise ConfigurationError("Missing required environment variable")
    except BaseUtilsError as err:
        handle_exception(err)