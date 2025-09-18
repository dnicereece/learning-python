# Create input validation utilities using functions with proper docstrings
# Import necessary modules
import re
# Validate if input is an integer
def is_integer(value: str) -> bool:
    """
    Validates if the input string can be converted to an integer.

    Arguments:
        value (str): The input string to validate.

    Returns:
        bool: True if the input can be converted to an integer, False otherwise.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False

# Validate if input is a float
def is_float(value: str) -> bool:
    """
    Validates if the input string can be converted to a float.

    Arguments:
        value (str): The input string to validate.

    Returns:
        bool: True if the input can be converted to a float, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

# Validate if input is a positive number
def is_positive_number(value: str) -> bool:
    """
    Validates if the input string is a positive number.

    Arguments:
        value (str): The input string to validate.

    Returns:
        bool: True if the input is a positive number, False otherwise.
    """
    return is_float(value) and float(value) > 0

# Validate if input is a non-empty string
def is_non_empty_string(value: str) -> bool:
    """
    Validates if the input string is a non-empty string.

    Arguments:
        value (str): The input string to validate.

    Returns:
        bool: True if the input is a non-empty string, False otherwise.
    """
    return bool(value)

# Validate if input is an email address
def is_email(value: str) -> bool:
    """
    Validates if the input string is a valid email address.

    Arguments:
        value (str): The input string to validate.

    Returns:
        bool: True if the input is a valid email address, False otherwise.
    """
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, value) is not None
# Validate if input is a phone number
def is_phone_number(value: str) -> bool:
    """
    Validates if the input string is a valid phone number.

    Arguments:
        value (str): The input string to validate.
    
    Returns:
        bool: True if the input is a valid phone number, False otherwise.
    """
    phone_pattern = r'^\+?1?\d{9,15}$'  # Simplified pattern for international phone numbers
    return re.match(phone_pattern, value) is not None

if __name__ == "__main__":
    pass

# Example usage
print(is_integer("123"))          # True
print(is_float("123.45"))         # True
print(is_positive_number("-123"))  # False
print(is_non_empty_string(""))     # False
print(is_email("test@example.com"))  # True
print(is_phone_number("+1234567890"))  # True