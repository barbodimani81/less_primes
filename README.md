# Prime Numbers Generator with Logger

Welcome to the **Prime Numbers Generator with Logger** – a Python program that generates prime numbers up to a specified limit, while logging the function's execution.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Code Explanation](#code-explanation)
6. [Contributing](#contributing)
7. [License](#license)

## Overview

This project demonstrates the use of a logger decorator in Python to log the start and end of a function's execution. The main functionality includes generating prime numbers up to a user-specified limit and printing those numbers to the console.

## Features

- **Prime Number Generation**: Generates prime numbers up to a given limit.
- **Logging**: Logs messages indicating when a function starts and finishes.
- **Command Line Argument Parsing**: Uses argparse for command-line argument parsing.

## Installation

To get started with the **Prime Numbers Generator with Logger**, follow these steps:

1. **Clone the Repository** (if applicable):

    ```bash
    git clone https://github.com/yourusername/prime-numbers-generator-logger.git
    cd prime-numbers-generator-logger
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    This project does not require any external libraries other than the standard Python library.

## Usage

1. **Run the Script**:

    ```bash
    python main.py -n <integer>
    ```

    Replace `<integer>` with the number up to which you want to generate prime numbers. For example:

    ```bash
    python main.py -n 100
    ```

    The script will compute all prime numbers less than the specified number and print them to the console. You will also see log messages indicating the start and end of the `generate_primes` function.

## Code Explanation

### Logger Decorator

The `logger_decorator` logs the start and end of a function's execution:

```python
def logger_decorator(function):
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(message)s')
        logger = logging.getLogger()
        logger.info(f"Function started")
        result = function(*args, **kwargs)
        logger.info(f"Function finished")
        return result

    return wrapper
