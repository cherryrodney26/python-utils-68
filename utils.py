import logging
import os
from typing import Any, Dict, Optional

# Configure standard logger for package
logger = logging.getLogger('python-utils-68')

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieve environment variable with optional fallback."""
    return os.environ.get(key, default)

def sanitize_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Remove keys with None values from dictionary."""
    return {k: v for k, v in data.items() if v is not None}

class DataProcessor:
    """Base class for data manipulation tasks."""
    def __init__(self, prefix: str = "proc"):
        self.prefix = prefix

    def format_key(self, key: str) -> str:
        return f"{self.prefix}_{key}"

def safe_execute(func: callable, *args, **kwargs) -> Any:
    """Execution wrapper with basic error catching."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.error(f"Execution failed: {e}")
        return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("Utilities module initialized")