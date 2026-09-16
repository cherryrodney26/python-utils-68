"""General data handling utilities for dictionary and nested structures."""

from typing import Any, Dict, List, Union


def deep_get(data: Dict[str, Any], keys: Union[str, List[str]], default: Any = None) -> Any:
    """Safely retrieve a value from nested dictionaries using a dot-separated key or key list."""
    if isinstance(keys, str):
        keys = keys.split('.')
    
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def deep_set(data: Dict[str, Any], keys: Union[str, List[str]], value: Any) -> Dict[str, Any]:
    """Set a value in a nested dictionary structure using a dot-separated key or key list."""
    if isinstance(keys, str):
        keys = keys.split('.')
    
    current = data
    for key in keys[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]
    
    current[keys[-1]] = value
    return data


def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary with delimited keys."""
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict) and value:
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)
