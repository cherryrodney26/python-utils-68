"""Custom exception hierarchy and error handling utilities for edge cases."""

from typing import Any, Callable, Optional, Type, Union
import functools


class BaseUtilError(Exception):
    """Base exception class for all python-utils package errors."""

    def __init__(self, message: str, payload: Optional[Any] = None) -> None:
        super().__init__(message)
        self.message = message
        self.payload = payload

    def __str__(self) -> str:
        if self.payload is not None:
            return f"{self.message} [payload={self.payload!r}]"
        return self.message


class ValidationError(BaseUtilError):
    """Raised when input parameters fail domain or formatting constraints."""
    pass


class ResourceLimitError(BaseUtilError):
    """Raised when execution limits like memory or iteration counts are exceeded."""
    pass


class ConversionError(BaseUtilError):
    """Raised when data transformation fails for boundary or invalid values."""
    pass


def safe_execute(
    default_value: Any = None,
    caught_exceptions: Union[Type[Exception], tuple[Type[Exception], ...]] = (BaseUtilError, ValueError, TypeError)
) -> Callable:
    """Decorator to safely handle edge case exceptions and return a fallback value."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except caught_exceptions:
                return default_value
        return wrapper
    return decorator
