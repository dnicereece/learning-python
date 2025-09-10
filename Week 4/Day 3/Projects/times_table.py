# Create a multiplication table program using nested loops

# Prompt user for the number to generate the times table, and loop back to ask for a new number until they choose to exit
while True:
    user_input = input("Enter a number to generate its multiplication table (or type 'exit' to quit): ").strip()
    
    if user_input.lower() == 'exit':
        print("Exiting the multiplication table generator. Goodbye!")
        break
    
    if not user_input.isdigit():
        print("Invalid input. Please enter a positive integer or 'exit' to quit.")
        continue
    
    number = int(user_input)
    
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):  # Loop through numbers 1 to 12
        product = number * i  # Calculate product
        print(f"{number} x {i:2} = {product:4}")  # Formatted output
    print()  # New line after the table