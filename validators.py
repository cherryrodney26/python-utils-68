import functools
import re
from typing import Any, Dict

# Cache compiled patterns for validation efficiency
_PATTERN_CACHE: Dict[str, re.Pattern] = {}

def get_pattern(regex: str) -> re.Pattern:
    """Thread-safe access to cached regex objects."""
    if regex not in _PATTERN_CACHE:
        _PATTERN_CACHE[regex] = re.compile(regex)
    return _PATTERN_CACHE[regex]

@functools.lru_cache(maxsize=1024)
def validate_string_format(value: str, pattern: str) -> bool:
    """High-performance validation using cached patterns and lru_cache."""
    if not isinstance(value, str):
        return False
    return bool(get_pattern(pattern).match(value))

def batch_validate(data_list: list, pattern: str) -> list:
    """Optimized batch processing of string validation checks."""
    regex_obj = get_pattern(pattern)
    return [isinstance(item, str) and bool(regex_obj.match(item)) for item in data_list]

class DataValidator:
    """Reusable validator instance with internal pattern memoization."""
    def __init__(self, schema: Dict[str, str]):
        self.schema = schema
        self._compiled = {k: re.compile(v) for k, v in schema.items()}

    def check(self, data: Dict[str, Any]) -> bool:
        """Efficient dictionary field verification against schema."""
        for field, pattern in self._compiled.items():
            val = data.get(field)
            if not isinstance(val, str) or not pattern.match(val):
                return False
        return True