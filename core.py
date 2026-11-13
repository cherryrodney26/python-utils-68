from typing import Any, Dict, List, Optional

def merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries for configuration management."""
    result = base.copy()
    for key, value in override.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result

def sanitize_input(data: Any, allowed_types: Optional[List[type]] = None) -> Any:
    """Validate and clean input based on allowed types."""
    if allowed_types and not isinstance(data, tuple(allowed_types)):
        raise ValueError(f"Input {data} is not of type {allowed_types}")
    if isinstance(data, str):
        return data.strip()
    return data

class DataProcessor:
    """Base class for standard data transformation operations."""
    def __init__(self, prefix: str = "proc") -> None:
        self.prefix = prefix

    def format_key(self, key: str) -> str:
        """Apply prefix to a given key string."""
        return f"{self.prefix}_{key}"

    def process_batch(self, items: List[str]) -> List[str]:
        """Transform a list of strings using the instance prefix."""
        return [self.format_key(i) for i in items]