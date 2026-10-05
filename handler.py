from typing import Any, Dict, Optional, Callable

class RequestHandler:
    """Handles incoming request processing and lifecycle management."""

    def __init__(self, timeout: int = 30) -> None:
        """Initialize handler with a specific timeout duration."""
        self.timeout: int = timeout
        self.hooks: Dict[str, Callable[[Any], None]] = {}

    def register_hook(self, name: str, callback: Callable[[Any], None]) -> None:
        """Register a callback function for a specific lifecycle event."""
        self.hooks[name] = callback

    def process(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Execute processing logic for provided data dictionary."""
        if not data:
            return None

        if "pre_process" in self.hooks:
            self.hooks["pre_process"](data)

        result: Dict[str, Any] = {
            "status": "success",
            "processed": True,
            "payload": data
        }

        if "post_process" in self.hooks:
            self.hooks["post_process"](result)

        return result

    def get_config(self) -> Dict[str, int]:
        """Retrieve current handler configuration parameters."""
        return {"timeout": self.timeout}