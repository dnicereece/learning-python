# Creatte a game utility module with functions for dice rolling and score calculation
# Import the random module to generate random numbers
import random
# Define a function to roll a standard six-sided die
def roll_die():
    return random.randint(1, 6) # Return a random integer between 1 and 6
# Define a function to keep track of player score
def calculate_score(current_score, points):
    return current_score + points # Return the updated score by adding points to the current score
# Define the main function as a game loop where the player can roll the die multiple times
def main():
    while True:
        score = 0 # Initialize player score to zero
        rounds = 0 # Initialize round counter
        print("Welcome to the Dice Rolling Game!")
        while True:
            if rounds >= 10: # Limit the game to 10 rounds
                print(f"Game over! Your final score is: {score}")
                break
            choice = input("Press 'r' to roll the die or 'q' to quit: ").lower() # Get user input and convert to lowercase
            if choice == 'r':
                roll = roll_die() # Call the roll_die function to get a die roll
                print(f"You rolled a {roll}!")
                score = calculate_score(score, roll) # Update the score using the calculate_score function
                print(f"Your current score is: {score}")
                rounds += 1 # Increment the round counter
                print(f"Rounds left: {10 - rounds}") # Display remaining rounds
            elif choice == 'q':
                print(f"Thanks for playing! Your final score is: {score}")
                break
            else:
                print("Invalid choice. Please try again.")
        play_again = input("Would you like to play again? (y/n): ").lower() # Ask if the player wants to play again
        if play_again != 'y':
            print("Goodbye!")
            break

# Run the game utility module
if __name__ == "__main__":
    main()