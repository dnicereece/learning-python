"""
In Python, a 2D data structure can be effectively represented using nested lists, also known as a list of 
lists. This structure allows for the organization of data in a tabular or grid-like format, with rows and 
columns.
"""

## Creating a 2D nested list
"""
A 2D nested list is created by enclosing multiple lists within an outer list. Each inner list represents 
a row, and the elements within that inner list represent the columns.
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a 2D nested list
"""
Elements in a 2D nested list are accessed using two indices: the first index specifies the row, and the 
second index specifies the column within that row. Both indices are zero-based.
"""
element = matrix[1][2]  # Accesses the element at row 1, column 2 (value 6)
print(element)

# Iterating through a 2D nested list
"""
Nested loops are commonly used to iterate through all elements of a 2D nested list. The outer loop 
iterates through the rows, and the inner loop iterates through the elements within each row.
"""
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Newline after each row

# Modifying elements in a 2D nested list
"""
Individual elements can be modified by assigning a new value to a specific row and column index.
"""
matrix[0][0] = 10  # Changes the element at row 0, column 0 to 10
print(matrix)

# Appending to a 2D nested list
"""
New rows (inner lists) can be added to the end of the 2D nested list using the append() method. Elements 
can also be appended to existing inner lists.
"""
# Appending a new row
matrix.append([10, 11, 12])
print(matrix)

# Appending an element to an existing row
matrix[0].append(4)
print(matrix)