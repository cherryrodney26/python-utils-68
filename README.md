# python-utils-68

A collection of lightweight, high-performance Python utilities designed to streamline common development tasks. This library focuses on reducing boilerplate code for file handling, data transformation, and environment configuration.

## Features

*   **Robust File Operations:** Simplified decorators for recursive file traversal and thread-safe batch processing of large directories.
*   **Data Transformation:** Built-in sanitization and schema-validation helpers for cleaning messy CSV/JSON exports.
*   **Env Manager:** A zero-dependency configuration loader that prioritizes environment variables and defaults over `.env` file reading.
*   **Performance Metrics:** Decorator-based execution timing and memory logging for benchmarking production code in real-time.

## Installation

Install `python-utils-68` directly via pip:

```bash
pip install python-utils-68
```

Alternatively, if you are working within a requirements-based workflow:

```bash
echo "python-utils-68==1.0.4" >> requirements.txt
pip install -r requirements.txt
```

## Usage

Below is a quick example of how to use the built-in performance decorator to monitor function execution:

```python
from pyutils68.metrics import time_execution
from pyutils68.files import secure_load

@time_execution
def process_data(file_path):
    data = secure_load(file_path)
    # ... logic here ...
    return data

result = process_data("data/input.json")
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Developed by Developer. Built for reliability and performance.*