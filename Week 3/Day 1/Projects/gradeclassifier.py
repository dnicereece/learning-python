# Ask user for their numerical grade
grade = float(input("Enter your numerical grade: "))
# Determine the letter grade based on the numerical grade  
if grade >= 90:
    print("Your letter grade is A")
elif grade >= 80:
    print("Your letter grade is B")
elif grade >= 70:
    print("Your letter grade is C")
elif grade >= 60:
    print("Your letter grade is D")
else:
    print("Your letter grade is F")
    