import logging

logger = logging.getLogger(__name__)

def validate_input_schema(data):
    """Validates dictionary structure and types for main loop processing."""
    required_fields = {"id": int, "payload": str}
    
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    
    for field, expected_type in required_fields.items():
        if field not in data:
            raise KeyError(f"Missing required field: {field}")
        if not isinstance(data[field], expected_type):
            raise TypeError(f"Field {field} must be of type {expected_type.__name__}")
    
    return True

def process_main_loop(items):
    """Main processing loop with integrated input validation."""
    processed = []
    for item in items:
        try:
            if validate_input_schema(item):
                # Process logic for validated data
                result = item["payload"].strip()
                processed.append({ "id": item["id"], "status": "success", "val": result })
        except (ValueError, KeyError, TypeError) as e:
            logger.error(f"Skipping invalid item {item}: {e}")
            continue
    return processed