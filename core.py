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

def format_data(items: List[Any], prefix: Optional[str] = None) -> List[str]:
    """Convert list of items to string representations with optional prefix."""
    formatted = [str(item) for item in items]
    if prefix:
        return [f"{prefix}{item}" for item in formatted]
    return formatted

class DataProcessor:
    """Basic utility class for batch data transformation."""
    def __init__(self, multiplier: float = 1.0) -> None:
        self.multiplier = multiplier

    def process(self, values: List[float]) -> List[float]:
        """Apply multiplier to all numeric values in list."""
        return [v * self.multiplier for v in values]