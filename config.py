import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and validation of application configurations."""
    
    def __init__(self, env_prefix: str = "APP_"):
        self.prefix = env_prefix

    def get_settings(self) -> Dict[str, Any]:
        """Extract environment variables prefixed with application settings."""
        return {
            key[len(self.prefix):].lower(): value
            for key, value in os.environ.items()
            if key.startswith(self.prefix)
        }

    @staticmethod
    def validate(config: Dict[str, Any], required_keys: list) -> bool:
        """Ensure essential configuration keys exist."""
        return all(key in config for key in required_keys)

# Global default configuration instance
default_config = ConfigLoader().get_settings()

def get_app_setting(key: str, default: Any = None) -> Any:
    """Access specific setting with fallback support."""
    return default_config.get(key, default)