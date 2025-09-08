# Create a program that calculates and outputs the result of an arithmetic operation based on user input.
expression = input("Enter an arithmetic expression (e.g., 3 + 4): ")

x, y, z = expression.split()
x = int(x)
z = int(z)

if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    print(float(x / z))
else:
    print("Invalid operator")



