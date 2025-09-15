# Define functions to validate user input
# Define a function to validate age input
def validate_age(age):
    if not age.isdigit() or int(age) < 0 or int(age) > 120: # Check if age is a number and within a reasonable range
        return "Error! Please enter a valid age between 0 and 120."
    return int(age) # Return age as an integer if valid
# Define a function to validate email input
def validate_email(email):
    if "@" not in email or "." not in email: # Check for basic email structure
        return "Error! Please enter a valid email address."
    return email

# Define a function to validate phone number input
def validate_phone(phone):
    if not phone.isdigit() or len(phone) != 10: # Check if phone number is numeric and 10 digits long
        return "Error! Please enter a valid 10-digit phone number."
    return phone

# Call the functions with example inputs and print the results
print(validate_age("25"))
print(validate_age("-5"))
print(validate_age("130"))
print(validate_email("john.doe@example.com"))
print(validate_email("invalid-email"))
print(validate_phone("1234567890"))
print(validate_phone("12345"))