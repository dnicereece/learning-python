import json
from datetime import datetime
import os
import re

# Set the path for the JSON data file to always be in the same directory as this script
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Student_Management.json')

def load_data():
    """
    Load student data from the JSON file.
    Returns:
        dict: Dictionary of all student records.
    """
    try:
        with open(DATA_FILE, 'r') as f: # Open the file in read mode
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    """
    Save student data to the JSON file.
    Args:
        data (dict): Dictionary of all student records.
    """
    with open(DATA_FILE, 'w') as f: # Open the file in write mode
        json.dump(data, f, indent=4)

def get_next_student_id(data):
    """
    Generate the next student ID by incrementing the highest existing ID.
    Args:
        data (dict): Dictionary of all student records.
    Returns:
        str: Next student ID.
    """
    if not data:
        return "1001"
    max_id = max(int(sid) for sid in data.keys()) # Convert keys to integers to find the max
    return str(max_id + 1) # Return the next ID as a string

def add_student(name, major):
    """
    Add a new student to the records.
    Args:
        name (str): Student's name.
        major (str): Student's major.
    """
    data = load_data()
    # Prevent duplicate names
    for student in data.values():
        if student["name"] == name:
            print("Student already exists.")
            return
    student_id = get_next_student_id(data) # Generate a new unique ID
    data[student_id] = {
        "name": name,
        "major": major,
        "classes": []
    }
    save_data(data)
    print(f"Student added with ID {student_id}.")

def remove_student(student_id):
    """
    Remove a student from the records by ID.
    Args:
        student_id (str): Student's ID.
    """
    data = load_data()
    if student_id in data:
        del data[student_id]
        save_data(data)
        print("Student removed.")
    else:
        print("Student not found.")

def update_student(student_id, major=None):
    """
    Update a student's major.
    Args:
        student_id (str): Student's ID.
        major (str, optional): New major.
    """
    data = load_data()
    student = data.get(student_id) # Use get to avoid KeyError
    if not student:
        print("Student not found.")
        return
    if major:
        student['major'] = major # Update major if provided
    save_data(data)
    print("Student updated.")

def add_class(student_id, class_name, day, time):
    """
    Add a class to a student's schedule.
    Args:
        student_id (str): Student's ID.
        class_name (str): Name of the class.
        day (str): Day of the class.
        time (str): Time of the class.
    """
    data = load_data()
    student = data.get(student_id)
    if not student:
        print("Student not found.")
        return
    student['classes'].append({    # Add class with initial empty attendance and grades
        "class_name": class_name,
        "day": day,
        "time": time,
        "attendance": [],
        "grades": {
            "overall": 0,
            "assignments": []
        }
    })
    save_data(data)
    print("Class added.")

def add_grade(student_id, class_name, assignment, score):
    """
    Add an assignment grade to a class and recalculate the overall grade.
    Args:
        student_id (str): Student's ID.
        class_name (str): Name of the class.
        assignment (str): Assignment name.
        score (float): Assignment score.
    """
    data = load_data()
    student = data.get(student_id)
    if not student:
        print("Student not found.")
        return
    for cls in student['classes']:  # Find the class to add the grade to
        if cls['class_name'] == class_name:
            cls['grades']['assignments'].append({"name": assignment, "score": score}) # Add the new assignment
            scores = [a['score'] for a in cls['grades']['assignments']] # Extract scores
            cls['grades']['overall'] = round(sum(scores) / len(scores), 2) # Recalculate overall grade
            save_data(data) # Save changes
            print("Grade added and overall recalculated.")
            return
    print("Class not found.")

def add_missed_attendance(student_id, class_name):
    """
    Record a missed attendance date for a class.
    Args:
        student_id (str): Student's ID.
        class_name (str): Name of the class.
    """
    data = load_data()
    student = data.get(student_id)
    if not student:
        print("Student not found.")
        return
    for cls in student['classes']:
        if cls['class_name'] == class_name:
            missed_date = datetime.now().strftime('%Y-%m-%d') # Current date as timestamp
            cls['attendance'].append(missed_date) # Record missed attendance
            save_data(data)
            print(f"Missed attendance recorded for {missed_date}.")
            return
    print("Class not found.")

