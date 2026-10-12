import re
from typing import Any, Optional

class DataValidator:
    """Utility class for common data structure validation tasks."""

    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Check if the provided string follows standard email format."""
        if not isinstance(email, str):
            return False
        return bool(DataValidator.EMAIL_REGEX.match(email))

    @staticmethod
    def validate_range(value: int, min_val: int, max_val: int) -> bool:
        """Verify integer is within the inclusive boundaries."""
        return isinstance(value, int) and min_val <= value <= max_val

    @staticmethod
    def sanitize_input(value: Any) -> str:
        """Convert input to string and strip whitespace."""
        if value is None:
            return ""
        return str(value).strip()

    @classmethod
    def check_required_keys(cls, data: dict, keys: list[str]) -> bool:
        """Ensure all specified keys exist in the dictionary."""
        if not isinstance(data, dict):
            return False
        return all(key in data for key in keys)

def validate_payload(data: Any, schema: dict) -> bool:
    """Basic schema validation for incoming data objects."""
    if not isinstance(data, dict):
        return False
    
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True