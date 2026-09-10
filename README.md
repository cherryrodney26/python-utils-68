# python-utils-68

`python-utils-68` is a collection of high-performance utility functions designed to streamline routine data processing and system automation tasks. This toolkit minimizes boilerplate code, allowing developers to focus on core logic rather than repetitive implementation details.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

*   **Robust File Operations:** Advanced wrappers for recursive directory traversal, rapid file pattern matching, and safe atomic writes.
*   **Performance Decorators:** Production-ready decorators for function memoization, execution timing, and configurable retry logic for transient errors.
*   **Data Serialization:** Simplified helpers for converting nested JSON structures to typed Python objects and vice-versa.
*   **System Helpers:** Cross-platform utilities for retrieving hardware metrics, process management, and environment variable sanitation.

## Installation

Install the package directly via pip:

```bash
pip install python-utils-68
```

Alternatively, if you are cloning the repository:

```bash
git clone https://github.com/developer/python-utils-68.git
cd python-utils-68
pip install -r requirements.txt
```

## Basic Usage

Quickly implement retries on network requests or IO-bound tasks using the `retry` utility:

```python
from pyutils68.decorators import retry

@retry(attempts=3, delay=2)
def fetch_data(url):
    # Function will retry automatically if an exception is raised
    return client.get(url)

# Utilize the filesystem helper
from pyutils68.io import safe_write

safe_write('config.json', {'status': 'active'})
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request for bug fixes or new utility suggestions. Ensure all new code includes corresponding unit tests in the `/tests` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.