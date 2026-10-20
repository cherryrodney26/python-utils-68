import os
import json
import logging

logger = logging.getLogger(__name__)

def load_config(filepath: str) -> dict:
    """Loads configuration from a JSON file with validation."""
    if not filepath:
        raise ValueError("configuration filepath cannot be empty")

    if not os.path.exists(filepath):
        logger.error(f"config file missing: {filepath}")
        return {}

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if not isinstance(data, dict):
                logger.warning(f"invalid format in {filepath}, expected dict")
                return {}
            return data
    except json.JSONDecodeError as e:
        logger.error(f"failed to parse json in {filepath}: {e}")
        return {}
    except PermissionError:
        logger.error(f"insufficient permissions for {filepath}")
        return {}
    except Exception as e:
        logger.error(f"unexpected error reading config: {e}")
        return {}