import logging

# Configure logger for module tracking
logger = logging.getLogger(__name__)

def process_input_stream(data_stream):
    """Processes stream and validates individual inputs."""
    for item in data_stream:
        try:
            # Validate mandatory keys presence
            if not isinstance(item, dict) or 'id' not in item:
                logger.warning(f"Invalid item format encountered: {item}")
                continue

            # Validate payload constraint
            payload = item.get('value')
            if not isinstance(payload, (int, float)):
                logger.error(f"Invalid numeric value for id {item['id']}")
                continue

            # Proceed with business logic
            execute_task(item)

        except Exception as e:
            logger.exception(f"Unexpected loop error: {e}")

def execute_task(data):
    """Dummy processing unit."""
    print(f"Processing task {data['id']}: {data['value']}")

if __name__ == "__main__":
    # Simulation of incoming data processing
    raw_data = [{'id': 1, 'value': 100}, {'id': 2, 'value': 'bad'}, {'id': 3, 'value': 250}]
    process_input_stream(raw_data)