def view_students():
    """
    Display a list of all students with their IDs, names, and majors.
    """
    data = load_data()
    if not data:
        print("No students found.")
        return
    print("\nStudent List:")
    for sid, info in data.items(): # Display ID, name, and major
        print(f"ID: {sid} | Name: {info['name']} | Major: {info['major']}")

def view_student_details(student_id):
    """
    Display full details for a specific student.
    Args:
        student_id (str): Student's ID.
    """
    data = load_data()
    student = data.get(student_id)
    if not student:
        print("Student not found.")
        return
    print(f"\nDetails for ID {student_id}:")
    print(f"Name: {student['name']}")
    print(f"Major: {student['major']}")
    for cls in student['classes']:
        print(f"Class: {cls['class_name']}, Day: {cls['day']}, Time: {cls['time']}")
        print(f"  Attendance: {cls['attendance']}")
        print(f"  Grades: {cls['grades']}")

def search_students(query):
    """
    Search for students by first or last name (case-insensitive, partial match).
    Args:
        query (str): Search query for name.
    """
    data = load_data()
    results = []
    query = query.strip().lower() # Normalize query
    for sid, info in data.items(): # Check each student's name parts for a match
        name_parts = info['name'].lower().split() # Split name into parts
        if any(query in part for part in name_parts): # Partial match in any part
            results.append((sid, info)) # Collect matching students
    if not results:
        print("No matching students found.")
    else:
        print("\nSearch Results:")
        for sid, info in results: # Display matching students
            print(f"ID: {sid} | Name: {info['name']} | Major: {info['major']}")
            view_student_details(sid)

def report_students_average_grades():
    """
    Print a report of all students with their average grade across all classes.
    """
    data = load_data()
    print("\nStudent Average Grades Report:")
    for sid, info in data.items(): # Calculate average across all classes
        total = 0
        count = 0
        for cls in info['classes']:
            if 'grades' in cls and 'overall' in cls['grades']: # Ensure grades exist
                total += cls['grades']['overall'] # Sum overall grades
                count += 1
        avg = round(total / count, 2) if count else "N/A" # Handle no classes
        print(f"ID: {sid} | Name: {info['name']} | Major: {info['major']} | Average Grade: {avg}")

