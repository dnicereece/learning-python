# Create a substitution cipher program that encrypts messages using a provided key.
import sys
import string

# Define the alphabet
alphabet = string.ascii_lowercase

# Define a function to convert the key to be case-insensitive
def normalize_key(key):
    """
    Normalize the key by stripping whitespace and converting to lowercase.

    Args:
        key (str): The key to normalize.

    Returns:
        str: The normalized key.
    """
    return key.strip().lower()
# Define a function to validate the key
def is_valid_key(key):
    """
    Validate the key for the substitution cipher.

    Args:
        key (str): The key to validate.

    Returns:
        bool: True if the key is valid, False otherwise.
    """
    # Check if the key is 26 characters long
    if len(key) != 26:
        return False
    # Check if the key contains only alphabetic characters
    if not key.isalpha():
        return False
    # Check for duplicate characters
    if len(set(key)) != 26:
        return False
    return True
# Define a function to build a map for both lowercase and uppercase letters
def build_substitution_map(key):
    """
    Build a substitution map from the key.

    Args:
        key (str): The key to use for the substitution map.

    Returns:
        dict: A dictionary mapping each letter of the alphabet to its substitution.
    """
    substitution_map = {}
    for i in range(26):
        substitution_map[alphabet[i]] = key[i].lower()
        substitution_map[alphabet[i].upper()] = key[i].upper()
    return substitution_map
# Define a function to encrypt the plaintext using the substitution map
def encrypt(plaintext, substitution_map):
    """
    Encrypt the plaintext using the substitution map.

    Args:
        plaintext (str): The plaintext to encrypt.
        substitution_map (dict): The substitution map to use for encryption.

    Returns:
        str: The encrypted ciphertext.
    """
    ciphertext = ""
    for char in plaintext:
        if char in substitution_map:
            ciphertext += substitution_map[char]
        else:
            ciphertext += char
    return ciphertext
# Define a function  to expect exactly one command-line argument
def parse_arguments():
    """
    Parse command-line arguments.
    
    Args:
        None

    Returns:
        str: The key provided as a command-line argument.
    """
    if len(sys.argv) != 2:
        print("Usage: python substitution.py KEY")
        sys.exit(1)
    return sys.argv[1]
# Main function to run the program
def main():
    """
    Run the substitution cipher program.
    """
    key = parse_arguments()
    key = normalize_key(key)
    if not is_valid_key(key):
        print("Key must contain 26 unique alphabetic characters.")
        sys.exit(1)
    substitution_map = build_substitution_map(key)
    plaintext = input("plaintext: ")
    ciphertext = encrypt(plaintext, substitution_map)
    print(f"ciphertext: {ciphertext}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()