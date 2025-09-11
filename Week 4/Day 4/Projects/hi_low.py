# Create a number guessing game with hi/low hints
# Import random module for random number generation
import random
# Starting dialogue 
print("Welcome to Hi-Low! Guess a number with hints after each guess")
print("Type 'q' anytime to quit.\n")

# Wrap code in a while loop to keep game running until user quits
while True:

# Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    guess = None
    
    # Loop until user guesses correctly or quits
    while guess != random_number:
        # Ask the user to input their guess
        guess_input = input("Guess a number between 1 and 100 (or 'q' to quit): ")

        # Exit loop if user quits
        if guess_input.lower() == 'q':
            print("Thanks for playing!")
            exit()

        # Convert guess to integer with validation check
        if guess_input.isdigit():
            guess = int(guess_input)
        else:
            print("Please enter a valid number.")
            continue

        # Give hints
        if guess > random_number:
            print("Too high!")
        elif guess < random_number:
            print("Too low!")
        else:
            print("Correct! You guessed the number. Let's play again.\n")
            break     