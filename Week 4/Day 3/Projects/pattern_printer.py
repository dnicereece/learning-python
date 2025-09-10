# Print stars, triangles, and pyramids using nested loops
# Create a menu to choose between patterns or exit
while True:
    print("Choose a pattern to print: ")
    print("1. Stars")
    print("2. Triangles")
    print("3. Pyramids")
    print("4. Exit")

    choice = input("Enter your choice: ").strip() # Using string methods to validate input

    # Nested loops to print patterns
    if choice == '1':
        rows = int(input("Enter number of rows for stars: "))
        for i in range(rows):
            print("*" * (i + 1)) # Print stars
    elif choice == '2':
        rows = int(input("Enter number of rows for triangles: "))
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * (2 * i - 1)) # Print triangle
    elif choice == '3':
        rows = int(input("Enter number of rows for pyramids: "))
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "#" * (2 * i - 1)) # Print pyramid
    elif choice == '4':
        print("Exiting the pattern printer. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

