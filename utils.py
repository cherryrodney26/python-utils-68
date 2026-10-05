import json
import os
from typing import Any, Dict, Optional

def load_data(filepath: str) -> Optional[Dict[str, Any]]:
    """Load and parse JSON data from a file."""
    if not os.path.exists(filepath):
        return None
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_data(filepath: str, data: Dict[str, Any]) -> bool:
    """Save dictionary to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (TypeError, IOError):
        return False

def sanitize_input(data: Any) -> Any:
    """Remove null values from dictionary or list."""
    if isinstance(data, dict):
        return {k: sanitize_input(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [sanitize_input(i) for i in data if i is not None]
    return data