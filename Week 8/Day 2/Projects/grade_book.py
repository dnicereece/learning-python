# Grade book to read and write student grades to a CSV file

import os
import csv

data = [
    ["Name", "Grade", "Subject"],
    ["Alice", "A", "Math"],
    ["Bob", "B", "Science"],
    ["Charlie", "A", "History"]
]

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "grade_book.csv")

with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Function to read and display the contents of the CSV file
def read_grade_book(file_path):
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# Function to add a new student record to the CSV file
def add_student_record(file_path, student_data):
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(student_data)

# Function to update a student's grade
def update_student_grade(file_path, student_name, new_grade):
    rows = []
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == student_name:
                row[1] = new_grade
            rows.append(row)
    
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

# Example usage
print("Initial Grade Book:")
read_grade_book(csv_path)
add_student_record(csv_path, ["David", "C", "Art"])
print("\nAfter Adding David:")
read_grade_book(csv_path)
update_student_grade(csv_path, "Bob", "A")
print("\nAfter Updating Bob's Grade:")
read_grade_book(csv_path)
