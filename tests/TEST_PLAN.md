# Spreadsheet - Python Tests

The `tests` directory contains Python _pytest_ tests.

## Test Structure

- `test_simple_spreadsheet.py` - Basic spreadsheet operations
- `test_formulas.py` - Formula parsing and calculation
- `test_dependencies.py` - Cell references and dependencies
- `test_circular_references.py` - Circular reference handling

## Notes

- The tests assume a `Sheet` class will be implemented in a `src/sheet.py` file
- The test code should follow the Pytest testing framework conventions

## Detailed Test Documentation

### 1. Test Simple Spreadsheet

Test module for basic spreadsheet operations:
- Test that cells return empty string by default.
- Test that text values can be stored and retrieved from cells.
- Test that multiple cells can store different values independently.
- Test that numeric values are properly handled.
- Test that literal values can be retrieved for editing purposes.

### 2. Test Formulas

Test module for formula parsing and calculation:
- Test that formulas must start with '=' without leading space.
- Test basic constant formula evaluation.
- Test formula evaluation with parentheses.
- Test formula evaluation with nested parentheses.
- Test multiplication operations.
- Test addition operations.
- Test operator precedence (multiplication before addition).
- Test complex expression with mixed operations and parentheses.
- Test error handling for malformed formulas.
- Test error handling for unmatched parentheses.

### 3. Test Dependencies

Test module for cell references and dependency management:
- Test basic cell reference in formulas.
- Test that changes to referenced cells propagate to dependent cells.
- Test complex formulas with multiple cell references.
- Test that changes propagate through multiple levels of dependencies.
- Test complex interdependent formulas with multiple cells.

### 4. Test Circular References

Test module for circular reference detection and handling:
- Test that circular references don't cause the system to crash.
- Test that circular references are properly detected and reported.
