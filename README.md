# python-utils-68

A lightweight collection of robust, production-ready Python helper functions designed to streamline repetitive coding tasks. This utility suite focuses on performance, type safety, and minimizing boilerplate across diverse data processing workflows.

## Features

*   **FileSystem Streamliner:** Simplify directory traversal and file manipulation with atomic path operations and recursive pattern matching.
*   **Dict-Object Mapper:** Seamlessly convert nested dictionaries to attribute-access objects for cleaner configuration management.
*   **Performance Decorators:** Built-in tools for easy execution timing, memoization, and retry logic with exponential backoff.
*   **String Sanitizer:** Efficient text normalization tools to strip whitespace, clean Unicode artifacts, and validate input formats.

## Installation

Install `python-utils-68` directly via pip:

```bash
pip install python-utils-68
```

Alternatively, if you are cloning the repository:

```bash
git clone https://github.com/Developer/python-utils-68.git
cd python-utils-68
pip install -r requirements.txt
```

## Basic Usage

Integrate utility modules into your existing scripts with minimal overhead:

```python
from pyutils68 import timers, sanitizers

# Measure function performance automatically
@timers.measure_execution_time
def process_data(data):
    return [sanitizers.normalize_text(i) for i in data]

data = ["  Hello World! ", "  Python-Utils-68 "]
clean_data = process_data(data)

print(clean_data)
# Output: ['Hello World!', 'Python-Utils-68']
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.