def update_student_menu(student_id):
    """
    Sub-menu for updating a student's information and classes.
    Args:
        student_id (str): Student's ID.
    """
    while True:
        #Show student details before update options
        view_student_details(student_id)
        print(f"\nUpdate Menu for Student ID {student_id}")
        print("1. Change Major")
        print("2. Add Class")
        print("3. Remove Class")
        print("4. Update Class Schedule")
        print("5. Add Assignment Grade")
        print("6. Add Missed Attendance")
        print("7. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            major = None
            while not major:
                major = validate_nonempty_title(input("New Major: "), "Major") # Validate non-empty and title case
            update_student(student_id, major)
        elif choice == '2':
            class_name = None
            while not class_name:
                class_name = validate_nonempty_title(input("Class Name: "), "Class Name") # Validate non-empty and title case
            day = None
            while not day:
                day = validate_nonempty_title(input("Day: "), "Day") # Validate non-empty and title case
            time = None
            while not time:
                time = validate_time_format(input("Time (HH:MM AM/PM): ")) # Validate time format
            add_class(student_id, class_name, day, time)
        elif choice == '3':
            class_name = None
            while not class_name:
                class_name = validate_nonempty_title(input("Class Name to Remove: "), "Class Name") # Validate non-empty and title case
            remove_class(student_id, class_name)
        elif choice == '4':
            class_name = None
            while not class_name:
                class_name = validate_nonempty_title(input("Class Name to Update: "), "Class Name") # Validate non-empty and title case
            day = None
            while not day:
                day = validate_nonempty_title(input("New Day: "), "Day") # Validate non-empty and title case
            time = None
            while not time:
                time = validate_time_format(input("New Time (HH:MM AM/PM): ")) # Validate time format
            update_class_schedule(student_id, class_name, day, time)
        elif choice == '5':
            class_name = None
            while not class_name:
                class_name = validate_nonempty_title(input("Class Name: "), "Class Name") # Validate non-empty and title case
            assignment = None
            while not assignment:
                assignment = validate_nonempty_title(input("Assignment Name: "), "Assignment Name") # Validate non-empty and title case
            score = None
            while score is None:
                score = validate_grade(input("Score (0-100): ")) # Validate score is a number between 0 and 100
            add_grade(student_id, class_name, assignment, score)
        elif choice == '6':
            class_name = None
            while not class_name:
                class_name = validate_nonempty_title(input("Class Name: "), "Class Name") # Validate non-empty and title case
            add_missed_attendance(student_id, class_name)
        elif choice == '7':
            break
        else:
            print("Invalid option. Please try again.")

def remove_class(student_id, class_name):
    """
    Remove a class from a student's schedule.
    Args:
        student_id (str): Student's ID.
        class_name (str): Name of the class to remove.
    """
    data = load_data()
    student = data.get(student_id)
    if not student:
        print("Student not found.")
        return
    original_len = len(student['classes']) # Store original length to check if removal occurred
    # Remove class by filtering out the matching class_name
    student['classes'] = [cls for cls in student['classes'] if cls['class_name'] != class_name] # List comprehension to filter classes
    if len(student['classes']) < original_len: # Check if a class was actually removed
        save_data(data)
        print("Class removed.")
    else:
        print("Class not found.")

def update_class_schedule(student_id, class_name, new_day, new_time):
    """
    Update the schedule (day and time) for a specific class.
    Args:
        student_id (str): Student's ID.
        class_name (str): Name of the class to update.
        new_day (str): New day for the class.
        new_time (str): New time for the class.
    """
    data = load_data()
    student = data.get(student_id)
    if not student:
        print("Student not found.")
        return
    for cls in student['classes']: # Find the class to update
        if cls['class_name'] == class_name: 
            cls['day'] = new_day
            cls['time'] = new_time
            save_data(data)
            print("Class schedule updated.")
            return
    print("Class not found.")

def validate_nonempty_title(text, field_name):
    """
    Validate that the input is a non-empty string and convert to title case.
    Args:
        text (str): Input text.
        field_name (str): Name of the field for error messages.
    Returns:
        str or None: Title-cased string or None if invalid.
    """
    if not text.strip(): # Check for non-empty input
        print(f"{field_name} cannot be empty.")
        return None
    return text.strip().title() # Convert to title case

def validate_time_format(time_str):
    """
    Validate that the time is in HH:MM AM/PM format.
    Args:
        time_str (str): Input time string.
    Returns:
        str or None: Validated time string or None if invalid.
    """
    pattern = r'^(0[1-9]|1[0-2]):[0-5][0-9] (AM|PM)$' # Regex for HH:MM AM/PM format
    if not re.match(pattern, time_str.strip()): # Validate against the pattern
        print("Time must be in HH:MM AM/PM format (e.g., 10:00 AM).")
        return None
    return time_str.strip() # Return trimmed valid time string

def validate_grade(grade_str):
    """
    Validate that the grade is a number between 0 and 100.
    Args:
        grade_str (str): Input grade string.
    Returns:
        float or None: Validated grade or None if invalid.
    """
    try:
        grade = float(grade_str) # Convert to float
        if 0 <= grade <= 100: # Check if grade is within valid range
            return grade
        else:
            print("Grade must be between 0 and 100.")
            return None
    except ValueError:
        print("Grade must be a number.")
        return None

# Main loop for the menu
def main():
    """
    Main menu loop for the Student Management System.
    """
    while True:
        print("\nStudent Management System")
        print("1. View All Students")
        print("2. View Student Details")
        print("3. Add Student")
        print("4. Remove Student")
        print("5. Update Student")
        print("6. Search Students")
        print("7. Report: Student Average Grades")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_students()
        elif choice == '2':
            student_id = input("Student ID: ")
            view_student_details(student_id)
        elif choice == '3':
            name = None
            while not name:
                name = validate_nonempty_title(input("Student Name: "), "Name")
            major = None
            while not major:
                major = validate_nonempty_title(input("Major: "), "Major")
            add_student(name, major)
        elif choice == '4':
            student_id = input("Student ID: ")
            remove_student(student_id)
        elif choice == '5':
            student_id = input("Student ID: ")
            if load_data().get(student_id):
                update_student_menu(student_id)
            else:
                print("Student not found.")
        elif choice == '6':
            query = input("Enter first or last name to search: ")
            search_students(query)
        elif choice == '7':
            report_students_average_grades()
        elif choice == '8':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()