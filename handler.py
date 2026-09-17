import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)


def validate_payload(data: Dict[str, Any]) -> Tuple[bool, str]:
    """Validates the input item structure and required types."""
    if not isinstance(data, dict):
        return False, "Payload must be a dictionary"

    required_fields = {
        "id": (int, float),
        "value": (int, float),
        "operation": str,
    }

    for field, expected_type in required_fields.items():
        if field not in data:
            return False, f"Missing required field: '{field}'"
        if not isinstance(data[field], expected_type):
            return False, f"Invalid type for '{field}'"

    if data["operation"] not in ("multiply", "divide", "add", "subtract"):
        return False, f"Unsupported operation: {data['operation']}"

    if data["operation"] == "divide" and data["value"] == 0:
        return False, "Division by zero is not allowed"

    return True, ""


def process_batch(items: List[Dict[str, Any]], base_value: float) -> List[float]:
    """Processes a batch of payloads with strict input validation inside the loop."""
    results = []

    for index, item in enumerate(items):
        is_valid, error_msg = validate_payload(item)

        if not is_valid:
            logger.warning(f"Skipping item at index {index}: {error_msg}")
            continue

        item_id = item["id"]
        operation = item["operation"]
        value = item["value"]

        try:
            if operation == "add":
                result = base_value + value
            elif operation == "subtract":
                result = base_value - value
            elif operation == "multiply":
                result = base_value * value
            elif operation == "divide":
                result = base_value / value
            else:
                continue

            results.append(result)
            logger.info(f"Successfully processed item {item_id}: {result}")
        except Exception as err:
            logger.error(f"Unexpected error processing item {item_id}: {err}")

    return results