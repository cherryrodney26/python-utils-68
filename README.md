# python-utils-68

A collection of lightweight, high-performance utility functions designed to streamline repetitive Python development tasks. This library focuses on simplifying data manipulation, file system operations, and system logging for production-ready applications.

## Features

*   **Robust File Operations:** Advanced directory traversal and recursive file processing tools with built-in error handling.
*   **Performance Decorators:** A suite of timing and memoization decorators to profile and optimize CPU-intensive functions.
*   **Data Validation:** Simplified schema validation tools for dictionaries and environment configuration objects.
*   **Smart Logging:** Configurable logging helpers that automate file rotation and color-coded console output.

## Installation

Install the package directly via pip:

```bash
pip install python-utils-68
```

Alternatively, include it in your `requirements.txt`:

```text
python-utils-68>=1.0.0
```

## Basic Usage

Import the utility modules to handle common tasks with minimal boilerplate code.

```python
from pyutils68 import timer, file_manager

# Measure execution time of any function
@timer
def process_data(data):
    # Perform intensive operations
    return [d * 2 for d in data]

# Recursively clean up temp files in a directory
file_manager.delete_by_extension('./cache', '.tmp')

process_data([1, 2, 3, 4])
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.