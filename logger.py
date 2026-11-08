import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(
    name: str = "app",
    log_file: Optional[str] = "app.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 3,
    fmt: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
) -> logging.Logger:
    """Configures and returns a logger instance with standard output and rotation.

    Args:
        name: Identifier for the logger instance.
        log_file: Destination file path for log outputs.
        level: Logging threshold level.
        max_bytes: Size limit in bytes before log file rotates.
        backup_count: Number of rotated log files to keep.
        fmt: String format for log messages.

    Returns:
        logging.Logger: Configured logger with handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent handler duplication if already setup
    if logger.handlers:
        return logger

    formatter = logging.Formatter(fmt)

    # Stream handler for stdout
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating file handler
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
