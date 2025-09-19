# Create math utilities using functions with proper docstrings

# Addition
def add(a, b) -> float | int:
    """
    Adds two numbers and returns the result.

    Arguments:
        a (int, float): The first number.
        b (int, float): The second number.
    
    Returns:
        int, float: The sum of the two numbers.
    """
    return a + b
# Subtraction
def subtract(a, b) -> float | int:
    """
    Subtracts the second number from the first.

    Arguments:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int, float: The result of the subtraction.
    """
    return a - b
# Multiplication
def multiply(a, b) -> float | int:
    """
    Multiplies two numbers and returns the result.

    Arguments:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int, float: The product of the two numbers.
    """
    return a * b
# Division
def divide(a, b) -> float | int:
    """
    Divides the first number by the second.

    Arguments:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int, float: The result of the division.
    """
    if b != 0:
        return a / b
    else:
        return "Division by zero error"
# Exponentiation
def power(a, b) -> float | int:
    """
    Raises the first number to the power of the second.

    Arguments:
        a (int, float): The base number.
        b (int, float): The exponent.

    Returns:
        int, float: The result of the exponentiation.
    """
    return a ** b
# Factorial
def factorial(n) -> int:
    """
    Calculates the factorial of a non-negative integer.

    Arguments:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
# Example usage
print(add(5, 3))        # Output: 8
print(subtract(5, 3))   # Output: 2
print(multiply(5, 3))   # Output: 15
print(divide(5, 0))     # Output: Division by zero error
print(power(2, 3))      # Output: 8
print(factorial(5))     # Output: 120