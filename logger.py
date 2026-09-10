import logging
import sys
from typing import Optional

class AppLogger:
    """Standardized application logger setup."""

    def __init__(self, name: str = "python-utils-68", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        """Configure console output formatting."""
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

def get_default_logger(name: str = "python-utils-68") -> logging.Logger:
    """Factory function for global logger access."""
    return AppLogger(name).get_logger()