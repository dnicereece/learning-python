# Check if a number is even or odd
# Define the function
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Get user input and display the result
num = int(input("Enter a number: "))
result = is_even_or_odd(num)
print(f"The number {num} is {result}.")


