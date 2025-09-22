# Practice with lists, indexing, and list methods

# Create a list

fruits = ["apple", "banana", "cherry"]
# Basic indexing
print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: cherry

# List methods
fruits.append("date") # Add an item to the end
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
fruits.remove("banana") # Remove an item
print(fruits)  # Output: ['apple', 'cherry', 'date']
fruits.insert(2, "blueberry") # Insert an item at index 2
print(fruits)  # Output: ['apple', 'cherry', 'blueberry', 'date']
last = fruits.pop() # Remove and return item at index -1 (last item) unless index is specified
print(last)    # Output: date
print(fruits)  # Output: ['apple', 'cherry', 'blueberry']

