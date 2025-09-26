"""
Functions that modify lists versus functions that return new lists represent two distinct 
approaches to handling mutable data structures like lists in programming.
"""

# Functions that modify lists (in-place modification):
def modify_list_in_place(my_list):
    my_list.append(4)
    my_list.sort()

my_list = [3, 1, 2]
modify_list_in_place(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
"""
-These functions directly alter the content or structure of the list object passed as an argument.

-They typically do not return the modified list explicitly, or they might return None 
(as in Python's list.sort()).

-Modifying functions are often more memory-efficient as they avoid creating new list objects.

-Examples include methods like append(), extend(), insert(), remove(), pop(), and sort() on a list object.
"""

# Functions that return new lists (non-destructive operations):
def create_new_list_with_modifications(original_list):
    new_list = sorted(original_list)
    new_list.append(4)
    return new_list

original_list = [3, 1, 2]
new_modified_list = create_new_list_with_modifications(original_list)
print(original_list)       # Output: [3, 1, 2] (original list unchanged)
print(new_modified_list)  # Output: [1, 2, 3, 4]
"""
-These functions take an existing list as input and create a completely new list containing the desired 
modifications or transformations.

-The original list remains unchanged.

-They explicitly return the newly created list.

-This approach promotes immutability and can be easier to reason about, as the original data is preserved.

-Examples include using list comprehensions or functions that explicitly create and return a new list.
"""

# Choosing between the two approaches:
"""
Performance: In-place modification can be faster and use less memory, especially for large lists, as it 
avoids object creation overhead.

Readability and Predictability: Returning a new list can make code easier to understand and debug, as 
you're guaranteed the original list's state won't be unexpectedly altered. This is particularly important 
in concurrent programming or when passing lists between different parts of a program.

Functional Programming: The approach of returning new lists aligns more closely with functional programming 
paradigms, where immutability is a core principle.

API Design: When designing functions or methods for others to use, clearly indicating whether a function 
modifies in-place or returns a new object is crucial for a predictable and reliable API. Conventionally, 
methods that modify in-place might not return the modified object, while functions that return new objects 
will.
"""
