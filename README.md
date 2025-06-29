# Expression Evaluator

A **Terminal-Based Mathematical Expression Evaluator** built using pure Python. This program parses and computes mathematical expressions with correct operator precedence, bracket handling, and error detection like a basic calculator.

## Features

- Supports:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`, `×`, `x`, `X`)
  - Division (`/`, `÷`)
  - Exponentiation (`^`)
- Handles:
  - Nested brackets `()`
  - Unary operators (`-5 + 2`, `+4-3`)
  - Operator precedence (`BODMAS/PEMDAS`)
- Error Handling:
  - Mismatched brackets
  - Zero Division Error
  - Invalid characters
  - Invalid operator sequences (`++`, `**/`, etc.)

##  How to Run

1. **Clone or Download the Repository**

   Save the file as `calculator.py`

2. **Run the Script:**

   ```bash
   python calculator.py
   ```

3. **Input Example:**

   ```
   Enter Expression: (5 + 3) * (2 ^ (4 - 2))
   ```

   Output:

   ```
   32.0
   ```

## Example Expressions

| Input                                    | Output |
|-------------------------------------------|--------|
| `5 + 3 * 2`                              | 11.0   |
| `(5 + 3) * 2`                            | 16.0   |
| `4 ^ (2 + 1)`                            | 64.0   |
| `((3 + 2) * (7 - 5)) ^ 2`                 | 100.0  |
| `5 + --3` *(double minus handled as plus)*| 8.0    |
| `5 + 3x4` *(multiplication with 'x')*     | 17.0   |

##  Error Handling Examples

| Problem                        | Example      | Error Message                        |
|---------------------------------|--------------|---------------------------------------|
| Mismatched Brackets             | `(5 + 3`     | Close all the Brackets !!            |
| Invalid Character               | `5 + @ 3`    | `@ Cant Be Evaluated !!`             |
| Operator at End                 | `5 + 3 *`    | Expression Ends With An Operator !!   |
| Invalid Operator Sequence       | `5 ** / 3`   | `**/ Cant Be Evaluated !!`           |
| Division by Zero                | `5 / 0`      | Zero Division Error                  |

## Function Overview

| Function                | Purpose                                                        |
|-------------------------|----------------------------------------------------------------|
| `in_put()`              | Cleans, formats, and parses raw input into a standardized form.|
| `check_errors()`        | Validates syntax, brackets, and operators.                     |
| `list_maker()`          | Converts the expression string into a list of tokens.          |
| `unary_minus()`         | Handles unary minus and plus.                                  |
| `exponent_function()`   | Computes exponentiation (`^`).                                 |
| `division_function()`   | Processes division (`/`, `÷`) with zero division handling.     |
| `multiplication()`      | Computes multiplication (`*`, `×`, `x`, `X`).                  |
| `plus_minus()`          | Performs addition and subtraction.                             |
| `expression_evaluator()`| Evaluates the tokenized expression respecting precedence.      |
| `bracket_evaluator()`   | Handles nested brackets recursively.                           |
| `evaluate()`            | Main function to call for evaluating expressions.              |

## How to Use in Other Python Programs

```python
from calculator import evaluate

result = evaluate("3 + (2 * 5) ^ 2")
print("Result:", result)
```

## 🔧 Requirements

- Python 3.x
- No external libraries required

## Future Improvements

- Add support for:
  - Mathematical functions (`sin()`, `cos()`, `sqrt()`)
  - Factorial (`!`)
  - Modulus (`%`)
- Implement a GUI or Web-based interface
- Improve error reporting with line/index pointers

##  License

This project is open-source and free to use under the **MIT License**.

##  Contributions

Suggestions, bug reports, and contributions are welcome.
