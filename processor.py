import json
from typing import Any, Dict, List, Optional

def clean_data(data: Any, default: Any = None) -> Any:
    """
    Recursively cleans input data to handle None values or empty strings.
    Returns a sanitized version of the provided input structure.
    """
    if isinstance(data, dict):
        return {k: clean_data(v, default) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [clean_data(item, default) for item in data if item is not None]
    return data if data is not None else default

def batch_process(items: List[Dict], key: str, transform_func) -> List[Any]:
    """
    Applies a transformation function to specific keys in a list of dictionaries.
    Returns a list of transformed values, skipping missing keys.
    """
    results = []
    for item in items:
        if key in item:
            try:
                results.append(transform_func(item[key]))
            except (ValueError, TypeError):
                continue
    return results

def serialize_json(data: Any, indent: int = 4) -> str:
    """
    Safe serialization of complex objects into JSON strings.
    """
    try:
        return json.dumps(data, indent=indent, default=str)
    except (TypeError, ValueError):
        return json.dumps({"error": "serialization failed"})