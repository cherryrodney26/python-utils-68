import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a standardized logger instance."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger

def log_execution_time(logger: logging.Logger, func_name: str, elapsed: float) -> None:
    """Utility to log function duration."""
    logger.info(f"Function '{func_name}' completed in {elapsed:.4f} seconds")

def setup_debug_logging() -> None:
    """Global override to enable debug mode for all app loggers."""
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    for handler in root.handlers:
        handler.setLevel(logging.DEBUG)