# Create a program that determines the winner of a game of Scrabble

# Import necessary libraries
import string

# Assign point values to each letter
POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Function to compute the score of a word
def compute_score(word):
    """Compute the score for a given word."""
    score = 0
    for char in word:
        if char.isalpha():  # Check if the character is a letter
            index = ord(char.lower()) - ord('a')  # Get the index (0-25)
            score += POINTS[index]  # Add the corresponding points
    return score

# Prompt the user for two words
word1 = input("Player 1: ")
word2 = input("Player 2: ")

# Compute the score for each word
score1 = compute_score(word1)
score2 = compute_score(word2)

# Print the winner (or a tie)
if score1 > score2:
    print("Player 1 wins!")
elif score2 > score1:
    print("Player 2 wins!")
else:
    print("It's a tie!")