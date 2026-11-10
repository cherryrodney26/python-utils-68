[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-68

`python-utils-68` is a lightweight, high-performance collection of helper functions designed to streamline common Python development workflows. It simplifies routine data transformation, file system operations, and execution handling without introducing heavy third-party dependencies.

## Features

* **Smart File I/O:** Thread-safe JSON and YAML utilities with automatic parent directory creation and atomic writes.
* **Data Masking:** Fast sanitization routines for obfuscating sensitive PII, such as emails, credit cards, and phone numbers in log strings.
* **Resilient Execution:** Configurable retry decorators featuring exponential backoff and jitter for network calls.
* **Performance Benchmarking:** Context managers to measure code block execution time and memory usage with minimal overhead.

## Installation

Install the package directly via `pip`:

```bash
pip install python-utils-68
```

Or install locally for development:

```bash
git clone https://github.com/Developer/python-utils-68.git
cd python-utils-68
pip install -e .
```

## Quick Start

```python
from python_utils_68.io import safe_save_json
from python_utils_68.security import mask_email
from python_utils_68.decorators import retry

# 1. Obfuscate sensitive strings
user_email = "developer@example.com"
print(mask_email(user_email))  # Output: d***r@example.com

# 2. Retry flaky operations automatically
@retry(max_attempts=3, delay=1.0, backoff=2.0)
def fetch_remote_data():
    # Simulated API call
    return {"status": "success", "user": user_email}

data = fetch_remote_data()

# 3. Write data atomically to disk
safe_save_json("output/data.json", data, indent=2)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.