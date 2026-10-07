import logging

def validate_input(data):
    """Ensures input data conforms to expected schema."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if "id" not in data or not isinstance(data["id"], int):
        raise ValueError("Missing or invalid integer 'id'")
    return True

def process_items(items):
    """Main processing loop with integrated input validation."""
    results = []
    for item in items:
        try:
            if validate_input(item):
                # Simulate core processing logic
                processed = {
                    "id": item["id"],
                    "status": "processed",
                    "value": item.get("value", 0) * 2
                }
                results.append(processed)
        except (ValueError, TypeError) as e:
            logging.error(f"Skipping invalid item {item}: {e}")
            continue
    return results

if __name__ == "__main__":
    data_stream = [{"id": 1, "value": 10}, {"invalid": True}, {"id": 2, "value": 5}]
    print(process_items(data_stream))