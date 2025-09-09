# Prompt user for their name until they enter vsalid input (non-empty string)
name = input("Enter your name: ")
while not name.strip():
    name = input("Invalid input. Please enter a valid name: ")
print(f"Hello, {name}!")

