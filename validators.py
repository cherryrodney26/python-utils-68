import re
from typing import Any, Dict, List, Optional, Union


def is_valid_email(email: str) -> bool:
    """Validate basic email format using standard regex."""
    if not isinstance(email, str) or not email:
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email.strip()))


def is_valid_url(url: str) -> bool:
    """Check if a string is a valid HTTP or HTTPS URL."""
    if not isinstance(url, str) or not url:
        return False
    pattern = r"^https?://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, url.strip(), re.IGNORECASE))


def is_in_range(
    val: Union[int, float],
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
) -> bool:
    """Check if a numeric value falls within a given range (inclusive)."""
    if not isinstance(val, (int, float)):
        return False
    if min_val is not None and val < min_val:
        return False
    if max_val is not None and val > max_val:
        return False
    return True


def validate_dict_keys(data: Dict[str, Any], required_keys: List[str]) -> bool:
    """Verify that all required keys exist and are non-null in a dictionary."""
    if not isinstance(data, dict):
        return False
    return all(key in data and data[key] is not None for key in required_keys)
