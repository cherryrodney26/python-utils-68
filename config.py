import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class AppConfig:
    """Centralized application configuration management."""
    env: str
    debug: bool
    max_retries: int

    @classmethod
    def load_from_env(cls) -> 'AppConfig':
        """Initialize config from environment variables."""
        return cls(
            env=os.getenv("APP_ENV", "development"),
            debug=os.getenv("DEBUG", "true").lower() == "true",
            max_retries=int(os.getenv("MAX_RETRIES", "3")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Export configuration as a dictionary."""
        return {
            "environment": self.env,
            "debug_mode": self.debug,
            "retry_limit": self.max_retries
        }

def get_default_config() -> AppConfig:
    """Factory function for standard config retrieval."""
    return AppConfig.load_from_env()