import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(
    name: str,
    log_file: str,
    level: int = logging.INFO,
    max_bytes: int = 1048576,  # 1 MB
    backup_count: int = 5,
    log_to_console: bool = True
) -> logging.Logger:
    """
    Configures and returns a logger instance with rotating file support
    and optional stream logging to console.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if the logger is re-initialized
    if logger.hasHandlers():
        return logger

    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Ensure the parent directory for the log file exists
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    # Set up rotating file handler to prevent disk space exhaustion
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    file_handler.setFormatter(log_format)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    # Optional console output integration
    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)
        console_handler.setLevel(level)
        logger.addHandler(console_handler)

    return logger
