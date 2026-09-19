import re
from typing import Any, Optional

def is_email(email: str) -> bool:
    """Validate standard email address format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_uuid(uuid_str: str) -> bool:
    """Validate RFC 4122 UUID strings."""
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    return bool(re.match(pattern, uuid_str.lower()))

def validate_range(value: Any, min_val: float, max_val: float) -> bool:
    """Check if numeric value is within bounds."""
    if not isinstance(value, (int, float)):
        return False
    return min_val <= value <= max_val

def require_non_empty(data: Optional[Any]) -> bool:
    """Ensure data is not None or empty container."""
    if data is None:
        return False
    if isinstance(data, (str, list, dict, set)):
        return len(data) > 0
    return True

def is_alphanumeric(value: str) -> bool:
    """Check for strictly alphanumeric characters."""
    return value.isalnum()