import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_data(data_list):
    """Processes a list of integers with validation."""
    results = []
    for item in data_list:
        try:
            # Validate input type and constraints
            if not isinstance(item, (int, float)):
                raise ValueError(f"Invalid input type: {type(item).__name__}")
            
            if not (0 <= item <= 1000):
                raise ValueError(f"Input out of range: {item}")
            
            # Perform transformation
            processed = item * 2
            results.append(processed)
            logger.debug(f"Processed item: {item}")
            
        except ValueError as e:
            logger.error(f"Skipping invalid entry: {e}")
            continue
            
    return results

if __name__ == "__main__":
    raw_input = [10, 500, "invalid", 2000, 42]
    final_data = process_data(raw_input)
    logger.info(f"Processing complete. Items: {len(final_data)}")