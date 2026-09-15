import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_data(data_list):
    """Processes a list of integers with input validation."""
    results = []
    for item in data_list:
        try:
            # Validate that input is a numeric type
            if not isinstance(item, (int, float)):
                raise ValueError(f"Invalid input type: {type(item).__name__}")
            
            # Validate range constraints
            if not (0 <= item <= 1000):
                raise ValueError(f"Value out of bounds: {item}")
            
            processed_val = item * 2
            results.append(processed_val)
            logger.info(f"Processed {item} successfully")
            
        except ValueError as e:
            logger.warning(f"Skipping invalid entry: {e}")
            continue
            
    return results

if __name__ == "__main__":
    # Test data including invalid inputs for demonstration
    raw_input = [10, 500, "invalid", -5, 1200, 25]
    output = process_data(raw_input)
    print(f"Final processing results: {output}")