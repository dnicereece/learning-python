# Create functions to analyze text

# Define a function to count the number of words in a text
def count_words(text):
    words = text.split() # Split the text into words based on spaces
    return len(words) # Return the number of words

# Define a function to find the character count in a text
def count_char(text):
    return len(text) # Return the number of characters in the text

# Defince a function to find the most common character in a text
def most_common_char(text):
    text = text.replace(" ", "").lower() # Remove spaces and convert to lowercase for uniformity
    char_count = {} # Initialize an empty dictionary to store character counts
    for char in text:
        if char in char_count:
            char_count[char] += 1 # Increment count if character already in dictionary
        else:
            char_count[char] = 1 # Initialize count if character not in dictionary
    most_common = max(char_count, key=char_count.get) # Find the character with the highest count
    return most_common, char_count[most_common] # Return the most common character and its count

# Call the functions with example inputs and print the results
sample_text = "Hello world! Welcome to text analysis."
print(f"Word Count: {count_words(sample_text)}")
print(f"Character Count: {count_char(sample_text)}")
common_char, count = most_common_char(sample_text) # Get the most common character and its count
print(f"Most Common Character: '{common_char}' appears {count} times")