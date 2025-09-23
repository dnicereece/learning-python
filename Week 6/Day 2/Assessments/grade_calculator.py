# Create a grade calculator that takes a list of grades and returns the average, highest, and lowest grades from the list.
# Define the menu
def display_menu():
    """
    Display the menu options to the user.
    """
    print("\nGrade Calculator Menu:")
    print("1. Add Grade")
    print("2. View Grades")
    print("3. View Letter Grades")
    print("4. View Average.")
    print("5. View Highest Grade.")
    print("6. View Lowest Grade.")
    print("0. Exit")
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
# Define the function to calculate average grade
def calculate_average(grades):
    """
    Calculate and return the average of the grades.
    """
    if grades:
        average = sum(grades) / len(grades)
        return average
    else:
        return None
# Define the function to find highest grade
def find_highest_grade(grades):
    """
    Find and return the highest grade.
    """
    if grades:
        highest = max(grades)
        return highest
    else:
        return None
# Define the function to find lowest grade
def find_lowest_grade(grades):
    """
    Find and return the lowest grade.
    """
    if grades:
        lowest = min(grades)
        return lowest
    else:
        return None
# Map menu options to functions
menu_actions = {
    "1": add_grade,
    "2": view_grades,
    "3": view_letter_grades,
    "4": calculate_average,
    "5": find_highest_grade,
    "6": find_lowest_grade,
}
# Main program loop
def main():
    grades = []
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == "0":
            print("Exiting the program.")
            break
        action = menu_actions.get(choice)
        if action:
            result = action(grades)
            if result is not None:
                print(f"Result: {result}")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()