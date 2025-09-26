# Demonstrating various slicing techniques in Python
""" 
list_name[start:stop:step], where: 
    start: (Optional) The index where the slice begins. If omitted, 
    it defaults to the beginning of the list (index 0).
    
    stop: (Optional) The index where the slice ends. The element at this index 
    is not included in the slice (exclusive). If omitted, it defaults to the end of the list.

    step: (Optional) The increment between indices in the slice. If omitted, 
    it defaults to 1 (meaning consecutive elements are included).

    Negative indices can also be used, where -1 refers to the last element, 
    -2 to the second last, and so on.

    List slicing creates a new list containing the selected elements; 
    it does not modify the original list.
"""
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Basic slicing: from index 2 up to (but not including) index 5
sublist1 = my_list[2:5]  # Result: [2, 3, 4]

# Slicing from the beginning to a specific index
sublist2 = my_list[:4]   # Result: [0, 1, 2, 3]

# Slicing from a specific index to the end
sublist3 = my_list[6:]   # Result: [6, 7, 8, 9]

# Slicing with a step value
sublist4 = my_list[0:10:2] # Result: [0, 2, 4, 6, 8] (every other element)

# Using negative indices (counting from the end)
sublist5 = my_list[-3:]  # Result: [7, 8, 9] (last three elements)
sublist6 = my_list[:-2]  # Result: [0, 1, 2, 3, 4, 5, 6, 7] (all but the last two)

# Creating a shallow copy of the entire list
copy_list = my_list[:]   # Result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Displaying the results
print("Original list:", my_list)
print("Sliced list (2 to 5):", sublist1)
print("Sliced list (beginning to 4):", sublist2)
print("Sliced list (6 to end):", sublist3)
print("Sliced list (0 to 10, step 2):", sublist4)
print("Sliced list (last three elements):", sublist5)
print("Sliced list (all but last two):", sublist6)
print("Shallow copy of the list:", copy_list)