class BaseUtilsError(Exception):
    """Base exception for the python-utils-68 package."""

class ConfigurationError(BaseUtilsError):
    """Raised when configuration settings are invalid."""

class ProcessingError(BaseUtilsError):
    """Raised when data processing operations fail."""

class ValidationError(BaseUtilsError):
    """Raised when data validation constraints are violated."""

class ResourceNotFoundError(BaseUtilsError):
    """Raised when a requested resource is missing."""

def raise_error(exception_type: type[BaseUtilsError], message: str) -> None:
    """Helper to raise standardized package exceptions."""
    raise exception_type(message)

if __name__ == "__main__":
    # Example usage for verification
    try:
        raise_error(ConfigurationError, "Missing mandatory config key")
    except ConfigurationError as e:
        print(f"Caught expected exception: {e}")