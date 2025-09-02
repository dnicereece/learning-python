# Ask user for their age
while True:
    age_input = input("Are you old enough to vote? Please enter your age: ")
    if not age_input.isdigit():
        print("Invalid input. Please enter a valid age in numbers.")
        continue
    age = int(age_input)
        # Check if age is within a reasonable range
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    elif age < 18:
        print("You are a minor and not old enough to vote.")
        break
    elif age >= 18 and age <= 120:
        print("You are an adult and old enough to vote.")
        break
    elif age >= 120:
        print("That doesn't seem like a reasonable age.")
        break
    else:
        print("Please enter a realistic age.")
