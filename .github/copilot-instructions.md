# GitHub Copilot Instructions for this project

## Project Overview

This is a Python-based project using Test-Driven Development (TDD) with pytest for testing logic and related features.

## Project Structure

The project follows a clean TDD architecture with strict separation of concerns:
- `src/` - Contains the main business logic.
- `tests/test_*.py` - TDD test files that test the functionality of the code in `src/`
- `.gitignore` - Comprehensive ignore patterns for Python, IDE, and OS-specific files
- `pyproject.toml` - Modern Python project configuration and dependencies

**Note:** This project uses traditional TDD testing pattern with unit test files (`test_*.py`).

## Tools and Dependencies

This project uses pytest for testing. Key dependencies include:
- `pytest` - Testing framework
- `pytest-cov` - Code coverage plugin for pytest to measure test coverage
- Python 3.8+ for modern language features

## Code Coverage

The project should eventually achieve 100% code coverage using `pytest-cov`:
- All business logic in the `src/` directory is fully tested
- Coverage includes both statement and branch coverage
- HTML coverage reports are generated in the `htmlcov/` directory
- XML coverage reports are generated as `coverage.xml`
- Terminal coverage reports show complete coverage status

To run tests with coverage:
```bash
pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing
```

Coverage analysis tools:
- Run `python analyze_coverage.py` for detailed coverage analysis
- View HTML report: `htmlcov/index.html`

## TDD Testing Patterns

When working with TDD tests, follow these patterns:

1. Write a failing test that defines an incremental functional requirement.
2. Implement the minimum code required to make the test pass.
3. Refactor the code while keeping the tests green.
4. Stop to allow for code review and feedback.

Use test files to organize tests logically and avoid clutter, as described in the `tests/TEST_PLAN.md` file.

Use corresponding `tests/test_*.py` files described in the `tests/TEST_PLAN.md` file.

Use Arrange, Act, Assert comments within the test methods to clarify the test structure.

Keep the test methods short and focused on a single behavior.

Name the test methods descriptively to indicate the behavior being tested, for example:
- `test_calculate_with_valid_input_expect_proper_result`
- `test_calculate_with_invalid_input_expect_value_error`

## Exception Handling

In the code under test, use specific exceptions to indicate different error conditions:

Use `NotImplementedError` for unimplemented features or functionality.

Use `ValueError` built-in exception when an operation or function receives an argument that has the correct type but is an inappropriate or invalid value.

Use `RuntimeError` for business rule violations or calculations that cannot be performed with the given parameters.

## Testing Conventions

**Important**: This project exclusively uses TDD testing. All testing should go through the TDD workflow with corresponding `test_*.py` files.

## Code Organization

Keep business logic separate from test code.

## Project Maintenance

The project includes a comprehensive `.gitignore` file that excludes:
- Python bytecode and cache files (`__pycache__/`, `*.pyc`)
- Virtual environments (`.venv/`, `venv/`)
- IDE-specific files (VS Code, PyCharm)
- OS-specific files (macOS `.DS_Store`, Windows `Thumbs.db`)
- Testing artifacts (`.pytest_cache/`, coverage reports)

When adding new functionality, ensure:
1. TDD tests are created as `tests/test_*.py` files
2. Empty or unused test files are removed to keep the project clean
3. All new code paths are tested to maintain 100% coverage