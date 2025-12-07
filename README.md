# Calculator using Python

This project is a basic command-line calculator written in Python.  
It supports four operations:

- Addition
- Subtraction
- Multiplication
- Division

---

## How to Run the Calculator

Run the following command:

$ python calculator.py

You will be asked to enter:

1. First number
2. Operator (+, -, \*, /)
3. Second number

---

## Unit Testing

A simple test script is included to validate the calculator functions using Python's `pytest`.

To run the tests:

$ pytest -v

Expected output:

```
test_calculator.py::test_add PASSED                                                                            [ 25%]
test_calculator.py::test_subtract PASSED                                                                       [ 50%]
test_calculator.py::test_multiply PASSED                                                                       [ 75%]
test_calculator.py::test_divide PASSED                                                                         [100%]

================================================= 4 passed in 0.05s =================================================
```

---

## Project Structure

```
calc_app/
│
├── calculator.py         # Main calculator logic
├── test_calculator.py    # Unit tests
├── requirements.txt      # pytest and other requirements (if added in future)
├── .github/workflows/python-test.yml    # github actions workflow defined
└── README.md             # Project documentation
```

---

## GitHub Actions

Tests run automatically on every push and pull actions.

---

---

# Python Language Conventions

This README contains a comprehensive list of Python coding conventions based on PEP 8, PEP 20 (Zen of Python), and widely accepted industry practices.

---

## 1. Python Philosophy

Key ideas:

- Simple is better than complex
- Readability counts
- Explicit is better than implicit
- There should be one — and preferably only one — obvious way to do it

---

## 2. Naming Conventions

### Variables:

Use snake_case
Example: user_name, max_count

### Functions:

Use snake_case
Example: calculate_tax

### Classes:

Use PascalCase
Example: UserProfile

### Constants:

Use ALL_CAPS
Example: MAX_SPEED, PI

### Modules and Files:

Lowercase with underscores
Example: user_service.py, config_loader.py

### Private Members:

Prefix with underscore
Example: \_helper_function

---

## 3. Function Parameters

Positional parameters example:
def add(a, b)

Keyword parameters example:
def greet(name="Guest")

Variable-length arguments:
\*args inside a function allow multiple positional args
\*\*kwargs allow multiple keyword-value pairs

Keyword-only arguments:
def connect(host, \*, timeout=10)

---

## 4. Imports

### One import per line:

import os
import sys

### Preferred grouping:

1. Standard library
2. Third-party libraries
3. Local modules

### Avoid wildcard imports:

from module import \* (BAD PRACTICE)

---

## 5. Errors and Exceptions

Basic example:
try converting input
catch specific exceptions such as ValueError

Avoid catching broad Exception unless required

Raise descriptive exceptions:
raise ValueError("age must be positive")

Use finally for cleanup tasks:
closing files, releasing resources

---

## 6. Formatting

### Indentation:

Always use 4 spaces

### Line length:

Use a maximum of 79–120 characters per line based on style guide

### Spacing:

x = 5 (good)
x=5 (bad)

### Blank lines:

Two blank lines before top-level definitions
One blank line between class methods

---

## 7. Docstrings

### Functions:

Docstring describes purpose and behavior

### Classes:

Docstring describes what the class represents

### Modules:

Top-level docstring explains module purpose

---

## 8. Classes and OOP Guidelines

Prefer properties over getter/setter methods
Prefer composition over inheritance
Classes should remain small and focused

---

## 9. Type Hinting

Function annotations example:
add(a: int, b: int) -> int

Optional types example:
Optional[User]

---

## 10. Testing Conventions

### Test file naming:

test_add.py

### Basic pytest example:

assert add(2, 3) == 5

### Use Arrange–Act–Assert style

---

## 11. Logging

Use the built-in logging module instead of print for production code

---

## 12. Best Practices

- Avoid global variables
- Prefer list and dictionary comprehensions
- Keep functions simple and short
- Prefer explicit over implicit
- Use virtual environments
- Avoid unnecessary abstraction and overengineering
- Write meaningful and readable names
- Keep modules focused on a single purpose

---

# End of README
