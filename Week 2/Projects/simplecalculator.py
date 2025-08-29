# Calculator requiring type conversion

print("Simple Calculator")
num1 = input("Enter first number: ")  # input returns a string
num2 = input("Enter second number: ")

# Convert input strings to float for calculation
num1 = float(num1)
num2 = float(num2)

operation = input("Choose operation (+, -, *, /): ")

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

value = input("Enter something: ")
print(type(value))