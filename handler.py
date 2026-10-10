from typing import Any, Dict, Optional, Callable
import logging

logger = logging.getLogger(__name__)

class DataHandler:
    """Handles transformation and validation of input datasets."""

    def __init__(self, transform_func: Optional[Callable[[Any], Any]] = None) -> None:
        self.transform_func = transform_func

    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Applies transformation logic to the provided dictionary data.

        Args:
            data: A dictionary containing raw input data.

        Returns:
            A dictionary with processed values.
        """
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")

        processed = data.copy()
        if self.transform_func:
            for key, value in processed.items():
                processed[key] = self.transform_func(value)
        
        logger.info(f"Processed {len(processed)} items successfully")
        return processed

    def validate_keys(self, data: Dict[str, Any], required_keys: list[str]) -> bool:
        """
        Checks if all required keys are present in the dictionary.

        Args:
            data: The dictionary to check.
            required_keys: A list of keys that must exist.

        Returns:
            True if all keys are present, False otherwise.
        """
        return all(key in data for key in required_keys)