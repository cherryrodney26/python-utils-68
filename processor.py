import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)

class DataProcessor:
    """Processes and validates raw data payloads in batches."""

    def __init__(self, min_value: float = 0.0, max_value: float = 1000.0):
        self.min_value = min_value
        self.max_value = max_value

    def validate_record(self, record: Dict[str, Any]) -> Tuple[bool, str]:
        """Validates a single record for required keys and correct data types."""
        if not isinstance(record, dict):
            return False, "Record must be a dictionary"

        if "id" not in record or "value" not in record:
            return False, "Missing required keys: 'id' or 'value'"

        if not isinstance(record["id"], (int, str)):
            return False, "Identifier 'id' must be an integer or string"

        try:
            val = float(record["value"])
        except (ValueError, TypeError):
            return False, "Field 'value' must be a numeric value"

        if not (self.min_value <= val <= self.max_value):
            return False, f"Value {val} out of bounds [{self.min_value}, {self.max_value}]"

        return True, ""

    def process_batch(self, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Processes a batch of data, skipping and logging invalid entries."""
        processed_data = []

        for index, item in enumerate(batch):
            is_valid, error_msg = self.validate_record(item)
            if not is_valid:
                logger.warning(f"Skipping record at index {index}: {error_msg}")
                continue

            clean_item = {
                "id": item["id"],
                "value": float(item["value"]),
                "processed": True
            }
            processed_data.append(clean_item)

        return processed_data
