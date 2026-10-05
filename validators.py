"""Input validation utilities for record processing pipelines."""

from typing import Any, Callable, Dict, List, Optional, Tuple


class ValidationError(Exception):
    """Raised when input validation fails."""
    pass


def validate_record(
    record: Dict[str, Any],
    schema: Dict[str, Tuple[type, bool, Optional[Callable[[Any], bool]]]],
) -> Dict[str, Any]:
    """Validate a single record against schema rules.
    
    Schema format: {field_name: (expected_type, required, optional_validator_func)}
    """
    if not isinstance(record, dict):
        raise ValidationError(f"Expected dict record, got {type(record).__name__}")

    validated = {}
    for field, rules in schema.items():
        expected_type, required, custom_validator = rules
        
        if field not in record or record[field] is None:
            if required:
                raise ValidationError(f"Missing required field: '{field}'")
            validated[field] = None
            continue
            
        val = record[field]
        if not isinstance(val, expected_type):
            raise ValidationError(
                f"Field '{field}' must be of type {expected_type.__name__}, got {type(val).__name__}"
            )
            
        if custom_validator and not custom_validator(val):
            raise ValidationError(f"Field '{field}' failed custom validation with value: {val}")
            
        validated[field] = val
        
    return validated


def process_and_validate_batch(
    items: List[Dict[str, Any]],
    schema: Dict[str, Tuple[type, bool, Optional[Callable[[Any], bool]]]],
    skip_invalid: bool = False,
) -> List[Dict[str, Any]]:
    """Validate a batch of input records within a processing loop."""
    valid_records = []
    for index, item in enumerate(items):
        try:
            clean_item = validate_record(item, schema)
            valid_records.append(clean_item)
        except ValidationError as err:
            if not skip_invalid:
                raise ValidationError(f"Batch item at index {index} failed: {err}") from err
    return valid_records
