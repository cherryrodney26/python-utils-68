import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'app.log', level: int = logging.INFO) -> logging.Logger:
    """
    Configures a rotating file logger for general application use.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        # Format: timestamp - name - level - message
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate at 5MB, keep 3 backup files
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)

        # Console output for visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

if __name__ == '__main__':
    log = setup_logger('dev_logger')
    log.info('logger initialization successful')