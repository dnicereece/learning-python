# School system with student and course classes

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name}, Age: {self.age}"

class Course:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor

    def info(self):
        return f"Course: {self.title}, Instructor: {self.instructor}"
# Creating multiple Student objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 19)

# Creating multiple Course objects
course1 = Course("Mathematics", "Dr. Smith")
course2 = Course("History", "Prof. Johnson")
course3 = Course("Biology", "Dr. Lee")

# Displaying student information
print(student1.info())
print(student2.info())
print(student3.info())

# Displaying course information
print(course1.info())
print(course2.info())
print(course3.info())

# Assigning students to courses
student_courses = {
    student1.name: [course1.title, course2.title],
    student2.name: [course2.title, course3.title],
    student3.name: [course1.title, course3.title],
}   

# Displaying student course assignments
for student, courses in student_courses.items():
    print(f"{student} is enrolled in: {', '.join(courses)}")