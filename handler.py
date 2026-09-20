from typing import Any, Dict, Optional, Callable
import logging

logger = logging.getLogger(__name__)

class DataHandler:
    """Utility class for processing structured data streams."""

    def __init__(self, callback: Optional[Callable[[Any], None]] = None) -> None:
        self.callback = callback
        self.registry: Dict[str, Any] = {}

    def register(self, key: str, value: Any) -> None:
        """Stores data in the internal registry."""
        self.registry[key] = value

    def process(self, key: str) -> Optional[Any]:
        """Retrieves and processes registered data by key."""
        data = self.registry.get(key)
        if data is None:
            logger.warning(f"No data found for key: {key}")
            return None

        if self.callback:
            self.callback(data)

        return data

    def clear_registry(self) -> None:
        """Resets the internal storage to empty state."""
        self.registry.clear()

    def get_count(self) -> int:
        """Returns the current count of registry items."""
        return len(self.registry)