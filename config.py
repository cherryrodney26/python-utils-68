import os
from typing import Any, Dict, Optional, Type, TypeVar, Union

T = TypeVar("T")


class Config:
    """A flexible configuration manager with environment variable overrides."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the configuration with optional default values."""
        self._config: Dict[str, Any] = defaults or {}

    def get(
        self, key: str, default: Optional[T] = None, cast_to: Optional[Type[T]] = None
    ) -> Union[Any, T, None]:
        """Retrieve a configuration value by key, checking env variables first.

        Args:
            key: The configuration key to retrieve.
            default: The default value to return if not found.
            cast_to: Optional type to cast the resulting value.

        Returns:
            The configured value, cast to the desired type, or default.
        """
        env_key = key.upper()
        value = os.environ.get(env_key, self._config.get(key, default))

        if value is None:
            return default

        if cast_to is not None:
            try:
                if cast_to is bool:
                    return str(value).lower() in ("true", "1", "yes", "on")  # type: ignore
                return cast_to(value)
            except (ValueError, TypeError):
                return default

        return value

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value dynamically."""
        self._config[key] = value
