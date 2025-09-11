# Create a menu driven calculator
print("Welcome to the Calculator.")
# Add menu options in loop until user exits
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Get user selection
    choice = input("Enter the type of calculations you would like to complete, or exit: ").strip()

    if choice == '5':
        print("Goodbye.")
        break

    # Get user input with validation
    while True:
        num1 = input("Enter first number: ")
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
        if choice in ['1', '2', '3', '4']:
            if choice == '4' and num2 == 0: # Check for division by zero
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
            print("Invalid selection. Please choose from (1, 2, 3, 4, or 5).")

    # Perform calculation
    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        print("Result:", num1 / num2)
    else:
        print("Invalid operation")