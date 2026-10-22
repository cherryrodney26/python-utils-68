import functools
from itertools import islice
from typing import Any, Callable, Generator, Iterable, List, Optional


class FastBatchProcessor:
    """High-performance batch processing engine with memoized transforms."""

    def __init__(self, batch_size: int = 1000) -> None:
        if batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")
        self.batch_size = batch_size

    @functools.lru_cache(maxsize=4096)
    def _memoized_transform(self, item: Any, transform_fn: Callable[[Any], Any]) -> Any:
        """Cache repeated transformations on identical data elements."""
        return transform_fn(item)

    def chunk_iterable(self, iterable: Iterable[Any]) -> Generator[List[Any], None, None]:
        """Yield successive chunks from iterable without loading full stream into memory."""
        iterator = iter(iterable)
        while True:
            chunk = list(islice(iterator, self.batch_size))
            if not chunk:
                break
            yield chunk

    def process_stream(
        self,
        data_stream: Iterable[Any],
        transform_fn: Callable[[Any], Any],
        filter_fn: Optional[Callable[[Any], bool]] = None,
    ) -> Generator[Any, None, None]:
        """Stream processing pipeline utilizing batched chunks and cached transforms."""
        for batch in self.chunk_iterable(data_stream):
            items = (item for item in batch if filter_fn(item)) if filter_fn else batch
            for item in items:
                yield self._memoized_transform(item, transform_fn)

    def clear_cache(self) -> None:
        """Reset internal transformer lookup cache."""
        self._memoized_transform.cache_clear()
