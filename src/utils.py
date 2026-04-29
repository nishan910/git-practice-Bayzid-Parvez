# Utility functions for basic math operations with error handling

def add(a, b):
    # Error Handling: Check if inputs are numbers
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Error: Invalid input! Please provide numbers."
    return a + b

def subtract(a, b):
    # Error Handling: Check if inputs are numbers
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Error: Invalid input! Please provide numbers."
    return a - b

def multiply(a, b):
    # Error Handling: Check if inputs are numbers
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Error: Invalid input! Please provide numbers."
    return a * b