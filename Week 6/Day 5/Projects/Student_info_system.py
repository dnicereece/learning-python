# Student Info System - List Processing Focus

# Student data: [name, grade, attendance, [assignment grades]]
students = [
    ["Alice", 92, 18, [92]],
    ["Bob", 85, 16, [85]],
    ["Charlie", 78, 20, [78]],
    ["Diana", 88, 19, [88]],
    ["Eve", 95, 20, [95]],
    ["Frank", 67, 15, [67]],
]

def calculate_grade(student):
    """
    Calculate the grade for a student based on their assignment scores.

    Args:
        student (list): A list containing student information [name, grade, attendance, [assignment grades]]

    Returns:
        None: Updates the student's grade in place based on the average of assignment grades.
    """
    assignments = student[3]
    if assignments:
        student[1] = round(sum(assignments) / len(assignments), 2)
    else:
        student[1] = 0

def display_menu():
    print("\nStudent Data Processing Menu")
    print("1. Show all student names")
    print("2. Show top 3 students by grade")
    print("3. Show students with grade >= 90")
    print("4. Show all assignment grades")
    print("5. Show average grade of all students")
    print("6. Show attendance list")
    print("7. Show student index and name")
    print("8. Check if all students have perfect attendance (all/any)")
    print("9. Sort students by attendance")
    print("10. Show all student data")
    print("11. Add a new student")
    print("12. Add assignment grades to student")
    print("13. Exit")

def show_all_names():
    """
    Show the names of all students.

    Returns:
        Prints the list of student names.
    """
    names = [student[0] for student in students]
    print("All names:", names)

def show_top_3_by_grade():
    """
    Show the top 3 students by grade.

    Returns:
        Prints the top 3 students with their grades.
    """
    top_students = sorted(students, key=lambda s: s[1], reverse=True)[:3]
    print("Top 3 students by grade:")
    for s in top_students:
        print(s)

def show_high_achievers():
    """
    Show students with grade >= 90.

    Returns:
        Prints the students who are high achievers.
    """
    high_achievers = [s for s in students if s[1] >= 90]
    print("Students with grade >= 90:")
    for s in high_achievers:
        print(s)

def show_all_assignment_grades():
    """
    Show all assignment grades.

    Returns:
        Prints a list of all assignment grades from all students.
    """
    all_assignments = [grade for student in students for grade in student[3]]
    print("All assignment grades:", all_assignments)

def show_average_grade():
    """
    Show the average grade of all students.
    
    Returns:
        Prints the average grade rounded to 2 decimal places.
    """
    average_grade = sum(s[1] for s in students) / len(students)
    print("Average grade:", round(average_grade, 2))

def show_attendance_list():
    """
    Show the attendance list of all students.

    Returns:
        Prints the attendance list.
    """
    attendance_list = [s[2] for s in students]
    print("Attendance list:", attendance_list)

def show_student_indices():
    """
    Show the index and name of each student.

    Returns:
        Prints the index and name of each student.
    """
    for idx, student in enumerate(students):
        print(f"Student #{idx+1}: {student[0]}")

def check_perfect_attendance():
    """
    Check if all students have perfect attendance.

    Returns:
        Prints whether all students have perfect attendance (20 days).
    """
    all_perfect = all(s[2] == 20 for s in students)
    print("All students have perfect attendance?", all_perfect)

def sort_by_attendance():
    """
    Sort students by attendance.

    Returns:
        Prints the list of students sorted by attendance in descending order.
    """
    students.sort(key=lambda s: s[2], reverse=True)
    print("Students sorted by attendance (highest first):")
    for s in students:
        print(s)

def show_all_data():
    """
    Show all student data.

    Returns:
        Prints all student data including name, grade, attendance, and assignment grades.
    """
    print("All student data [Name, Grade, Attendance, [Assignment Grades]]:")
    for s in students:
        print(s)

def add_student():
    """
    Add a new student.

    Returns:
        Prompts for student details and adds the new student to the list.
    """
    name = input("Enter student name: ")
    try:
        attendance = int(input("Enter attendance (0-20): "))
        assignments_input = input("Enter assignment grades separated by commas (e.g. 80,90,100): ")
        assignments = [int(x.strip()) for x in assignments_input.split(",") if x.strip().isdigit()]
        new_student = [name, 0, attendance, assignments]
        calculate_grade(new_student)
        students.append(new_student)
        print(f"Added student: {name}")
    except ValueError:
        print("Invalid input. Student not added.")

def add_assignment():
    """
    Add assignment grades for a student.

    Returns:
        Prompts for student index and assignment grades, then updates the student's record.
    """
    show_student_indices()
    try:
        idx = int(input("Enter student index to add assignment grades: ")) - 1
        if 0 <= idx < len(students):
            assignments_input = input("Enter assignment grades separated by commas (e.g. 80,90,100): ")
            new_assignments = [int(x.strip()) for x in assignments_input.split(",") if x.strip().isdigit()]
            students[idx][3].extend(new_assignments)
            calculate_grade(students[idx])
            print(f"Updated assignments for {students[idx][0]}. New grade: {students[idx][1]}")
        else:
            print("Invalid student index.")
    except ValueError:
        print("Invalid input. No assignments added.")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == "1":
            show_all_names()
        elif choice == "2":
            show_top_3_by_grade()
        elif choice == "3":
            show_high_achievers()
        elif choice == "4":
            show_all_assignment_grades()
        elif choice == "5":
            show_average_grade()
        elif choice == "6":
            show_attendance_list()
        elif choice == "7":
            show_student_indices()
        elif choice == "8":
            check_perfect_attendance()
        elif choice == "9":
            sort_by_attendance()
        elif choice == "10":
            show_all_data()
        elif choice == "11":
            add_student()
        elif choice == "12":
            add_assignment()
        elif choice == "13":
            print("Exiting.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()