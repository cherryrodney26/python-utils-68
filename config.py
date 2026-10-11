import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """Handles loading and merging of configuration settings."""

    def __init__(self, env_prefix: str = "APP_") -> None:
        self.env_prefix: str = env_prefix
        self.settings: Dict[str, Any] = {}

    def load_from_env(self) -> None:
        """Loads environment variables into the settings dictionary."""
        for key, value in os.environ.items():
            if key.startswith(self.env_prefix):
                config_key = key[len(self.env_prefix):].lower()
                self.settings[config_key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a configuration value with a default fallback."""
        return self.settings.get(key, default)

    def set_override(self, key: str, value: Any) -> None:
        """Manually sets a configuration value."""
        self.settings[key] = value

def get_default_config() -> Dict[str, str]:
    """Returns basic default configuration values."""
    return {
        "debug": "false",
        "version": "1.0.0",
        "log_level": "INFO"
    }