# System Design - Spreadsheet Dojo

## Overview

The Spreadsheet is a Python module that implements **basic spreadsheet functionality** with a focus on formula parsing and cell dependency management. This project serves as a learning exercise for building a rudimentary spreadsheet engine from scratch, emphasizing test-driven development practices.

## Goals

The system solves the following core problems:

- **Cell Data Storage**: Store and retrieve text and numeric values in named cells (e.g., "A1", "B2")
- **Formula Engine**: Parse and evaluate mathematical expressions with proper operator precedence
- **Dependency Management**: Automatically recalculate dependent cells when referenced cells change
- **Error Handling**: Gracefully handle formula syntax errors and circular references
- **Literal Value Access**: Provide access to raw cell values for editing purposes

## Architecture

### Core Components

```
┌─────────────────┐    ┌─────────────────┐    ┌──────────────────┐
│     Sheet       │    │  FormulaParser  │    │ DependencyGraph  │
│                 │    │                 │    │                  │
│ - cells: dict   │◄──►│ - parse()       │◄──►│ - track_deps()   │
│ - get()         │    │ - evaluate()    │    │ - update()       │
│ - put()         │    │ - validate()    │    │ - detect_cycles()│
│ - get_literal() │    │                 │    │                  │
└─────────────────┘    └─────────────────┘    └──────────────────┘
```

### Data Flow

1. **Input**: User provides cell reference and value via `put(cell, value)`
2. **Storage**: Raw value stored with cell reference as key
3. **Analysis**: If value starts with "=", parse as formula
4. **Evaluation**: Calculate result using formula parser
5. **Dependencies**: Update dependency graph for cell references
6. **Propagation**: Recalculate dependent cells automatically

## Usage Examples

### Basic Operations

```python
from sheet import Sheet

# Create a new spreadsheet
sheet = Sheet()

# Store simple values
sheet.put("A1", "Hello World")
sheet.put("B1", "42")

# Retrieve values
print(sheet.get("A1"))  # Output: "Hello World"
print(sheet.get("B1"))  # Output: "42"

# Access literal values for editing
print(sheet.get_literal("A1"))  # Output: "Hello World"
```

### Formula Operations

```python
# Basic arithmetic
sheet.put("A1", "10")
sheet.put("A2", "=A1 + 5")
print(sheet.get("A2"))  # Output: "15"

# Complex expressions with precedence
sheet.put("B1", "=7 + 2 * 3")
print(sheet.get("B1"))  # Output: "13"

# Parentheses and nested operations
sheet.put("C1", "=7 * (2 + 3) * ((2 + 1))")
print(sheet.get("C1"))  # Output: "105"
```

### Cell Dependencies

```python
# Create dependent cells
sheet.put("A1", "8")
sheet.put("A2", "=A1 * 2")
sheet.put("A3", "=A2 + 10")

print(sheet.get("A3"))  # Output: "26"

# Change source cell - dependencies auto-update
sheet.put("A1", "12")
print(sheet.get("A3"))  # Output: "34" (automatically recalculated)
```

### Error Handling

The system uses Python's exception handling mechanism to provide robust error reporting and recovery capabilities.

- Formula syntax errors - raises ValueError with detailed message
- Circular references - raises ValueError with cycle detection
- Unmatched parentheses - raises ValueError with specific error
- Invalid cell references - raises ValueError for input validation
- Graceful error handling in applications

#### Exception Types and Handling

| **Error Type** | **Exception** | **Description** | **Recovery Strategy** |
|----------------|---------------|-----------------|----------------------|
| **Syntax Errors** | `ValueError` | Invalid formula syntax | Catch and prompt user to fix |
| **Circular References** | `ValueError` | Cell dependency loops | Catch and break dependency |
| **Invalid Input** | `ValueError` | Empty/invalid cell references | Catch and validate input |
| **Division by Zero** | `ValueError` | Mathematical errors | Catch and handle gracefully |

#### Benefits of Exception-Based Error Handling

1. **Detailed Error Information**: Exceptions provide specific error messages and context
2. **Programmatic Handling**: Applications can catch and handle errors appropriately
3. **Python Idiomatic**: Follows Python's "Easier to Ask for Forgiveness than Permission" (EAFP) principle
4. **Fail Fast**: Prevents silent failures and data corruption
5. **Debugging Support**: Stack traces help identify error sources

## Implementation Requirements

### Core Class: `Sheet`

```python
class Sheet:
    def get(self, cell_ref: str) -> str:
        """Get the calculated value of a cell."""
        pass
    
    def put(self, cell_ref: str, value: str) -> None:
        """Set the value of a cell."""
        pass
    
    def get_literal(self, cell_ref: str) -> str:
        """Get the raw/literal value of a cell for editing."""
        pass
```

### Key Features

- **Cell References**: Support standard spreadsheet notation (A1, B2, ZX347)
- **Formula Parsing**: Recursive descent or operator precedence parsing
- **Numeric Handling**: Automatic number formatting (strip whitespace)
- **Dependency Tracking**: Directed acyclic graph for cell relationships
- **Circular Detection**: Identify and report circular references
- **Error Recovery**: Graceful handling of malformed expressions

## Testing Strategy

The system is designed with comprehensive test coverage achieving 100% code coverage:

1. **Basic Operations** - Cell storage and retrieval with input validation
2. **Formula Engine** - Mathematical expression evaluation with all arithmetic operations
3. **Dependencies** - Cell reference and multi-level propagation logic
4. **Error Handling** - Exception-based error handling for all error conditions
5. **Edge Cases** - Boundary conditions, malformed input, and circular references
6. **Interface Testing** - Public API methods with type validation

## Future Enhancements

- Support for additional mathematical functions (SUM, AVERAGE, MIN, MAX, etc.)
- Range operations (A1:B10) for batch calculations
- String manipulation functions (CONCAT, LEFT, RIGHT, etc.)
- Date/time operations and formatting
- Import/export capabilities (CSV, Excel)
- Performance optimizations for large spreadsheets
- Multi-sheet support
- User interface integration
