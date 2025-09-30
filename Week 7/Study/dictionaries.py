'''
Python dictionaries are a built-in data type used to store data values in key:value pairs. They 
are a collection that is ordered (from Python 3.7 onwards), changeable, and do not allow duplicate 
keys. Dictionaries are also known as hashmaps, hash tables, or associative arrays in other 
programming languages. 
'''

## Key characteristics of Python dictionaries:

# Key-Value Pairs:
"""
Dictionaries store data as a mapping between unique, immutable keys and their corresponding 
values. Keys can be strings, numbers, or tuples, but not lists or other mutable types. Values 
can be of any data type and can be duplicated.
"""

# Ordered
"""
Dictionaries maintain the order of insertion for their key-value pairs. This means that when you 
iterate over a dictionary, the items will be returned in the order they were added. This feature 
was officially introduced in Python 3.7, although it was already present in CPython 3.6.
"""

# Changeable (Mutable)
"""
Dictionaries are mutable, meaning you can change their content without changing their identity. 
You can add, remove, or modify key-value pairs after the dictionary has been created.
"""

# No Duplicate Keys
"""
Dictionaries do not allow duplicate keys. If you try to create a dictionary with duplicate keys, 
the last value assigned to that key will overwrite any previous value. This ensures that each key 
is unique within the dictionary.
"""

# Efficient Data Retrieval
"""
Dictionaries are optimized for retrieving values based on their keys. The average time complexity for 
looking up a value by its key is O(1), making dictionaries a highly efficient data structure for 
searching and accessing data.
"""

# Creating and Using Dictionaries
"""
Dictionaries are created using curly braces {} with key-value pairs separated by colons :. 
Each key-value pair is separated by a comma.
"""

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Modifying a value
my_dict["age"] = 31

# Adding a new key-value pair
my_dict["occupation"] = "Engineer"

# Removing a key-value pair
del my_dict["city"]

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")


# Accessing Dictionary Items:
"""
Accessing and modifying Python dictionaries involves using keys to interact with their associated 
values.
"""

# Using square brackets to access values
"""
The most common way to access a value is by placing the key within square brackets [] next to 
the dictionary name.
"""
print(my_dict["name"])  # Output: Alice

# Using the get() method
"""
Using the get() method: This method provides a safer way to access values, as it returns None 
(or a specified default value) if the key is not found, instead of raising a KeyError.
"""
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("city", "Unknown")) # Output: Unknown (default value)
print(my_dict.get("city"))  # Output: None (key not found)