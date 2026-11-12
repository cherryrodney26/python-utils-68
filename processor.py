from typing import Any, Callable, Dict, List, Tuple


class DataProcessor:
    """Processes a stream or list of items with strict input validation."""

    def __init__(self, validator: Callable[[Any], bool] = None):
        self.validator = validator or self._default_validator

    @staticmethod
    def _default_validator(item: Any) -> bool:
        """Default validation checks if item is non-None and non-empty if container."""
        if item is None:
            return False
        if isinstance(item, (str, dict, list, set, tuple)) and len(item) == 0:
            return False
        return True

    def process_batch(self, items: List[Any]) -> Tuple[List[Any], List[Dict[str, Any]]]:
        """Runs the main processing loop with input validation.

        Returns processed results and validation error records.
        """
        processed_results = []
        validation_errors = []

        for index, item in enumerate(items):
            # Input validation in the main processing loop
            if not isinstance(item, (dict, list, str, int, float)):
                validation_errors.append(
                    {"index": index, "item": item, "reason": "Unsupported data type"}
                )
                continue

            if not self.validator(item):
                validation_errors.append(
                    {
                        "index": index,
                        "item": item,
                        "reason": "Failed validation check",
                    }
                )
                continue

            # Transform valid item
            transformed = self._transform(item)
            processed_results.append(transformed)

        return processed_results, validation_errors

    def _transform(self, item: Any) -> Any:
        """Applies basic processing transformation to valid inputs."""
        if isinstance(item, str):
            return item.strip().lower()
        if isinstance(item, (int, float)):
            return item * 2
        if isinstance(item, dict):
            return {k: self._transform(v) for k, v in item.items() if v is not None}
        return item
