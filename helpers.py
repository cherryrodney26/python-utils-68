import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def safe_get_nested(data: dict, keys: list, default: Any = None) -> Any:
    """Safely access nested dictionary keys with error handling."""
    if not isinstance(data, dict):
        logger.warning("Input data is not a dictionary")
        return default
    
    current = data
    try:
        for key in keys:
            if not isinstance(current, dict) or key not in current:
                return default
            current = current[key]
        return current
    except (TypeError, KeyError, IndexError) as e:
        logger.error(f"Unexpected error accessing keys {keys}: {e}")
        return default

def robust_conversion(value: Any, target_type: type, default: Any = None) -> Any:
    """Attempt type conversion with graceful failure."""
    try:
        return target_type(value)
    except (ValueError, TypeError, OverflowError) as e:
        logger.debug(f"Conversion to {target_type} failed for {value}: {e}")
        return default

def validate_and_process(items: list, processor_func: callable) -> list:
    """Process list elements with item-level error isolation."""
    results = []
    for item in items:
        try:
            results.append(processor_func(item))
        except Exception as e:
            logger.error(f"Failed to process item {item}: {e}")
            continue
    return results