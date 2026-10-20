from typing import Any, Dict, List, Optional


class DataHandler:
    """Utility handler for nested dictionary navigation and transformation."""

    @staticmethod
    def flatten(data: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
        """Flatten a nested dictionary into a single-level dictionary using custom separators."""
        items: List[tuple] = []
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                items.extend(DataHandler.flatten(value, new_key, sep=sep).items())
            else:
                items.append((new_key, value))
        return dict(items)

    @staticmethod
    def get_nested(data: Dict[str, Any], path: str, default: Optional[Any] = None, sep: str = ".") -> Any:
        """Safely extract a value from a deep nested dict structure using key paths."""
        keys = path.split(sep)
        current = data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current

    @staticmethod
    def set_nested(data: Dict[str, Any], path: str, value: Any, sep: str = ".") -> Dict[str, Any]:
        """Set a value at a specific path, creating missing nested dicts automatically."""
        keys = path.split(sep)
        current = data
        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value
        return data
