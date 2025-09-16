# Create a calculator function to perform basic arithmetic operations

# Define a function that performs addition, subtraction, multiplication, and division
def calc(a, b):
    add = a + b
    sub = a - b
    mult = a * b
    div = a / b if a and b != 0 else "Error! Division by zero." # Handle division by zero
    return add, sub, mult, div
    # 'Results' is a tuple containing results of all operations [add(0), sub(1), mult(2), div(3)]

# Call the function with example inputs and print the results
results = calc(10, 2)
print(f"Addition: {results[0]}")
print(f"Subtraction: {results[1]}")
print(f"Multiplication: {results[2]}")
print(f"Division: {results[3]}")
