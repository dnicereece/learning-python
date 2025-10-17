# Student class for managing grades and GPA calculations
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        average = sum(self.grades) / len(self.grades)
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def get_grades(self):
        return self.grades
    
# Example usage:
student = Student("John Doe")
student.add_grade(85)
student.add_grade(92)
student.add_grade(76)
print("Grades:", student.get_grades())          # Output: Grades: [85, 92, 76]
print("GPA:", student.calculate_gpa())          # Output: GPA: 3.0

student2 = Student("Jane Smith")
student2.add_grade(58)
student2.add_grade(64)
print("Grades:", student2.get_grades())         # Output: Grades: [58, 64]
print("GPA:", student2.calculate_gpa())         # Output: GPA: 0.5