import logging
import sys

def setup_logger(name: str) -> logging.Logger:
    """Configures a standard console logger."""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

def run_processing_loop(data_list: list):
    """Processes a list of integers with input validation."""
    logger = setup_logger("processor")
    
    for item in data_list:
        # Validate input type and value range
        if not isinstance(item, int):
            logger.error(f"Invalid input type: {type(item).__name__}. Expected int.")
            continue
            
        if item < 0:
            logger.warning(f"Negative value ignored: {item}")
            continue
            
        # Perform dummy business logic
        result = item * 2
        logger.info(f"Processed value {item} to {result}")

if __name__ == "__main__":
    test_data = [10, "invalid", -5, 20]
    run_processing_loop(test_data)