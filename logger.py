import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a standardized logger with edge case error handling."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        try:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        except (OSError, IOError) as e:
            # Fallback to null handler if stdout is unavailable
            logger.addHandler(logging.NullHandler())
            print(f"Logger setup failed: {e}", file=sys.stderr)

    return logger

def safe_log(logger: logging.Logger, level: int, message: str) -> None:
    """Logs messages safely handling potential serialization errors."""
    try:
        if not isinstance(message, str):
            message = str(message)
        logger.log(level, message)
    except Exception as e:
        # Ensure error reporting does not crash the application
        print(f"Logging failure: {e}", file=sys.stderr)

# Example usage for python-utils-68
if __name__ == "__main__":
    app_logger = setup_logger("utils_logger")
    safe_log(app_logger, logging.INFO, "System initialized successfully")