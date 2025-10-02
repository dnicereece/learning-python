# Calculate statistices from a grade dictionary using dictionary methods and iteration

grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}

# Calculate average grade
total = 0 # Initialize total to 0
for grade in grades.values(): # Iterate through all the values in the dictionary
    total += grade # Add each grade to the total
average = total / len(grades) # Calculate average by dividing total by number of entries
print(f"Average Grade: {average}") # Outputs: Average Grade: 86.6

# Find highest and lowest grades
highest = max(grades.values()) # Use max() to find the highest grade
lowest = min(grades.values()) # Use min() to find the lowest grade
print(f"Highest Grade: {highest}") # Outputs: Highest Grade: 92
print(f"Lowest Grade: {lowest}") # Outputs: Lowest Grade: 78

# List students with grades above average
above_average_students = [] # Initialize an empty list to hold names of students above average
for student, grade in grades.items(): # Iterate through key-value pairs in the dictionary
    if grade > average: # Check if the grade is above average
        above_average_students.append(student) # Add student name to the list if condition is met
print(f"Students with above average grades: {above_average_students}") 
    # Outputs: Students with above average grades: ['Bob', 'David', 'Eva']