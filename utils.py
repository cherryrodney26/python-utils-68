import os
import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def ensure_directory(path: str) -> bool:
    """Creates a directory if it does not exist."""
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            return True
        return False
    except OSError as e:
        logger.error(f"Failed to create directory {path}: {e}")
        return False

def clean_temp_files(directory: str, extension: str = ".tmp") -> int:
    """Removes files with specific extension from directory."""
    count = 0
    if not os.path.exists(directory):
        return count
    
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
                count += 1
            except OSError as e:
                logger.warning(f"Could not delete {file_path}: {e}")
    return count

def get_env_variable(key: str, default: Any = None) -> Optional[str]:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default)

class DataSanitizer:
    """Utility class for string cleanup operations."""
    @staticmethod
    def strip_whitespace(data: str) -> str:
        return " ".join(data.split())