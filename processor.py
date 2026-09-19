import logging

# Configure logging for the processor
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_data(items):
    """Processes a list of items with input validation."""
    processed_results = []
    
    for index, item in enumerate(items):
        # Validate input schema: expected integer and non-empty string
        if not isinstance(item, dict) or 'id' not in item or 'value' not in item:
            logger.warning(f"Skipping invalid item at index {index}: {item}")
            continue

        item_id = item['id']
        value = item['value']

        if not isinstance(item_id, int) or not isinstance(value, str):
            logger.error(f"Type mismatch in item {item_id}, skipping.")
            continue

        if len(value) == 0:
            logger.warning(f"Empty value string in item {item_id}, skipping.")
            continue

        # Perform dummy processing logic
        result = f"Processed-{item_id}-{value.upper()}"
        processed_results.append(result)
        logger.info(f"Successfully processed item {item_id}")

    return processed_results

if __name__ == "__main__":
    data = [
        {"id": 1, "value": "alpha"},
        {"id": 2, "value": ""},
        "invalid_type",
        {"id": 3, "value": "beta"}
    ]
    results = process_data(data)
    print(f"Final count: {len(results)}")