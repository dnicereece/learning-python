from datetime import date
# Define function and it's perameters
def calculate_age(birth_day, birth_month, birth_year):
    
    # Get today's date
    today = date.today()
    # Create a date object for the birthdate
    birthdate = date(birth_year, birth_month, birth_day)
    # Calculate initial age
    age = today.year - birthdate.year

    # Adjust age if the birth month/day hasn't occurred yet in the current year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

# Example usage:
try:
    day = int(input("Enter your birth day (DD): "))
    month = int(input("Enter your birth month (MM): "))
    year = int(input("Enter your birth year (YYYY): "))

    user_age = calculate_age(day, month, year)
    print(f"You are {user_age} years old.")

except ValueError:
    print("Invalid input. Please enter valid numbers for day, month, and year.")
