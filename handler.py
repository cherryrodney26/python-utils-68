import logging
from typing import Any, Callable, Dict, Optional, Tuple, TypeVar

T = TypeVar("T")

logger = logging.getLogger(__name__)


class SafeHandler:
    """Utility handler designed to execute operations safely with edge case recovery."""

    @staticmethod
    def safe_cast(val: Any, target_type: type, default: Optional[Any] = None) -> Any:
        """Safely cast value to target_type, returning default on failure."""
        if val is None:
            return default
        try:
            return target_type(val)
        except (ValueError, TypeError) as err:
            logger.debug(f"Failed to cast {val!r} to {target_type.__name__}: {err}")
            return default

    @staticmethod
    def safe_get(data: Dict[str, Any], key_path: str, default: Any = None, delimiter: str = ".") -> Any:
        """Retrieve nested dictionary or list values using delimited keys with boundary checks."""
        if not isinstance(data, dict) or not key_path:
            return default

        keys = key_path.split(delimiter)
        current: Any = data

        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            elif isinstance(current, (list, tuple)):
                idx = SafeHandler.safe_cast(key, int)
                if idx is not None and 0 <= idx < len(current):
                    current = current[idx]
                else:
                    return default
            else:
                return default

        return current

    @staticmethod
    def execute_with_fallback(
        func: Callable[..., T],
        *args: Any,
        fallback: Optional[T] = None,
        **kwargs: Any
    ) -> Tuple[Optional[T], Optional[Exception]]:
        """Execute function catching standard runtime errors and returning result with error state."""
        try:
            result = func(*args, **kwargs)
            return result, None
        except Exception as exc:
            func_name = getattr(func, "__name__", "callable")
            logger.warning(f"Error executing {func_name}: {exc}")
            return fallback, exc
