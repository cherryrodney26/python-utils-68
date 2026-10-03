import functools
import logging

# internal cache for performance optimization
_cache = {}

class DataProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @staticmethod
    @functools.lru_cache(maxsize=1024)
    def process_item(item_id: int) -> dict:
        """computes heavy data transformation with lru caching"""
        # simulate resource intensive operation
        result = {"id": item_id, "data": [i * 2 for i in range(1000)]}
        return result

    def batch_process(self, item_ids: list) -> list:
        """efficient processing using list comprehension and cache"""
        return [self.process_item(i) for i in item_ids]

    def clear_cache(self):
        """manual memory management for internal caches"""
        self.process_item.cache_clear()
        self.logger.info("core module cache cleared")

def get_instance():
    """singleton pattern for data processor"""
    if not hasattr(get_instance, "_instance"):
        get_instance._instance = DataProcessor()
    return get_instance._instance