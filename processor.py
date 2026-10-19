import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    """Base exception for processor operations."""
    pass

def process_data(data: Any) -> Optional[dict]:
    """Process raw data with input validation and error handling."""
    try:
        if data is None:
            raise ValueError("Received null input data")
        
        if not isinstance(data, dict):
            raise TypeError(f"Expected dict, got {type(data).__name__}")

        # Simulate processing logic
        result = {"status": "success", "payload": data}
        return result

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return None
    except TypeError as e:
        logger.error(f"Type mismatch error: {e}")
        return None
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}", exc_info=True)
        raise ProcessingError("Critical failure during data processing") from e

def batch_process(items: list) -> list:
    """Safe execution of multiple data items."""
    results = []
    for item in items:
        processed = process_data(item)
        if processed:
            results.append(processed)
    return results