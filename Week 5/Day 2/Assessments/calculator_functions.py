# Create a calculator calculator using only functions that return values
# Define a function that performs addition, subtraction, multiplication, and division
def calc(a, b):
    add = a + b
    sub = a - b
    mult = a * b
    div = a / b if b != 0 else "Error! Division by zero." # Handle division by zero
    return add, sub, mult, div

# Define main function to call calc and print results
def main():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ").strip() # Get user selection
        if choice == '5':
            print("Goodbye.")
            break

        if choice in ['1', '2', '3', '4']: # Validate operation choice
            while True:
                try:
                    num1 = float(input("Enter first number: ")) # Get and validate numbers
                    num2 = float(input("Enter second number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")

            results = calc(num1, num2) # Call calc function
            operations = { # Map choices to operation names
                '1': "Addition",
                '2': "Subtraction",
                '3': "Multiplication",
                '4': "Division"
            }
            print(f"{operations[choice]} Result: {results[int(choice)-1]}") # Print the result of the chosen operation (-1 for zero-based index)
        else:
            print("Invalid selection. Please choose from (1, 2, 3, 4, or 5).")
            continue

if __name__ == "__main__":
    main()# Call the main function to run the calculator