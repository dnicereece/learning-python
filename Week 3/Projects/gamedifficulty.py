# Ask the user to select a game difficulty from a menu
print("Select a game difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

# Get user input
while True: 
    choice = input("Enter the number corresponding to your choice (1-3): ").strip()
    if choice in ['1', '2', '3']:
        break
    else:
        print("Invalid input. Please enter 1, 2, or 3.")

# Map the choice to a difficulty level
if choice == '1':
    difficulty = "Easy"
elif choice == '2':
    difficulty = "Medium"
else:
    difficulty = "Hard"

print(f"You have selected {difficulty} difficulty.")