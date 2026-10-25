"""Data processing engine with robust input validation."""

from typing import Any, Dict, List, Tuple


class ValidationError(Exception):
    """Raised when input item fails validation checks."""
    pass


class BatchProcessor:
    """Processes batches of incoming data items with structural validation."""

    def __init__(self, required_fields: List[str] | None = None) -> None:
        self.required_fields = required_fields or ["id", "payload"]
        self.processed_count = 0
        self.errors: List[Tuple[int, str]] = []

    def _validate_item(self, item: Any) -> Dict[str, Any]:
        """Validate an individual item structure and constraints."""
        if not isinstance(item, dict):
            raise ValidationError(f"Expected dict, got {type(item).__name__}")

        for field in self.required_fields:
            if field not in item or item[field] is None:
                raise ValidationError(f"Missing required field: '{field}'")

        if not isinstance(item["id"], (int, str)) or not str(item["id"]).strip():
            raise ValidationError("Field 'id' must be a non-empty string or integer")

        return item

    def process_batch(self, items: List[Any]) -> List[Dict[str, Any]]:
        """Main processing loop with input validation for each entry."""
        results = []
        self.errors.clear()

        if not isinstance(items, list):
            raise TypeError("Input batch must be a list of items")

        for index, item in enumerate(items):
            try:
                # Validate input structure before performing operations
                valid_item = self._validate_item(item)
                
                # Execute record processing
                processed_record = {
                    "id": valid_item["id"],
                    "payload": str(valid_item["payload"]).strip().upper(),
                    "status": "processed"
                }
                results.append(processed_record)
                self.processed_count += 1

            except ValidationError as err:
                # Record validation failures without halting the batch
                self.errors.append((index, str(err)))

        return results
