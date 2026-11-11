from typing import Any, Dict, List, Optional
import json

def load_json_config(file_path: str) -> Dict[str, Any]:
    """
    Reads a JSON configuration file from the filesystem.

    Args:
        file_path: The absolute or relative path to the json file.

    Returns:
        A dictionary containing the configuration data.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def sanitize_input(data: List[str]) -> List[str]:
    """
    Cleans a list of strings by stripping whitespace.

    Args:
        data: A list of input strings to be cleaned.

    Returns:
        A list of cleaned and trimmed strings.
    """
    return [item.strip() for item in data if item]

def format_response(status: str, message: Optional[str] = None) -> Dict[str, str]:
    """
    Constructs a standardized response dictionary.

    Args:
        status: The response status code or label.
        message: An optional status description string.

    Returns:
        A dictionary containing the formatted response payload.
    """
    response: Dict[str, str] = {"status": status}
    if message:
        response["message"] = message
    return response