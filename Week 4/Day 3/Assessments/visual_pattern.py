# Create a visual pattern using nested loops
# Prompt user for row height or exit

while True:
    user_input = input("Enter the number of rows for the pattern up to 9 (or type 'exit' to quit): ").strip()
    
    if user_input.lower() == 'exit':
        print("Exiting the visual pattern generator. Goodbye!")
        break
    
    if not user_input.isdigit() or int(user_input) <= 0 or int(user_input) >= 10:
        print("Invalid input. Please enter a positive integer or 'exit' to quit.")
        continue
    
    rows = int(user_input)

    for i in range(1, rows + 1):
        for s in range(rows - i):
            print("  ", end="")
            
        for j in range(1, i + 1):
            print(f"{j:2}", end="")

        for j in range(i - 1, 0, -1):
            print(f"{j:2}", end="")
        print()  # New line after each row