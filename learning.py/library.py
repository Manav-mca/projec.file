# library in python code

"""
A simple Python library example
"""

__version__ = "1.0.0"
__author__ = "Your Name"

class Calculator:
    """Simple calculator class"""
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

# Make classes and functions available when importing
__all__ = ['Calculator', 'greet']


# main.py (to test your library)
from library import Calculator, greet

# Use the calculator
calc = Calculator()
print(calc.add(5, 3))  # Output: 8
print(calc.divide(10, 2))  # Output: 5.0

# Use the greeting function
print(greet("manav"))

