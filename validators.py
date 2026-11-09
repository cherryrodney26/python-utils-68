from typing import Any, Dict, List, Optional, Union


class ValidationError(ValueError):
    """Raised when data validation fails."""
    pass


def validate_dict_structure(
    data: Any,
    required_keys: List[str],
    type_schema: Optional[Dict[str, type]] = None
) -> Dict[str, Any]:
    """
    Validates a dictionary against required keys and optional type constraints.
    Handles edge cases such as None inputs, non-dict types, missing keys, and invalid types.
    """
    if data is None:
        raise ValidationError("Input data cannot be None")
    
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dict, got {type(data).__name__}")
    
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        raise ValidationError(f"Missing required keys: {', '.join(missing_keys)}")
    
    if type_schema:
        for key, expected_type in type_schema.items():
            if key in data and data[key] is not None:
                if not isinstance(data[key], expected_type):
                    raise ValidationError(
                        f"Key '{key}' expected type {expected_type.__name__}, "
                        f"got {type(data[key]).__name__}"
                    )
    return data


def validate_numeric_range(
    value: Union[int, float],
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None
) -> Union[int, float]:
    """
    Validates that a numeric value falls within an optional min/max range.
    Handles edge cases like NaN, boolean inputs, non-numeric types, and range boundaries.
    """
    if value is None or isinstance(value, bool):
        raise ValidationError("Value must be a valid number (int or float)")
    
    if not isinstance(value, (int, float)):
        raise ValidationError(f"Expected int or float, got {type(value).__name__}")
    
    # Check for NaN floating point values
    if value != value:
        raise ValidationError("Numeric value cannot be NaN")
    
    if min_val is not None and value < min_val:
        raise ValidationError(f"Value {value} is below minimum allowed value {min_val}")
        
    if max_val is not None and value > max_val:
        raise ValidationError(f"Value {value} is above maximum allowed value {max_val}")
        
    return value
