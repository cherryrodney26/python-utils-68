import re
from typing import Any, Optional

def is_valid_email(email: str) -> bool:
    """Validate email address format."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def is_non_empty_string(value: Any) -> bool:
    """Check if input is a non-empty string."""
    return isinstance(value, str) and len(value.strip()) > 0

def is_within_range(value: int, min_val: int, max_val: int) -> bool:
    """Check if integer is within inclusive bounds."""
    return isinstance(value, int) and min_val <= value <= max_val

def validate_required_keys(data: dict, keys: list[str]) -> bool:
    """Verify presence of mandatory keys in dictionary."""
    return all(key in data for key in keys)

def sanitize_input(value: str) -> str:
    """Remove dangerous characters for basic sanitization."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', value)