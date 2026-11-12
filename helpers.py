"""General helper utilities with standard error handling for edge cases."""

from typing import Any, Dict, List, Union


def safe_cast(value: Any, target_type: type, default: Any = None) -> Any:
    """Safely cast a value to a target type with default fallback on failure."""
    if value is None:
        return default
    try:
        return target_type(value)
    except (ValueError, TypeError, OverflowError):
        return default


def get_nested(data: Union[Dict, List], path: str, default: Any = None, delimiter: str = ".") -> Any:
    """Retrieve a nested value from dict/list structure using a delimited path string."""
    if not isinstance(path, str) or not path:
        return default

    keys = path.split(delimiter)
    current = data

    for key in keys:
        if isinstance(current, dict):
            current = current.get(key, default)
        elif isinstance(current, (list, tuple)):
            try:
                idx = int(key)
                current = current[idx]
            except (ValueError, IndexError, TypeError):
                return default
        else:
            return default

        if current is default:
            break

    return current


def format_bytes(size: Union[int, float, str]) -> str:
    """Format byte sizes into a human-readable string representation."""
    try:
        num = float(size)
        if num < 0:
            return "0.00 B"
    except (ValueError, TypeError):
        return "0.00 B"

    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    unit_index = 0

    while num >= 1024.0 and unit_index < len(units) - 1:
        num /= 1024.0
        unit_index += 1

    return f"{num:.2f} {units[unit_index]}"
