"""
A nested dictionary in Python is a dictionary where the values associated with some keys are 
themselves other dictionaries. This structure allows for organizing complex, hierarchical data 
in a clear and structured manner.
"""

# Creating a Nested Dictionary
"""
You can create a nested dictionary by defining a dictionary whose values are other dictionaries, 
using curly braces {}.
"""
# Example of a nested dictionary
student_data = {
    "John Doe": {
        "age": 20,
        "major": "Computer Science",
        "courses": ["Calculus", "Programming I", "Data Structures"]
    },
    "Jane Smith": {
        "age": 21,
        "major": "Biology",
        "courses": ["Genetics", "Ecology", "Organic Chemistry"]
    }
}

# Accessing Elements in a Nested Dictionary:
"""
To access elements in a nested dictionary, you chain the keys together using square bracket 
notation [].
"""
# Example of accessing an element in the nested dictionary
johns_major = student_data["John Doe"]["major"]
print(f"John's major is: {johns_major}")

# Example of accessing an element further nested (a list within a dictionary)
jane_first_course = student_data["Jane Smith"]["courses"][0]
print(f"Jane's first course is: {jane_first_course}")

# Modifying Elements in a Nested Dictionary:
"""
You can modify elements in a nested dictionary by accessing the specific key and assigning 
a new value.
"""
# Example of modifying an element
student_data["John Doe"]["age"] = 21
print(f"John's new age is: {student_data['John Doe']['age']}")

# Adding a new key-value pair to an inner dictionary
student_data["Jane Smith"]["gpa"] = 3.8
print(f"Jane's GPA: {student_data['Jane Smith']['gpa']}")

# Iterating Through a Nested Dictionary:
"""
You can iterate through a nested dictionary using for loops. You need to check if a value is itself 
a dictionary to iterate through its contents.
"""
for student_name, details in student_data.items():
    print(f"\nStudent: {student_name}")
    for detail_key, detail_value in details.items():
        print(f"  {detail_key}: {detail_value}")