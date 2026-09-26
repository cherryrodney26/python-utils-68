import logging
from typing import Any, Optional, Union

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles data transformation with robust error recovery."""

    def __init__(self, default_val: Any = None):
        self.default_val = default_val

    def process_item(self, item: Any) -> Any:
        try:
            if item is None:
                raise ValueError("Received null input")
            
            # Simulate standard operation
            return str(item).strip()
            
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid input encountered: {e}")
            return self.default_val
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}")
            raise

    def batch_process(self, items: list) -> list:
        """Process a list of items and handle potential batch failures."""
        if not isinstance(items, list):
            logger.warning("Batch process received non-list input")
            return []

        results = []
        for item in items:
            try:
                results.append(self.process_item(item))
            except Exception:
                results.append(self.default_val)
        return results