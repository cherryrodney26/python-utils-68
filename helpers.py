from typing import List, Optional, Any, Callable

def filter_none(data: List[Optional[Any]]) -> List[Any]:
    """Remove all None entries from a list.

    Args:
        data: A list containing optional elements.

    Returns:
        A filtered list containing only non-None values.
    """
    return [item for item in data if item is not None]

def apply_transformation(items: List[Any], func: Callable[[Any], Any]) -> List[Any]:
    """Apply a transformation function to each item in a list.

    Args:
        items: The input list of elements.
        func: A callable function to transform each element.

    Returns:
        A new list with transformed values.
    """
    return [func(item) for item in items]

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of a fixed size.

    Args:
        items: The list to be partitioned.
        size: The maximum size of each chunk.

    Returns:
        A list of lists containing the chunks.
    """
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [items[i:i + size] for i in range(0, len(items), size)]