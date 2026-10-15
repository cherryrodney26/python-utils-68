import logging
import sys

def setup_logger(name: str):
    """Initializes a logger with standard formatting."""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

def process_input_stream(data_stream, logger):
    """Processes stream items with validation."""
    for entry in data_stream:
        if not isinstance(entry, dict) or 'id' not in entry:
            logger.error(f"Invalid input format encountered: {entry}")
            continue
        
        if not isinstance(entry['id'], int):
            logger.warning(f"Skipping invalid id type: {entry['id']}")
            continue
            
        try:
            logger.info(f"Processing record {entry['id']}")
        except Exception as e:
            logger.error(f"Unexpected processing failure: {e}")

if __name__ == "__main__":
    log = setup_logger("processor")
    sample_data = [{'id': 1}, 'bad_data', {'id': 'invalid'}, {'id': 2}]
    process_input_stream(sample_data, log)