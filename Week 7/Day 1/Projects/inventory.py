# Practice using dictionaries for data lookup and modification.

# Create dictionary
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20
}

# Access a quantity (using key)
print("Apple quantity:", inventory["apple"])  # Output: 50

# Access a quantity (using get method)
print("Banana quantity:", inventory.get("banana"))  # Output: 30
print("Grapes quantity:", inventory.get("grapes", 0))  # Output: 0
print("Grapes quantity:", inventory.get("grapes"))  # Output: None

# Add new item
inventory["grapes"] = 15
print("Added grapes:", inventory)

# Modify existing item's quantity
inventory["apple"] = 60
print("Updated apple quantity:", inventory)

# Remove an item
removed = inventory.pop("orange")
print("Removed orange (quantity:", removed, "):", inventory)

# Iterate through dictionary
print("\nAll items in inventory:")
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")