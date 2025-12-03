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
