# Create a password strength checker
# Import re modue for search patterns
import re

# Define a strong password
def is_strong(password):
    # Check for at least 1 uppercase character
    if not re.search(r"[A-Z]", password):
        print("Password must have at least 1 uppercase letter.")
        return False
    
    # Check for at least 1 lowercase character
    if not re.search(r"[a-z]", password):
        print("Password must have at least 1 lowercase letter")
        return False
    
    # Check for at least 1 digit
    if not re.search(r"\d", password):
        print("Password must have at least 1 digit.")
        return False
    
    # Check for at least 1 special character
    if not re.search(r"[!@#$%^&*(),.?:;]", password):
        print("Password must have at least 1 special character.")
        return False
    
    # Check for at least 8 total charcters
    if len(password) < 8:
        print("Password must have be at least 8 characters long.")
        return False
    
    return True

# Create the loop
while True:
    # Ask the user for their password
    password = input("Check the strength of your password. Please enter your proposed password or press 'q' to quit: ")

    # Exit loop if user quits
    if password.lower() == 'q':
        print("Goodbye.")
        break

    # If password is not strong
    while not is_strong(password):
        password = input("Propose another password or 'q' to quit: ")

    print("You have a strong password!\n")

    # Prompt user to check another password
    again = input("Do you want to check another password?: ")
    if again.lower() not in ['y', 'yes']:
        print("Goodbye.")
        break