# Get user input and validate age
print("Welcome! This program will validate your age.")  

# Check if input is all digits
while True:
    age_input = input("Please enter your age: ")
    if not age_input.isdigit():
        print("Invalid input. Please enter a valid age in numbers.")
    else:
        age = int(age_input)
        # Check if age is within a reasonable range
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif age < 18:
            print("You are a minor.")
            break
        elif age <= 65:
            print("You are an adult.")
            break
        elif age <= 120:
            print("That doesn't seem like a reasonable age.")
            break
        else:
            print("Please enter a realistic age.")