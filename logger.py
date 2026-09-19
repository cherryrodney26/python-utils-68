import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """Configures a rotating file logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Ensure directory exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Setup rotation: 5MB per file, keep 3 backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )

    # Formatter for consistent log output
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

if __name__ == "__main__":
    # Usage example
    app_logger = setup_logger("app", "logs/application.log")
    app_logger.info("logger initialized successfully")