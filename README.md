[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-68

A lightweight, zero-dependency Python utility toolkit designed to streamline common data transformation, file handling, and logging workflows. It eliminates redundant boilerplate code across Python projects by providing robust, battle-tested helper modules out of the box.

## Features

* **Safe Dot-Notation Extraction:** Fetch values from deeply nested dictionaries and JSON payloads safely without triggering `KeyError` or `AttributeError` exceptions.
* **Atomic File Operations:** Read, write, and update local files with built-in temporary buffering to prevent file corruption during execution failures.
* **Smart Data Formatters:** Instantly convert byte sizes, microsecond execution times, and Unix timestamps into human-readable strings.
* **Structured Console Logger:** Configurable, color-coded logging utility with built-in JSON output formatting for cloud monitoring environments.

## Installation

Install the package directly via `pip`:

```bash
pip install python-utils-68
```

Or install the latest development version from the repository:

```bash
git clone https://github.com/Developer/python-utils-68.git
cd python-utils-68
pip install .
```

## Quick Start

```python
from python_utils_68 import safe_get, format_bytes, AtomicWriter, get_logger

# Initialize structured logger
logger = get_logger("app_module")
logger.info("Initializing workflow...")

# Extract values from complex nested structures
payload = {
    "system": {
        "metrics": {
            "memory_usage": 1073741824
        }
    }
}

memory_bytes = safe_get(payload, "system.metrics.memory_usage", default=0)
print(f"Memory in use: {format_bytes(memory_bytes)}")
# Output: Memory in use: 1.00 GB

# Safely write data to disk
with AtomicWriter("output.txt", mode="w") as file:
    file.write("Processing completed successfully.")

logger.info("Task finished cleanly.")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.