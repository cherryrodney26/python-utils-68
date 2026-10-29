import json
from typing import Any, Dict, Optional

def safe_data_extract(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """
    Navigates nested dictionary using dot-notation string.
    Example: safe_data_extract(data, 'user.profile.id')
    """
    keys = path.split('.')
    current = data
    
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current.get(key)
            else:
                return default
        return current if current is not None else default
    except (AttributeError, TypeError, KeyError):
        return default

def format_json_output(data: Any, indent: int = 4) -> str:
    """
    Serializes complex data structures to clean JSON string.
    """
    try:
        return json.dumps(data, indent=indent, sort_keys=True)
    except (TypeError, ValueError) as e:
        return json.dumps({"error": "serialization failed", "details": str(e)})

def normalize_keys(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Converts all top-level dictionary keys to lowercase.
    """
    return {str(k).lower(): v for k, v in data.items()}