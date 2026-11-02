import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Returns a configured logger instance with standard formatting.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_exception(logger: logging.Logger, message: str, exc: Exception) -> None:
    """
    Utility for consistent error logging with exception traceback.
    """
    logger.error(f"{message}: {str(exc)}", exc_info=True)

def setup_basic_logging(level: int = logging.INFO) -> None:
    """
    Global configuration for basic logging setup.
    """
    logging.basicConfig(
        level=level,
        format='%(levelname)s: %(message)s',
        stream=sys.stdout
    )