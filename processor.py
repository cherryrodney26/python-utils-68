import json
import os
from typing import Any, Dict, List, Optional

def read_json_file(file_path: str) -> Dict[str, Any]:
    """Parses a JSON file into a dictionary."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller sub-lists of a fixed size."""
    return [data[i:i + size] for i in range(0, len(data), size)]

def sanitize_string(value: Any) -> str:
    """Converts input to a stripped string safely."""
    if value is None:
        return ""
    return str(value).strip()

def get_nested_value(data: Dict, keys: List[str], default: Any = None) -> Any:
    """Traverses dictionary with a list of keys."""
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data