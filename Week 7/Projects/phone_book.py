# Practice using dictionaries for data lookup and modification.

# Create dictionary
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-9876",
    "Charlie": "555-2468"
}

# Access a phone number (using key)
print("Alice's number:", phone_book["Alice"])  # Output: 555-1234

# Access a phone number (using get method)
print("Bob's number:", phone_book.get("Bob"))  # Output: 555-9876
print("David's number:", phone_book.get("David", "Not Found"))  # Output: Not Found
print("David's number:", phone_book.get("David"))  # Output: None

# Add new contact
phone_book["David"] = "555-1357"
print("Added David:", phone_book)

# Modify existing contact's number
phone_book["Alice"] = "555-4321"
print("Updated Alice's number:", phone_book)

# Remove a contact
removed = phone_book.pop("Charlie")
print("Removed Charlie (number:", removed, "):", phone_book)

# Iterate through dictionary
print("\nAll contacts in phone book:")
for name, number in phone_book.items():
    print(f"{name}: {number}")