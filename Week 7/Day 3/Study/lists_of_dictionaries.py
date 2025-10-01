"""
In Python, a list of dictionaries is a common and effective way to represent a collection of records,
where each record is a dictionary containing key-value pairs. This structure is particularly useful 
when dealing with tabular data or collections of objects with distinct attributes.
"""
# Creating a List of Dictionaries:
"""
You can create a list of dictionaries by enclosing individual dictionary objects within square 
brackets [] and separating them with commas.
"""
# Example: List of student records
students = [
    {'name': 'Alice', 'age': 20, 'major': 'Computer Science'},
    {'name': 'Bob', 'age': 22, 'major': 'Electrical Engineering'},
    {'name': 'Charlie', 'age': 21, 'major': 'Mathematics'}
]
# Accessing Elements in a List of Dictionaries:
## Accessing individual dictionaries:
"""
You can access individual dictionaries within the list using their index, just like with any 
other list.
"""
first_student = students[0]  # {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}
print(f"First student: {first_student}")

## Accessing values within a dictionary:
"""
Once you have a dictionary, you can access its values using their corresponding keys.
"""
alice_name = students[0]['name']  # 'Alice'
bob_age = students[1]['age']      # 22
print(f"Alice's name: {alice_name}")
print(f"Bob's age: {bob_age}")

# Iterating Through the List:
"""
You can use a for loop to iterate through the list and process each dictionary (record) individually.
"""
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}")
    print(f"Major: {student['major']}")

# Modifying Elements:
"""
You can modify the values within a dictionary in the list by accessing the dictionary and then 
updating the desired key.
"""
students[0]['age'] = 21  # Update Alice's age
students[2]['gpa'] = 3.8  # Add a new key-value pair to Charlie's record
print(f"Updated Alice's age: {students[0]['age']}")
print(f"Charlie's GPA: {students[2]['gpa']}")

# Adding and Removing Records:
## Adding a new record:
"""
Use append() to add a new dictionary to the end of the list.
"""
students.append({'name': 'Diana', 'age': 19, 'major': 'Physics'})
print(f"Added new student: {students[-1]}")

## Removing a record:
"""
Use pop() with an index or remove() with the dictionary object to remove a record.
"""
students.pop(1)  # Removes Bob's record
print(f"After removing Bob, students list: {students}")
students.remove({'name': 'Charlie', 'age': 21, 'major': 'Mathematics', 'gpa': 3.8})  # Removes Charlie's record
print(f"After removing Charlie, students list: {students}")