import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures data is a non-empty dictionary."""
    if not isinstance(data, dict):
        return False
    if not data:
        return False
    if 'id' not in data or 'payload' not in data:
        return False
    return True

def process_stream(data_stream):
    """
    Main processing loop with input validation.
    Processes valid payloads and logs errors for malformed data.
    """
    for index, item in enumerate(data_stream):
        if not validate_input(item):
            logger.warning(f"Skipping invalid item at index {index}: {item}")
            continue
        
        try:
            # Simulate processing logic
            result = item['payload'].upper()
            logger.info(f"Processed item {item['id']}: {result}")
        except Exception as e:
            logger.error(f"Unexpected error processing item {index}: {e}")

if __name__ == "__main__":
    sample_data = [
        {'id': 1, 'payload': 'hello'},
        {'id': 2, 'payload': 'world'},
        None,
        {},
        {'id': 3, 'payload': 'data'}
    ]
    process_stream(sample_data)