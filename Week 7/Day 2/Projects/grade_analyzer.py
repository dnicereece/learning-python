# Calculate statistices from a grade dictionary using dictionary methods and iteration

grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}

# Calculate average grade
total = 0
for grade in grades.values():
    total += grade
average = total / len(grades)
print(f"Average Grade: {average}")