# Create a multiplication table for numbers 1 through 12 using loops
for i in range(1, 13): # Loop through numbers 1 to 12
    for j in range(1, 13): # Second loop for multiplication
        product = i * j # Calculate product
        print(f"{product:4}", end=' ') 
    print()  # New line after each row

