import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input data contains required fields and valid types."""
    if not isinstance(data, dict):
        return False, "Input must be a dictionary"
    if 'id' not in data or not isinstance(data.get('id'), int):
        return False, "Field 'id' missing or invalid type"
    if 'payload' not in data or not isinstance(data.get('payload'), str):
        return False, "Field 'payload' missing or invalid type"
    return True, None

def process_stream(data_stream):
    """Main processing loop with input validation."""
    for item in data_stream:
        is_valid, error = validate_input(item)
        
        if not is_valid:
            logger.error(f"Validation failed: {error} for item: {item}")
            continue
            
        try:
            result = item['payload'].upper()
            logger.info(f"Processed item {item['id']}: {result}")
        except Exception as e:
            logger.error(f"Unexpected error processing item {item.get('id')}: {e}")

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'payload': 'hello world'},
        {'id': 'two', 'payload': 'invalid id'},
        {'id': 3, 'payload': 'valid entry'},
        {'invalid': 'structure'}
    ]
    process_stream(sample_data)