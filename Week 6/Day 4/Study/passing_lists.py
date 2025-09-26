"""
Passing lists to functions in Python involves providing a list as an argument to a function, allowing the 
function to access and potentially modify the list's contents.
"""

## How to pass a list to a function
# Define a function that takes a list as a parameter
def process_list(my_list):
# Function logic to work with my_list
    for item in my_list:
        print(item)

# Call the function, passing a list as an argument
my_data = [10, 20, 30, 40]
process_list(my_data)

## Important considerations
"""
Pass by Reference: In Python, when you pass a list to a function, you are passing a reference to the 
original list object in memory. This means that any modifications made to the list inside the function 
will directly affect the original list outside the function.
"""
def add_element(a_list):
    a_list.append(5)

original_list = [1, 2, 3]
add_element(original_list)
print(original_list)  # Output: [1, 2, 3, 5]

"""
Creating a Copy (if modification is not desired): If you want to prevent the original list from being 
modified, you should create a copy of the list before passing it to the function.
"""
def modify_copy(a_list):
    copied_list = a_list[:]  # Create a shallow copy
    copied_list.append(5)
    print(copied_list)

original_list = [1, 2, 3]
modify_copy(original_list)  # original_list remains unchanged
print(original_list)  # Output: [1, 2, 3]

"""
Note: For lists containing mutable objects (like lists of lists), a shallow copy might not be sufficient 
to prevent modifications to nested elements. In such cases, a deep copy (using copy.deepcopy()) is 
required.

Using *args for Unpacking: You can use the * operator to unpack a list into separate arguments when 
calling a function, provided the function is designed to accept multiple individual arguments.
"""
def sum_numbers(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = sum_numbers(*numbers)
print(result)  # Output: 6
