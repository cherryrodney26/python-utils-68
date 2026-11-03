"""Safe data retrieval and conversion utilities with robust edge case handling."""

import math
from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar("T")


def safe_get(
    data: Any,
    key_path: str,
    default: Optional[T] = None,
    delimiter: str = "."
) -> Union[Any, T]:
    """
    Safely retrieve nested values from dictionary or list structures.
    Handles None input, missing keys, out-of-bound indices, and invalid types.
    """
    if not key_path or not isinstance(key_path, str):
        return default

    if data is None:
        return default

    keys = key_path.split(delimiter)
    current = data

    for key in keys:
        if current is None:
            return default

        if isinstance(current, Mapping):
            current = current.get(key, default)
        elif isinstance(current, (list, tuple)):
            try:
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    return default
            except (ValueError, TypeError):
                return default
        else:
            return default

    return current


def safe_cast_float(value: Any, default: float = 0.0) -> float:
    """
    Safely cast input to float, handling NaN, Infinity, and type errors.
    """
    if value is None:
        return default

    try:
        result = float(value)
        if math.isnan(result) or math.isinf(result):
            return default
        return result
    except (ValueError, TypeError, OverflowError):
        return default
