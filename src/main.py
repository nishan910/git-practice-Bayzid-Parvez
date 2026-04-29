from datetime import datetime
from utils import add, subtract, multiply

# Print current project execution time
print(f"Project Run Time: {datetime.now()}")
print("-" * 35)

# Testing standard operations
print(f"Addition: {add(10, 5)}")
print(f"Subtraction: {subtract(10, 5)}")
print(f"Multiplication: {multiply(10, 5)}")

# Testing error handling with non-numeric input
print(f"Error Test Case: {add(10, 'abc')}")