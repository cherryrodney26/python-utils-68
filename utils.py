from typing import Any, List, Union, Type

def safe_get(
    data: Any,
    path: Union[str, List[Union[str, int]]],
    default: Any = None,
    expected_type: Type = None
) -> Any:
    """
    Safely retrieves a value from a deeply nested dictionary or list structure.
    Handles key/index errors, type mismatches, and malformed path formats.
    """
    if data is None:
        return default

    # Normalize path into a list of keys/indices
    if isinstance(path, str):
        if not path.strip():
            return default
        keys = [k for k in path.split(".") if k]
    elif isinstance(path, list):
        keys = path
    else:
        return default

    current = data
    for key in keys:
        if current is None:
            return default

        if isinstance(current, dict):
            # Safely check membership to avoid KeyError on None-like dict values
            if key not in current:
                return default
            current = current[key]
        elif isinstance(current, list):
            # Safely convert list keys and verify boundaries
            try:
                idx = int(key)
                if idx < 0 or idx >= len(current):
                    return default
                current = current[idx]
            except (ValueError, TypeError):
                return default
        else:
            # Leaf node reached but path elements still remain
            return default

    # Validate and attempt type coercion if expected_type is specified
    if expected_type is not None:
        if not isinstance(current, expected_type):
            try:
                return expected_type(current)
            except (ValueError, TypeError):
                return default

    return current
