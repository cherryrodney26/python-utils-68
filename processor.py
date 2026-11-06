import logging
from typing import Any, Optional, Dict

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    """Custom exception for processor edge cases."""
    pass

def process_data(data: Any, schema: Optional[Dict] = None) -> Any:
    """Processes input data with boundary checking."""
    if data is None:
        logger.warning("Received null data input")
        return None

    try:
        if isinstance(data, dict):
            # Ensure schema compatibility if provided
            if schema:
                for key in schema:
                    if key not in data:
                        raise ProcessingError(f"Missing required key: {key}")
            return {k: v for k, v in data.items() if v is not None}
        
        elif isinstance(data, (list, tuple)):
            return [item for item in data if item is not None]
        
        else:
            raise ProcessingError(f"Unsupported data type: {type(data).__name__}")
            
    except (TypeError, ValueError) as e:
        logger.error(f"Data transformation failure: {e}")
        raise ProcessingError("Critical failure during data serialization") from e

if __name__ == "__main__":
    # Example usage for demonstration
    try:
        result = process_data({"a": 1, "b": None}, schema=["a"])
        print(f"Processed: {result}")
    except ProcessingError as err:
        print(f"Caught expected error: {err}")