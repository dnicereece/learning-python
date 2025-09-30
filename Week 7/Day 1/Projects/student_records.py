# Practice using dictionaries for data lookup and modification.

# Create dictionary
students = {
    "Alice": 90,
    "Bob": 82,
    "Charlie": 95
}

# Access a value (using key)
print(students["Alice"])  # Output: 90

# Access a value (using get method)
print(students.get("Bob"))  # Output: 82
print(students.get("David", "Not Found"))  # Output: Not Found
print(students.get("David"))  # Output: None

# Add new student
students["David"] = 88
print("Added David:", students)

# Modify existing student's score
students["Alice"] = 92
print("Updated Alice's score:", students)

# Remove a student
removed = students.pop("Charlie")
print("Removed Charlie (grade:", removed, "):", students)

# Iterate through dictionary
print("\nAll student records:")
for name, grade in students.items():
    print(f"{name}: {grade}")
