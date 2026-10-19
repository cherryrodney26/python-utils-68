import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a standardized console logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_exception(logger: logging.Logger, msg: str, exc: Exception) -> None:
    """Utility to log formatted exception details."""
    logger.error(f"{msg}: {type(exc).__name__} - {str(exc)}", exc_info=True)

class LoggerManager:
    """Singleton-style access for project-wide logging."""
    _loggers = {}

    @classmethod
    def get(cls, name: str) -> logging.Logger:
        if name not in cls._loggers:
            cls._loggers[name] = get_logger(name)
        return cls._loggers[name]