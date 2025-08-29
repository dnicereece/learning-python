# Prompt user for pyramid height
while True:
    h = input("Height (1-8): ")
    if h.isdigit() and 1 <= int(h) <= 8: # Validate input
        h = int(h)
        break
    print("Enter an integer between 1 and 8.")

# Print a pyramid of that height
for i in range(1, h + 1):
    print(" " * (h - i) + "#" * i) # Print row of bricks