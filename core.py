from typing import Any, Dict, List, Optional, Callable
import time

class DataProcessor:
    """Utility class for processing collections of data with timing support."""

    def __init__(self, debug: bool = False) -> None:
        self.debug: bool = debug

    def transform(self, items: List[Any], func: Callable[[Any], Any]) -> List[Any]:
        """Apply a function to all items and return a list of results."""
        start_time: float = time.time()
        results: List[Any] = [func(item) for item in items]
        
        if self.debug:
            duration: float = time.time() - start_time
            print(f"Processed {len(items)} items in {duration:.4f}s")
            
        return results

    def flatten(self, nested_list: List[List[Any]]) -> List[Any]:
        """Flatten a list of lists into a single list."""
        return [item for sublist in nested_list for item in sublist]

    def get_summary(self, data: Dict[str, Any]) -> str:
        """Return a string summary of the provided dictionary."""
        keys: List[str] = list(data.keys())
        return f"Dataset contains {len(keys)} keys: {', '.join(keys)}"