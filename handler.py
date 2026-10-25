import logging
import os
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class DataHandler:
    def __init__(self, directory: str = "./data"):
        self.directory = directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def process_payload(self, payload: Dict[str, Any]) -> bool:
        """Validate and persist incoming data dictionary."""
        if not payload or "id" not in payload:
            logger.error("Invalid payload structure: missing id")
            return False
        
        try:
            file_path = os.path.join(self.directory, f"{payload['id']}.json")
            import json
            with open(file_path, "w") as f:
                json.dump(payload, f, indent=4)
            return True
        except (IOError, TypeError) as e:
            logger.error(f"Failed to write data for {payload['id']}: {e}")
            return False

    def cleanup_old_files(self, max_files: int = 10) -> None:
        """Keep directory size manageable by removing oldest files."""
        files = [os.path.join(self.directory, f) for f in os.listdir(self.directory)]
        files.sort(key=os.path.getmtime)
        
        if len(files) > max_files:
            for file_to_remove in files[:-max_files]:
                os.remove(file_to_remove)
                logger.info(f"Removed stale file: {file_to_remove}")
