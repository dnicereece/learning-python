# Create validation functions that return boolean values

# Define a function to check if a number is even
def is_even(number):
    return number % 2 == 0 # Return True if number is even, else False

# Define a function to check if a number is positive
def is_positive(number):
    return number > 0 # Return True if number is positive, else False

# Define a function to check if a string is not empty
def is_not_empty(string):
    return bool(string) # Return True if string is not empty, else False

# Call the functions with example inputs and print the results
print(is_even(4)) # True
print(is_even(7)) # False
print(is_positive(5)) # True
print(is_positive(-1)) # False
print(is_not_empty("Hello")) # True
print(is_not_empty("")) # False