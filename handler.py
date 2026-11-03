import json
from typing import Any, Dict, Optional

def clean_data(data: Any, default: Any = None) -> Any:
    """Recursively removes null values from dictionaries."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    return data

def safe_json_load(content: str) -> Dict[str, Any]:
    """Robust parsing for json string input."""
    try:
        return json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return {}

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten nested dictionary keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)