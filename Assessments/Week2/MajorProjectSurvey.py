# Create a survey to assess understanding of major concepts

print("Welcome to the Major Project Survey!")

# Ask for name. Validate non-empty input
while True:
    raw_name = input("What is your name? ").strip()
    if raw_name:  # Ensure name is not empty
        name = raw_name.title()  # Format name as title case
        break
    print("Name cannot be empty. Please enter your name.")

# Ask for age. Validate digits only and reasonable range
while True:
    raw_age = input("How old are you? ").strip()
    if raw_age.isdigit() and 0 < int(raw_age) < 120:  # Age should be a positive integer less than 120
        age = int(raw_age)
        break
    print("Please enter a valid age between 1 and 119.")

# Ask if enjoying the course. Validate yes/no input and allow for y/n shorthand
while True:
    enjoys = input("Are you enjoying the course so far? (yes/no): ").strip().lower()
    if enjoys in ['y', 'yes', 'n', 'no']:
        enjoys = enjoys in ['y', 'yes']  # Convert to boolean
        if enjoys:
            print("Great to hear that you're enjoying the course!")
        else:
            print("We're sorry to hear that. We'll strive to improve.")
        break
    print("Please answer with 'yes' or 'no'.")

# Summarize survey responses
print("\nSurvey Summary:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Enjoying the course: {'Yes' if enjoys else 'No'}")

print("Thank you for completing the survey!")

