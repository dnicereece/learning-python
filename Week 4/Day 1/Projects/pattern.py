# Create a number pattern printer printing the Fibonacci sequence
a, b = 0, 1
for _ in range(10): # Print first 10 Fibonacci numbers
    print(a, end=' ') # Print current Fibonacci number
    a, b = b, a + b # Update values for next Fibonacci number
print()  # New line after the pattern
