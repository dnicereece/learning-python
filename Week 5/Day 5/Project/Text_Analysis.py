# Create a text analysis toolkit using functions with proper docstrings
# import necessary libraries
import re
# Word Count
def word_count(text):
    """
    Counts the number of words in the given text.

    Arguments:
        text (str): The text to analyze.        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())
    # Character Count
def character_count(text):
    """
    Counts the number of characters in the given text.

    Arguments:
        text (str): The text to analyze.

    Returns:
        int: The number of characters in the text.
    """
    return len(text)
# Uppercase Conversion
def uppercase_conversion(text):
    """
    Converts the given text to uppercase.

    Arguments:
        text (str): The text to convert.

    Returns:
        str: The text in uppercase.
    """
    return text.upper()
# Lowercase Conversion
def lowercase_conversion(text):
    """
    Converts the given text to lowercase.

    Arguments:
        text (str): The text to convert.

    Returns:
        str: The text in lowercase.
    """
    return text.lower()
# Title Case Conversion
def title_case_conversion(text):
    """
    Converts the given text to title case.

    Arguments:
        text (str): The text to convert.

    Returns:
        str: The text in title case.
    """
    return " ".join(word.capitalize() for word in text.strip().split())
# Sentence Count
def sentence_count(text):
    """
    Counts the number of sentences in the given text.

    Arguments:
        text (str): The text to analyze.

    Returns:
        int: The number of sentences in the text.
    """
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])
# Average reading level (Flesch-Kincaid)
def average_reading_level(text):
    """
    Calculates the Flesch-Kincaid reading level of the given text.

    Arguments:
        text (str): The text to analyze.

    Returns:
        float: The Flesch-Kincaid reading level of the text.
    """
    words = word_count(text)
    sentences = sentence_count(text)
    syllables = sum([len(re.findall(r'[aeiouy]+', word.lower())) for word in text.split()])
    if sentences == 0 or words == 0:
        return 0.0
    flesch_kincaid = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    return round(flesch_kincaid, 2)
# Most Common Word
def most_common_word(text, n=1):
    """
    Finds the most common word in the given text.

    Arguments:
        text (str): The text to analyze.
        n (int): The number of most common words to return.

    Returns:
        str: The most common word in the text.
    """
    words = re.findall(r'\w+', text.lower())
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        if not word_counts:
            return ""
        return max(word_counts, key=word_counts.get)
# Define the menu function
def menu():
    print("\nText Analysis Menu:")
    print("1. Word Count")
    print("2. Character Count")
    print("3. Uppercase Conversion")
    print("4. Lowercase Conversion")
    print("5. Title Case Conversion")
    print("6. Sentence Count")
    print("7. Average Reading Level (Flesch-Kincaid)")
    print("8. Most Common Word")
    print("9. Enter new text to Analyze")
    print("10. Exit")
# Define the main function to get user input and call the appropriate function
def main():
    print("Welcome to the Text Analysis Toolkit!")
    text = "" # Initialize an empty string to hold the text input
    while True:
        menu()
        if not text:
            text = input("Enter the text to analyze: ") # Get text input from the user
        choice = input("Please select an option (1-10): ")
        if choice == '1':
            print(f"Word Count: {word_count(text)}")
        elif choice == '2':
            print(f"Character Count: {character_count(text)}")
        elif choice == '3':
            print(f"Uppercase Conversion: {uppercase_conversion(text)}")
        elif choice == '4':
            print(f"Lowercase Conversion: {lowercase_conversion(text)}")
        elif choice == '5':
            print(f"Title Case Conversion: {title_case_conversion(text)}")
        elif choice == '6':
            print(f"Sentence Count: {sentence_count(text)}")
        elif choice == '7':
            print(f"Average Reading Level (Flesch-Kincaid): {average_reading_level(text)}")
        elif choice == '8':
            common_word = most_common_word(text)
            if common_word:
                print(f"Most Common Word: {common_word}")
            else:
                print("No words found in the text.")
        elif choice == '9':
            text = input("Enter the new text to analyze: ")
        elif choice == '10':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
# Run the text analysis program
if __name__ == "__main__":
    main()