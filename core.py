import logging

def validate_input(data):
    """Ensure input data is a non-empty dictionary."""
    if not isinstance(data, dict) or not data:
        raise ValueError("invalid payload: expected non-empty dictionary")
    if 'id' not in data:
        raise ValueError("invalid payload: missing required key 'id'")

def process_stream(items):
    """Main loop for processing items with validation."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    for index, item in enumerate(items):
        try:
            validate_input(item)
            logger.info(f"Processing item {item.get('id')}")
            # Simulate processing logic
            result = item.get('value', 0) * 2
            print(f"Processed result for {index}: {result}")
        except ValueError as e:
            logger.error(f"Skipping item {index}: {e}")
        except Exception as e:
            logger.critical(f"Unexpected failure on item {index}: {e}")

if __name__ == '__main__':
    data_stream = [
        {'id': 1, 'value': 10},
        {'invalid': 'data'},
        {'id': 2, 'value': 20},
        {}
    ]
    process_stream(data_stream)