# Create a simple menu that continues until user chooses to exit. 

# Display menu options to the user
# Use loop to keep program running until user chooses to exit

while True:
    print("Main Menu")
    print("1. Say Hallo")
    print("2. Add two numbers")
    print("3. Show countdown")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        name = input("Enter your name: ").title() # Using string methods to format input
        print(f"Hello, {name}!")

    elif choice == '2':
        first = input("Enter first number: ")
        second = input("Enter second number: ")

        if first.isdigit() and second.isdigit(): # Using string methods to validate input
            num1 = int(first)
            num2 = int(second)
            print(f"The sum is: {num1 + num2}")
        else:
            print("Invalid input. Please enter numeric values.")
    
    elif choice == '3':
        for i in range(5, 0, -1): # Using range to create a countdown
            print(i)
        print("Blast off!")

    elif choice == '4':
        print("Exiting the program. Goodbye!") # Breaking the loop to exit
        break

    else:
        print("Invalid choice. Please select a valid option.")