# Define mathmatical functions

# Define a function to add two numbers
def add(a, b):
    return a + b

# Define a function to subtract two numbers
def subtract(a, b):
    return a - b

# Define a function to multiply two numbers
def multiply(a, b):
    return a * b

# Define a function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error! Division by zero." # Handle division by zero
    return a / b
# Call the functions with example inputs and print the results
print(add(5, 3))
print(subtract(5, 3))
print(multiply(5, 3))
print(divide(5, 3))
print(divide(5, 0))

