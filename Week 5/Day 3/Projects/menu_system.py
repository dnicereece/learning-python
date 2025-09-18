# Create a menu system using functions

# Define the menu
def menu():
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
# Define functions for each menu option
def option1():
    print("You selected Option 1")
def option2():
    print("You selected Option 2")
def option3():
    print("You selected Option 3")
def option4():
    print("Exiting the menu. Goodbye!")


# Define the main function to get user input and call the appropriate function
def main():
    while True:
        menu()
        choice = input("Please select an option (1-4): ")
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            option4()
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu system
if __name__ == "__main__":
    main()