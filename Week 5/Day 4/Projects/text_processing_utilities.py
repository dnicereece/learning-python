# Create text processing utilities using functions with proper docstrings

# Count words in a string
def count_words(text: str) -> int:
    """
    Counts the number of words in a given string.

    Arguments:
        text (str): The input string.
    
    Returns:
        int: The number of words in the string.
    """
    words = text.split()
    return len(words)
# Count characters in a string
def count_characters(text: str) -> int:
    """
    Counts the number of characters in a given string.

    Arguments:
        text (str): The input string.

    Returns:
        int: The number of characters in the string.
    """
    return len(text)

# Convert string to uppercase
def to_uppercase(text: str) -> str:
    """
    Converts a given string to uppercase.

    Arguments:
        text (str): The input string.

    Returns:
        str: The uppercase version of the string.
    """
    return text.upper()

# Convert string to lowercase
def to_lowercase(text: str) -> str:
    """
    Converts a given string to lowercase.

    Arguments:
        text (str): The input string.

    Returns:
        str: The lowercase version of the string.
    """
    return text.lower()

# Convert string to title case
def to_title_case(text: str) -> str:
    """
    Converts a given string to title case.

    Arguments:
        text (str): The input string.

    Returns:
        str: The title case version of the string.
    """
    return text.title()

# Check if a string is a palindrome
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.

    Arguments:
        text (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Count vowels in a string
def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a given string.

    Arguments:
        text (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    pass

# Example usage
print(count_words("Hello world! This is a test."))  # Output: 6
print(count_characters("Hello world!"))             # Output: 13
print(to_uppercase("Hello"))                         # Output: "HELLO"
print(to_lowercase("HELLO"))                         # Output: "hello"
print(to_title_case("hello world! this is a test."))  # Output: "Hello World! This Is A Test."
print(is_palindrome("A man a plan a canal Panama"))   # Output: True
print(is_palindrome("Hello"))                          # Output: False
print(count_vowels("Hello world!"))                   # Output: 3
