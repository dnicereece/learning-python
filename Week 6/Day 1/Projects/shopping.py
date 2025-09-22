# Create a shopping list program that allows users to add, remove, and display items. 

# Define the menu
def display_menu():
    """
    Display the shopping list menu options.
    """
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("0. Exit\n")

# Define the function to add an item
def add_item(shopping_list):
    """
    Add an item or multiple items to the shopping list.
    """
    items = input("\nEnter the item(s) to add, separated by commas: ").strip()
    if items:
        shopping_list.extend(item.strip() for item in items.split(","))
        print(f'Added "{items}" to the shopping list.')
# Define the function to remove an item
def remove_item(shopping_list):
    """
    Remove an item from the shopping list.
    """
    name = input("\nEnter the item to remove: ").strip()
    if name in shopping_list:
        shopping_list.remove(name)
        print(f'Removed "{name}" from the shopping list.')
    else:
        print(f'Item "{name}" not found in the shopping list.')
# Define the function to view items
def view_items(shopping_list):
    """
    Display all items in the shopping list.
    """
    if shopping_list:
        print("\nShopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print((f"{index}. {item}"))
    else:
        print("The shopping list is empty.")
# Map menu choices to functions
actions = {
    "1": add_item,
    "2": remove_item,
    "3": view_items,
}
# Define the main function to run the shopping list program
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "0":
            print("Exiting the program.")
            break
        action = actions.get(choice)
        if action:
            action(shopping_list)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()