# Remake of Simple Calculator from Week 1, but now with input validation

print("Simple Calculator")

# Get user input with validation
while True:
    num1 = input("Enter first umber: ")
    if num1.replace('.', '', 1).isdigit() or num1.count('.') > 1: # Allows for one decimal point
        num1 = float(num1)
        break
    else:
        print("Invalid input. Please enter a valid number.")

# Get second number with validation
while True:
    num2 = input("Enter second number: ")
    if num2.replace('.', '', 1).isdigit() or num2.count('.') > 1: # Allows for one decimal point
        num2 = float(num2)
        break
    else:
        print("Invalid input. Please enter a valid number.")

# Get operation with validation
while True:
    operation = input("Choose operation (+, -, *, /): ")
    if operation in ['+', '-', '*', '/']:
        if operation == '/' and num2 == 0: # CHeck for division by zero
            print("Error: Division by zero is not allowed. Please enter a different second number.")
            while True:
                num2 = input("Enter second number: ")
                if num2.replace('.', '', 1).isdigit() or num2.count('.') > 1:
                    num2 = float(num2)
                    if num2 != 0:
                        break
                else:
                    print("Invalid input. Please enter a valid non-zero number.")
        break
    else:
        print("Invalid operation. Please choose from (+, -, *, /).")

# Perform calculation
if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/':
    print("Result:", num1 / num2)
else:
    print("Invalid operation")
        