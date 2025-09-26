"""
List comprehensions in Python provide a concise way to create new lists based on existing 
iterables. They offer a more compact and often more readable alternative to traditional 
for loops when constructing lists.
"""
# Basic syntax of a list comprehension
# new_list = [expression for item in iterable if condition]
"""
expression: The operation or value to be applied to each item.

item: The variable representing each element in the iterable.

iterable: The source data structure (e.g., a list, tuple, range, string) being iterated over.

condition: (Optional) A filter that determines whether the item should be included in the new 
list.
"""
# Example 1: Creating a list of squares of numbers from 0 to 9
numbers = [1, 2, 3, 4, 5]
squared_numbers = [n**2 for n in numbers]

#List comprehensions can include if statements to filter elements based on a condition:
# Example 2: Creating a list of even numbers from 1 to 6
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [n for n in numbers if n % 2 == 0]

#You can also use an if-else expression within the comprehension to modify elements conditionally:
# Example 3: Doubling even numbers and keeping odd numbers unchanged
numbers = [1, 2, 3, 4, 5]
modified_numbers = [n * 2 if n % 2 == 0 else n for n in numbers]

# For creating lists of lists or flattening nested structures, nested list comprehensions can be used:
# Example 4: Flattening a 2D list (matrix) into a 1D list
matrix = [[1, 2], [3, 4], [5, 6]]
flattened_list = [num for row in matrix for num in row]

"""
Benefits of List Comprehensions:

Conciseness: They allow you to create lists in a single line of code, reducing verbosity.

Readability: For many common list-building tasks, they can be more readable than equivalent for loops.

Efficiency: They are often optimized for performance compared to explicit for loops, especially for 
simple transformations.
"""

# Printing the final results
print("Original numbers:", numbers) # Output: [1, 2, 3, 4, 5]
print("Squared numbers:", squared_numbers) # Output: [1, 4, 9, 16, 25]
print("Even numbers:", even_numbers) # Output: [2, 4, 6]
print("Modified numbers:", modified_numbers) # Output: [1, 4, 3, 8, 5]
print("Flattened list:", flattened_list) # Output: [1, 2, 3, 4, 5, 6]