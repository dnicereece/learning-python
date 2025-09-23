# Create a practice program to count the frequency of each word in a given text input by the user.
# Get user input for text
print("Enter text. Press Enter on a blank line to finish.")
text = input("> ").strip()
# Split the text into words
words = text.split()
if not words:
    print("No text was entered.")
    exit()
# Ask user for a specific word to count
target_word = input("Enter the word to count its frequency: ").strip().lower()
# Using 'for item in list' to count word frequencies
count = 0 # Initialize count variable
for word in words:
    if word.lower() == target_word:
        count += 1
print(f'The word "{target_word}" appears {count} time(s) in the given text.')
