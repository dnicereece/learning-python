# Python has a set of built-in methods that you can use on dictionaries.
my_dict = {'a': 1, 'b': 2, 'c': 3}

# clear() - Removes all the elements from the dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# copy() - Returns a shallow copy of the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {'a': 1, 'b': 2, 'c': 3}

# fromkeys() - Creates a new dictionary with keys from an iterable and values set to a specified value
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# get() - Returns the value for a specified key if the key is in the dictionary
value = my_dict.get('a')
print(value)  # Output: 1

# items() - Returns a view object that displays a list of a dictionary's key-value tuple pairs
items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# keys() - Returns a view object that displays a list of all the keys in the dictionary
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b', 'c'])

# pop() - Removes the item with the specified key and returns its value
value = my_dict.pop('b')
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}

# popitem() - Removes and returns the last inserted key-value pair as a tuple
item = my_dict.popitem()
print(item)  # Output: ('c', 3)
print(my_dict)  # Output: {'a': 1}

# setdefault() - Returns the value of a specified key. If the key does not exist, insert the key with a specified value
value = my_dict.setdefault('b', 2)
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'b': 2}

# update() - Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs
my_dict.update({'c': 3, 'd': 4})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# values() - Returns a view object that displays a list of all the values in the dictionary
values = my_dict.values()
print(values)  # Output: dict_values([1, 2, 3, 4])