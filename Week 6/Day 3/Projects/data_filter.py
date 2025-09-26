# Create a data filter to extract items from a list meeting specific criteria.

# Define the menu
def display_menu():
    print("\nData Filter Menu:")
    print("1. Filter even numbers")
    print("2. Filter odd numbers")
    print("3. Filter numbers greater than a threshold")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

# Define the filtering functions
def filter_even_numbers(data):
    """
    Filter even numbers from the data list.

    Args:
        data (list): The input list of numbers.

    Returns:
        _type_: _description_
    """
    return [item for item in data if item % 2 == 0]

def filter_odd_numbers(data):
    """
    Filter odd numbers from the data list.

    Args:
        data (list): The input list of numbers.

    Returns:
        list: A list of odd numbers.
    """
    return [item for item in data if item % 2 != 0]

def filter_greater_than_threshold(data, threshold):
    """
    Filter numbers greater than a specified threshold from the data list.

    Args:
        data (list): The input list of numbers.
        threshold (int): The threshold value.

    Returns:
        list: A list of numbers greater than the threshold.
    """
    return [item for item in data if item > threshold]

# Main function to run the data filter
def main():
    while True:
        data = input("Enter a sequence of numbers (comma-separated): ").strip()
        try:
            data_list = [int(item) for item in data.split(",")]
            break
        except ValueError:
            print("Invalid input. Please enter a sequence of numbers.")

    data = data_list
    while True:
        choice = display_menu()
        if choice == '1':
            result = filter_even_numbers(data)
            print("Even numbers:", result)
        elif choice == '2':
            result = filter_odd_numbers(data)
            print("Odd numbers:", result)
        elif choice == '3':
            threshold = int(input("Enter the threshold value: "))
            result = filter_greater_than_threshold(data, threshold)
            print(f"Numbers greater than {threshold}:", result)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()