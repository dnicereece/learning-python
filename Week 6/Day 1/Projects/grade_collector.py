# Create a grade collector program that collects and displays student grades.
# Define the menu
def display_menu():
    """
    Display the grade collector menu options.
    """
    print("\nGrade Collector Menu:")
    print("1. Add grade")
    print("2. View grades")
    print("3. View letter grades")
    print("0. Exit\n")
# Define the function to input and store grades
def add_grade(grades):
    """
    Add a grade or multiple grades to the list.
    """
    entries = input("\nEnter the grade(s) to add, separated by commas: ").strip()
    if entries:
        for entry in entries.split(","):
            try:
                grade = float(entry.strip())
                if 0 <= grade <= 100:
                    grades.append(grade)
                    print(f'Added grade: {grade}')
                else:
                    print(f'Grade {grade} is out of range. Please enter a value between 0 and 100.')
            except ValueError:
                print(f'Invalid input "{entry}". Please enter numeric values only.')
# Define the function to display grades
def view_grades(grades):
    """
    Display all grades in the list.
    """
    if grades:
        print("\nGrades:")
        for index, grade in enumerate(grades, start=1):
            print(f"{index}. {grade}")
    else:
        print("No grades available.")
# Define the function to convert grades to letter grades
def convert_to_letter_grade(grade):
    """
    Convert a numeric grade to a letter grade.
    """
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade < 90:
        return "B"
    elif 70 <= grade < 80:
        return "C"
    elif 60 <= grade < 70:
        return "D"
    else:
        return "F"
# Define the function to display letter grades
def view_letter_grades(grades):
    """
    Display all grades with their corresponding letter grades.
    """
    if grades:
        print("\nLetter Grades:")
        for index, grade in enumerate(grades, start=1):
            letter = convert_to_letter_grade(grade)
            print(f"{index}. {grade} - {letter}")
    else:
        print("No grades available.")
# Map menu choices to functions
menu_actions = {
    "1": add_grade,
    "2": view_grades,
    "3": view_letter_grades
}
# Define the main function to run the grade collector program
def main():
    grades = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "0":
            print("Exiting the program.")
            break
        action = menu_actions.get(choice)
        if action:
            action(grades)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()