import logging
from typing import Any, Dict, Optional

# Configure logging for the main processing loop
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_payload(data: Any) -> bool:
    """Ensure input data is a non-empty dictionary."""
    if not isinstance(data, dict):
        return False
    if not data:
        return False
    return True

def process_items(queue: list) -> None:
    """Main processing loop with input validation."""
    for index, item in enumerate(queue):
        if not validate_payload(item):
            logger.error(f"Invalid data format at index {index}: {item}")
            continue

        try:
            # Process valid business logic here
            result = item.get("value", 0) * 2
            logger.info(f"Processed item {index}: result={result}")
        except Exception as e:
            logger.exception(f"Unexpected error processing index {index}: {e}")

if __name__ == "__main__":
    # Example usage for python-utils-68 loop
    sample_data = [{"value": 10}, "invalid_string", {}, {"value": 5}]
    process_items(sample_data)