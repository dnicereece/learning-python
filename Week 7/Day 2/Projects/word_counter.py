# Count word frequency in a text using dictionary methods and iteration

def word_counter(text):
    # Remove punctuation and convert to lowercase
    text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    
    words = text.split()  # Split text into words
    word_freq = {}  # Initialize an empty dictionary to hold word frequencies

    for word in words:  # Iterate through each word in the list
        if word in word_freq:  # If the word is already in the dictionary
            word_freq[word] += 1  # Increment its count
        else:
            word_freq[word] = 1  # Otherwise, add it to the dictionary with a count of 1

    return word_freq  # Return the dictionary containing word frequencies

# Example usage
text = "Hello world! Hello everyone. Welcome to the world of Python. Python is great, and the world is beautiful."
frequency = word_counter(text)
print(frequency)
# Outputs: {'hello': 2, 'world': 3, 'everyone': 1, 'welcome': 1, 'to': 1, 'the': 2, 'of': 1, 'python': 2, 'is': 2, 'great': 1, 'and': 1, 'beautiful': 1}
# You can also sort the dictionary by word frequency
sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
print(sorted_frequency)
# Outputs: {'world': 3, 'hello': 2, 'python': 2, 'is': 2, 'the': 2, 'everyone': 1, 'welcome': 1, 'to': 1, 'of': 1, 'great': 1, 'and': 1, 'beautiful': 1}