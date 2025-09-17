# Print stars, triangles, and pyramids using nested loops
print("Let's print some patterns!")
# Define functions for each pattern
def print_stars(rows):
    for i in range(rows):
        print("*" * (i + 1)) # Print stars

def print_triangles(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1)) # Print triangle

def print_pyramids(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "#" * (2 * i - 1)) # Print pyramid

# Define menu function
def menu():
    print("Choose a pattern to print: ")
    print("1. Stars")
    print("2. Triangles")
    print("3. Pyramids")
    print("4. Exit")

# Define main function to get user input and call the appropriate function
def main():
    while True:
        menu()
        choice = input("Enter your choice: ").strip() # Using string methods to validate input
        if choice in ['1', '2', '3']:
            while True:
                try:
                    rows = int(input("Enter number of rows: ")) # Get number of rows from user
                    if rows <= 0:
                        print("Please enter a positive integer for rows.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue

        if choice == '1':
            print_stars(rows)
        elif choice == '2':
            print_triangles(rows)
        elif choice == '3':
            print_pyramids(rows)
        elif choice == '4':
            print("Exiting the pattern printer. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
# Run the pattern printer program
if __name__ == "__main__":
    main()