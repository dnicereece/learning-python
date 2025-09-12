# Create a program to validate credit card numbers using Luhn's algorithm.
# Import re module to search patterns
import re 


# Function to validate credit card number using Luhn's algorithm
def validate_card(number):
    # Convert number to string and remove non-digit characters
    number = re.sub(r"\D", "", str(number))
    
    # Check if the number is empty or has less than 13 digits
    if len(number) < 13:
        return False
    
    # Reverse the credit card number and convert to a list of integers
    digits = [int(d) for d in number][::-1]
    
    # Double every second digit
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        # If doubling results in a number greater than 9, subtract 9
        if digits[i] > 9:
            digits[i] -= 9
    
    # Sum all the digits
    total = sum(digits)
    
    # If the total modulo 10 is 0, the card is valid
    return total % 10 == 0

# Check if it is AMEX, MASTERCARD, or VISA
def card_type(number):
    number = str(number)
    if re.match(r"^3[47]\d{13}$", number):
        return "AMEX"
    elif re.match(r"^5[1-5]\d{14}$", number):
        return "MASTERCARD"
    elif re.match(r"^4(\d{12}|\d{15})$", number):
        return "VISA"
    else:
        return "INVALID"

# Loop to allow multiple checks
while True:
    # Get credit card number from user
    number = input("Number (or 'q' to quit): ")
    if number.lower() == 'q':
        break
    # Validate the card and print the result
    if validate_card(number):
        print(card_type(number))
    else:
        print("INVALID")