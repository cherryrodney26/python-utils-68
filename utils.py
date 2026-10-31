from typing import Any, Iterable, Optional
from collections import defaultdict

def group_by_key(data: Iterable[dict], key: str) -> dict[Any, list[dict]]:
    """Groups a list of dictionaries by a specified key."""
    grouped = defaultdict(list)
    for entry in data:
        if key in entry:
            grouped[entry[key]].append(entry)
    return dict(grouped)

def flatten_list(nested_list: list[list[Any]]) -> list[Any]:
    """Flattens a list of lists into a single list."""
    return [item for sublist in nested_list for item in sublist]

def sanitize_dict(data: dict, allowed_keys: Optional[set[str]] = None) -> dict:
    """Returns a dictionary containing only specified allowed keys."""
    if allowed_keys is None:
        return data
    return {k: v for k, v in data.items() if k in allowed_keys}

def chunk_iterable(items: Iterable[Any], size: int) -> Iterable[list[Any]]:
    """Yields successive n-sized chunks from an iterable."""
    chunk = []
    for item in items:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk