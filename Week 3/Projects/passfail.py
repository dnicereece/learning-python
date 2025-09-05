# Check if a grade passes or fails
# Define the function
def is_pass_or_fail(grade):
    if grade >= 50:
        return "Pass"
    else:
        return "Fail"
# Get user input and display the result
grade = float(input("Enter the grade: "))
result = is_pass_or_fail(grade)
print(f"The grade {grade} is a {result}.") 
