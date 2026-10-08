from typing import Any, Dict, Generator, Iterable, List, Union


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into single-level keys."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def safe_get(
    data: Union[Dict, List], path: str, default: Any = None, sep: str = "."
) -> Any:
    """Retrieve nested values from dicts/lists using a separated path string."""
    keys = path.split(sep)
    current = data

    for key in keys:
        if isinstance(current, dict):
            current = current.get(key, default)
        elif isinstance(current, list) and key.isdigit():
            idx = int(key)
            if 0 <= idx < len(current):
                current = current[idx]
            else:
                return default
        else:
            return default

        if current is default:
            break

    return current


def chunk_iterable(
    iterable: Iterable[Any], chunk_size: int
) -> Generator[List[Any], None, None]:
    """Yield successive chunks of specified size from an iterable."""
    if chunk_size < 1:
        raise ValueError("chunk_size must be at least 1")

    chunk: List[Any] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
