# Create program that randomly generates a number between 1 and 100 and asks the user to guess the number.

# Import the random module to generate a random number
import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
# Program should keep asking the user to guess until they get it right
guess = None
while guess != random_number:
    # Ask the user to input their guess
    guess = int(input("Guess a number between 1 and 100: "))
    # If the user's guess is higher than the random number, print "Too high!"
    if guess > random_number:
        print("Too high!")
    # If the user's guess is lower than the random number, print "Too low!"
    elif guess < random_number:
        print("Too low!")
    # If the user guesses the correct number, print "Congratulations! You've guessed the number!"
    else:
        print("Congratulations! You've guessed the number!")