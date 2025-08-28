# Prompt user with a menu of options
print("Welcome to the cafe!")
print("Please choose from the following options:")
print("1. Coffee")
print("2. Tea")
print("3. Water")

# Get user choice and validate input
while True:
    choice = input("Enter the number of your choice: ")
    if not choice.isdigit():
        print("Invalid input. Please enter a number corresponding to your choice.")
    else:
        choice_num = int(choice)
        # Validate range
        if choice_num < 1 or choice_num > 3:
            print("Choice out of range. Please select a valid option (1-3).")
        else:
            if choice_num == 1:
                print("You selected Coffee. Enjoy your drink!")
                break
            elif choice_num == 2:
                print("You selected Tea. Enjoy your drink!")
                break
            elif choice_num == 3:
                print("You selected Water. Stay hydrated!")
                break