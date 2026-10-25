from typing import List, Any, Optional

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Recursively flattens a nested list into a single list.

    :param nested_list: List containing elements or further nested lists.
    :return: A flat list containing all non-list elements.
    """
    flat: List[Any] = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def get_dict_path(data: dict, path: str, delimiter: str = '.') -> Optional[Any]:
    """
    Retrieves a nested value from a dictionary using a dot-notation path.

    :param data: The dictionary to search.
    :param path: The string path (e.g., 'a.b.c').
    :param delimiter: The separator for the path keys.
    :return: The found value or None if path is invalid.
    """
    keys = path.split(delimiter)
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return None

def truncate_string(text: str, limit: int = 50, suffix: str = '...') -> str:
    """
    Truncates a string to a specified length and appends a suffix.

    :param text: The source string.
    :param limit: Maximum length of the result including suffix.
    :param suffix: String to append if truncation occurs.
    :return: The truncated string.
    """
    if len(text) <= limit:
        return text
    return text[:limit - len(suffix)] + suffix