# Pytest VDD Spreadsheet

For training Pytest verifier-driven development (VDD), this is a starter module (spreadsheet) that starts with specifications.

Based on coding challenges:
1. _Coding Dojo: Test First Spreadsheet_ by [Joe Wright](https://github.com/joejag) https://code.joejag.com/coding-dojo/test-first-spreadsheet/
2. _Test-First Challenge: Spreadsheet_ by [Bill Wake](https://github.com/wwake) https://xp123.com/test-first-challenge/

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Using virtual environment venv

Python virtual environments enable you to set up a Python sandbox with its own set of packages separate from the system site-packages in which to work.

#### Create

```bash
$ python -m venv .venv
```

#### Activate

To activate on macOS and Linux.
```bash
$ source .venv/bin/activate
```

To activate on Windows.
```bash
$ .venv\Scripts\activate.bat
```

To activate on Windows with PowerShell.
```bash
$ .venv\Scripts\Activate.ps
```

#### Deactivate

When done with the virtual environment, run:
```bash
$ deactivate
```

### Setup Instructions

Install dependencies:
```bash
pip install pytest pytest-cov
```

## Tests

### Running Tests

**Run all BDD tests:**
```bash
pytest tests/ -v
```

**Run tests with coverage:**
```bash
pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing
```

## Problem Statement

A Python implementation of **basic spreadsheet functionality** with formula parsing and cell dependency management. This project demonstrates test-driven development practices for building a spreadsheet engine from scratch.

### Features

- **Cell Data Management**: Store and retrieve text/numeric values in named cells
- **Formula Engine**: Parse and evaluate mathematical expressions with operator precedence
- **Dependency Tracking**: Automatic recalculation when referenced cells change  
- **Error Handling**: Graceful handling of syntax errors and circular references
- **Test-Driven Design**: Comprehensive test suite with Python pytest tests

### Documentation

- **[Functional Specification](docs/FUNC_SPEC.md)** - Business requirements and functional specifications
- **[System Design](docs/SYSTEM_DESIGN.md)** - High-level architecture, usage examples, and implementation requirements
- **[Test Plan](tests/TEST_PLAN.md)** - Comprehensive test suite documentation and methodology

## Usage

### As a Library

```python
from sheet import Sheet

# Create spreadsheet and add data
sheet = Sheet()
sheet.put("A1", "10")
sheet.put("A2", "=A1 * 2 + 5")

print(sheet.get("A2"))  # Output: "25"

# Change dependency - auto-recalculates
sheet.put("A1", "20") 
print(sheet.get("A2"))  # Output: "45"
```

## Project Structure

```
spreadsheet_dojo/
├── docs/                   # Documentation
│   ├── SYSTEM_DESIGN.md    # High-level system design
│   └── FUNC_SPEC.md        # Functional specification
├── src/                    # Python source code
└── tests/                  # Python pytest test suite
    └── TEST_PLAN.md        # Test documentation and methodology
```

## Learning Objectives

This coding dojo focuses on:

- **Test-Driven Development**: Write tests first, implement to make them pass
- **Formula Parsing**: Implement recursive descent or operator precedence parsing
- **Dependency Management**: Build and maintain cell reference graphs
- **Error Handling**: Graceful degradation with circular references and syntax errors
- **Clean Architecture**: Separation of concerns between storage, parsing, and evaluation

## Background Reading

For formula parsing implementation, research:
- **Recursive Descent Parsing** - Top-down parsing technique
- **Operator Precedence Parsing** - Handles mathematical operator priority
- **Abstract Syntax Trees** - Representing parsed expressions
- **Dependency Graphs** - Managing cell relationships

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

**Note**: This project is designed as a learning exercise for understanding spreadsheet engines, parsing techniques, and test-driven development practices.
