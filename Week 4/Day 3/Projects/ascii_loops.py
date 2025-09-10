# Create a program that generate ascii art using loops
# Create a menu to choose between patterns or exit
while True:
    print("Choose a pattern to print: ")
    print("1. Box")
    print("2. X")
    print("3. Checkerboard")
    print("4. Exit")

    choice = input("Enter your choice: ").strip() # Using string methods to validate input

    # Nested loops to print patterns
    if choice == '1':
        rows = int(input("Enter number of rows for box: "))
        cols = int(input("Enter number of columns for box: "))
        for i in range(rows):
            print("*" * cols) # Print box
    elif choice == '2':
        size = int(input("Enter size for X (odd number): "))
        if size % 2 == 0:
            print("Please enter an odd number.")
            continue
        for i in range(size):
            for j in range(size):
                if j == i or j == size - i - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif choice == '3':
        rows = int(input("Enter number of rows for checkerboard: "))
        cols = int(input("Enter number of columns for checkerboard: "))
        for i in range(rows):
            for j in range(cols):
                if (i + j) % 2 == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif choice == '4':
        print("Exiting the ASCII art generator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")