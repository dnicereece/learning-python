# Store and manage a student database with multiple attributes using nested dictionaries and lists of dictionaries.

# Student data in a nested dictionary format
students = [
    {'name': 'Alice', 'age': 20, 'major': 'Computer Science'},
    {'name': 'Bob', 'age': 22, 'major': 'Electrical Engineering'},
    {'name': 'Charlie', 'age': 21, 'major': 'Mathematics'},
    {'name': 'Diana', 'age': 19, 'major': 'Physics'}
]

# Function to display all students
def display_students(student_list):
    for student in student_list:
        print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# Function to add a new student
def add_student(student_list, name, age, major):
    student_list.append({'name': name, 'age': age, 'major': major})
    print(f"Added student: {name}")

# Function to remove a student by name
def remove_student(student_list, name):
    for i, student in enumerate(student_list): # Iterate through the list with index
        if student['name'] == name:
            student_list.pop(i) # Remove the student
            print(f"Removed student: {name}")
            return
    print(f"Student {name} not found.")

# Function to update a student's major
def update_major(student_list, name, new_major):
    for student in student_list:
        if student['name'] == name:
            student['major'] = new_major
            print(f"Updated {name}'s major to {new_major}")
            return
    print(f"Student {name} not found.")

# Function to display a single student's details
def display_student(student_list, name):
    for student in student_list:
        if student['name'] == name:
            print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")
            return
    print(f"Student {name} not found.")

# Example usage
display_students(students)
remove_student(students, 'Bob')
print("\nAfter removal:")
display_students(students)
add_student(students, 'Eve', 23, 'Chemistry')
print("\nAfter adding Eve:")
display_students(students)
update_major(students, 'Alice', 'Data Science')
print("\nAfter updating Alice's major:")
display_students(students)
display_student(students, 'Charlie') 