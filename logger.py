import logging
import sys
from typing import Optional

class AppLogger:
    """Standardized logging utility for python-utils-68."""

    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def get_logger(self) -> logging.Logger:
        """Access the underlying logger instance."""
        return self.logger

def get_module_logger(name: str) -> logging.Logger:
    """Factory function for consistent module logging."""
    return AppLogger(name).get_logger()