from typing import Any, Dict, List, Sequence, TypeVar

T = TypeVar("T")


def chunk_list(items: Sequence[T], chunk_size: int) -> List[Sequence[T]]:
    """Split a sequence into smaller chunks of a specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def safe_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve nested dictionary value using a dot-separated key path."""
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def flatten_dict(data: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten a nested dictionary structure using dot notation keys."""
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length appending suffix if shortened."""
    if len(text) <= max_length:
        return text
    if max_length <= len(suffix):
        return suffix[:max_length]
    return text[: max_length - len(suffix)] + suffix
