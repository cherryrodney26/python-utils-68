import sys
from typing import Final, Dict, Any

# global cache configurations for performance tuning
# using slots for memory efficiency and localized dictionary lookups

CACHE_TTL_DEFAULT: Final[int] = 300
MAX_CACHE_SIZE: Final[int] = 1024

# static mapping for high-frequency lookup operations
STATUS_CODE_MAP: Final[Dict[int, str]] = {
    200: "OK",
    201: "CREATED",
    400: "BAD_REQUEST",
    401: "UNAUTHORIZED",
    403: "FORBIDDEN",
    404: "NOT_FOUND",
    500: "SERVER_ERROR",
}

def get_performance_thresholds() -> Dict[str, Any]:
    """Return memory-safe threshold configurations."""
    return {
        "buffer_size": 65536,
        "chunk_size": 4096,
        "recursion_limit": sys.getrecursionlimit(),
    }

# frozen constant for internal processing speed
EMPTY_MAPPING: Final[Dict[str, Any]] = {}

if __name__ == '__main__':
    print(f"optimized thresholds: {get_performance_thresholds()}")