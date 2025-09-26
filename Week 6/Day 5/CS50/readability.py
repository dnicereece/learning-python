# Create a program that calculates the approximate grade level needed to comprehend a given text

# Import necessary libraries
import string
import math

# Function to count letters in the text
def count_letters(text):
    """Count the number of letters in the text."""
    return sum(1 for char in text if char.isalpha())
# Function to count words in the text
def count_words(text):
    """Count the number of words in the text."""
    return len(text.split())
# Function to count sentences in the text
def count_sentences(text):
    """Count the number of sentences in the text."""
    return sum(1 for char in text if char in '.!?')
# Function to compute the readability grade level
def compute_readability(text):
    """Compute the readability grade level for the given text."""
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate L and S
    L = (letters / words) * 100 if words > 0 else 0
    S = (sentences / words) * 100 if words > 0 else 0

    # Coleman-Liau index formula
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)
# Prompt the user for input text
text = input("Text: ")
# Compute the readability grade level
grade = compute_readability(text)
# Print the grade level
if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")