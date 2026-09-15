import logging
from typing import Any, Optional, Union

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles core data processing with defensive error handling."""
    
    def __init__(self, settings: Optional[dict] = None):
        self.settings = settings or {}

    def safe_transform(self, data: Any) -> Union[Any, None]:
        """Applies transformation with exhaustive error handling for edge cases."""
        try:
            if data is None:
                logger.warning("Attempted to process null data input")
                return None
            
            # Simulate potential processing error
            if not isinstance(data, (str, int, float, list, dict)):
                raise ValueError(f"Unsupported data type: {type(data).__name__}")
                
            return str(data).strip()

        except ValueError as ve:
            logger.error(f"Validation failure: {ve}")
            return None
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}", exc_info=True)
            return None

    def batch_process(self, items: list) -> list:
        """Processes list items while isolating failures."""
        if not isinstance(items, list):
            return []
        
        results = []
        for item in items:
            result = self.safe_transform(item)
            if result is not None:
                results.append(result)
        return results