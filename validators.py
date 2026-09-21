import math
import re
from typing import Any, Dict, List, Optional, Union


class ValidationError(ValueError):
    """Custom exception raised when validation fails."""

    pass


def validate_numeric(
    value: Any, min_val: Optional[float] = None, max_val: Optional[float] = None
) -> float:
    """Validates and converts a value to float, handling infinite and NaN edge cases."""
    if value is None:
        raise ValidationError("Value cannot be None")

    try:
        num = float(value)
    except (TypeError, ValueError) as err:
        raise ValidationError(f"Cannot convert {type(value).__name__} to float") from err

    if math.isnan(num):
        raise ValidationError("Value cannot be NaN (Not a Number)")

    if math.isinf(num):
        raise ValidationError("Value cannot be infinite")

    if min_val is not None and num < min_val:
        raise ValidationError(f"Value {num} is below minimum allowed {min_val}")

    if max_val is not None and num > max_val:
        raise ValidationError(f"Value {num} is above maximum allowed {max_val}")

    return num


def safe_get_nested(data: Any, path: List[Union[str, int]], default: Any = None) -> Any:
    """Safely traverses nested dictionaries or lists, handling index and key errors."""
    if not isinstance(data, (dict, list)):
        return default

    current = data
    for key in path:
        if isinstance(current, dict) and isinstance(key, str):
            if key in current:
                current = current[key]
            else:
                return default
        elif isinstance(current, list) and isinstance(key, int):
            if 0 <= key < len(current):
                current = current[key]
            else:
                return default
        else:
            return default

    return current


def validate_email(email: Any) -> str:
    """Validates an email address against length restrictions and basic format."""
    if not isinstance(email, str):
        raise ValidationError("Email must be a string")

    # Clean null bytes and leading/trailing spaces
    cleaned = email.strip().replace("\x00", "")

    if len(cleaned) < 3 or len(cleaned) > 254:
        raise ValidationError("Email length must be between 3 and 254 characters")

    # Simple regex for structure check, robust to basic ReDoS
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, cleaned):
        raise ValidationError("Invalid email address format")

    return cleaned
