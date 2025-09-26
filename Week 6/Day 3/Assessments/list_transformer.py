# Create a list transformer that applies operations to all items in a list.

# Menu
def menu():
    print("\nList Transformer Menu")
    print("1. Double each number")
    print("2. Square each number")
    print("3. Add value to each number")
    print("4. Negate each number")
    print("5. Increment each number above a threshold")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    return choice

# Define transformation functions
def double(data):
    """Return a list with each number doubled."""
    return [x * 2 for x in data]

def square(data):
    """Return a list with each number squared."""
    return [x ** 2 for x in data]

def add_value(data, value):
    """Return a list with a value added to each number."""
    return [x + value for x in data]

def negate(data):
    """Return a list with each number negated."""
    return [-x for x in data]

def increment(data, threshold):
    """Return a list with each number incremented if above a threshold."""
    return [x + 1 if x > threshold else x for x in data]

# Main program loop
def main():
    while True:
        data = input("Enter a list of numbers separated by commas: ").strip()
        try:
            original_list = [int(item) for item in data.split(",")]
            break
        except ValueError:
            print("Invalid input. Please enter a list of numbers.")

    while True:
        print(f"\nOriginal List: {original_list}")
        choice = menu()
        if choice == "1":
            result = double(original_list)
            print(f"Result: {result}")
        elif choice == "2":
            result = square(original_list)
            print(f"Result: {result}")
        elif choice == "3":
            try:
                value = int(input("Enter the value to add: "))
                result = add_value(original_list, value)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        elif choice == "4":
            result = negate(original_list)
            print(f"Result: {result}")
        elif choice == "5":
            try:
                threshold = int(input("Enter the threshold: "))
                result = increment(original_list, threshold)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()