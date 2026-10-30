import re
from typing import Any, Optional

# Validation patterns for standard input strings
EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
IP_PATTERN = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

def validate_email(email: str) -> bool:
    """Verify email address format against regex."""
    return bool(EMAIL_PATTERN.match(email))

def validate_ip(ip: str) -> bool:
    """Verify ipv4 address string structure."""
    if not IP_PATTERN.match(ip):
        return False
    return all(0 <= int(octet) <= 255 for octet in ip.split('.'))

def ensure_not_none(value: Any, name: str) -> Any:
    """Check for nullity and raise exception if invalid."""
    if value is None:
        raise ValueError(f"parameter {name} cannot be null")
    return value

class ValidatorManager:
    """Registry for reusable input validation logic."""
    def __init__(self):
        self._rules = {}

    def register(self, name: str, func: callable) -> None:
        self._rules[name] = func

    def check(self, name: str, value: Any) -> bool:
        if name not in self._rules:
            raise KeyError(f"validator {name} not defined")
        return self._rules[name](value)