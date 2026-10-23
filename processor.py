import logging

# Configure logger for module tracking
logger = logging.getLogger(__name__)

def validate_input(data):
    """Validate that the input dictionary contains required keys and types."""
    required_keys = {"id": int, "value": str}
    for key, expected_type in required_keys.items():
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
        if not isinstance(data[key], expected_type):
            raise TypeError(f"Invalid type for {key}, expected {expected_type.__name__}")
    return True

def process_stream(data_stream):
    """Main processing loop with integrated input validation."""
    for entry in data_stream:
        try:
            validate_input(entry)
            logger.info(f"Processing record {entry['id']}")
            
            # Simulate core logic execution
            result = entry['value'].strip().upper()
            print(f"Processed result: {result}")
            
        except (ValueError, TypeError) as e:
            logger.error(f"Validation failed for entry {entry}: {e}")
            continue
        except Exception as e:
            logger.critical(f"Unexpected error processing {entry}: {e}")
            break

if __name__ == "__main__":
    mock_data = [
        {"id": 1, "value": "alpha"},
        {"id": "invalid", "value": "beta"},
        {"id": 2, "value": "gamma"}
    ]
    process_stream(mock_data)