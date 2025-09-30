"""
AI Overview
Iterating through a dictionary in Python can be performed in several ways, depending on whether the 
keys, values, or both are required.
"""

# Iterating through keys
# Directly iterating through the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key) # Outputs: a, b, c


# Using the .keys() method
for key in my_dict.keys():
    print(key) # Outputs: a, b, c
    print(my_dict.keys()) # Outputs: dict_keys(['a', 'b', 'c'])

# Iterating through values
# Using the .values() method
for value in my_dict.values():
    print(value) # Outputs: 1, 2, 3
    print(my_dict.values()) # Outputs: dict_values([1, 2, 3])

# Iterating through key-value pairs
# Using the .items() method
"""
This is the most common and reccommended way to iterate through both keys and values.
"""
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}") 
    # Outputs: Key: a, Value: 1
    #          Key: b, Value: 2
    #          Key: c, Value: 3
    print(my_dict.items()) # Outputs: dict_items([('a', 1), ('b', 2), ('c', 3)])
    """
    The items() method returns a view object that yields key-value pairs as tuples, which are then 
    unpacked directly into key and value variables in the 'for' loop.
    """

# Accessing values by Key during Key iteration
"""
While iterating through keys, values can be accessed using my_dict[key]:
"""
for key in my_dict:
    value = my_dict[key]
    print(f"Key: {key}, Value: {value}")
    # Outputs: Key: a, Value: 1
    #          Key: b, Value: 2
    #          Key: c, Value: 3
    print(my_dict[key]) # Outputs: 1, 2, 3
    """
    However, using my_dict.items() is generally preferred for readability and efficiency when both 
    keys and values are needed.
    """