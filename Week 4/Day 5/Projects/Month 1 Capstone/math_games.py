# Create a suite of math games with menu and scoring. 

# Import necessary libraries
import random

# Function to display the main menu
def display_menu():
    print("Welcome to the Math Games!")
    print("1. Hi-Lo Game")
    print("2. Addition Game")
    print("3. Subtraction Game")
    print("4. Multiplication Game")
    print("5. Division Game")
    print("6. Exit")

# Function for Hi-Lo Game
def hi_lo_game():
    number_to_guess = random.randint(1, 100) # Random number between 1 and 100
    attempts = 0 # Initialize attempts
    print("Welcome to the Hi-Lo Game! Guess a number between 1 and 100.")
    
    while True: # Loop until the user guesses correctly
        guess = int(input("Enter your guess: ")) 
        attempts += 1 # Increment attempts
        if guess < number_to_guess: # Check if guess is too low
            print("Too low!")
        elif guess > number_to_guess: # Check if guess is too high
            print("Too high!")
        else:
            # Correct guess using f-string for formatted output of number and attempts
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Function for Addition Game
def addition_game():
    score = 0
    print("Welcome to the Addition Game! Solve as many problems as you can.")
    
    for _ in range(5):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        answer = num1 + num2
        user_answer = int(input(f"What is {num1} + {num2}? "))
        
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    
    print(f"Your total score is {score}/5.")

# Function for Subtraction Game
def subtraction_game():
    score = 0
    print("Welcome to the Subtraction Game! Solve as many problems as you can.")
    
    for _ in range(5):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        if num1 < num2:
            num1, num2 = num2, num1  # Ensure no negative results
        answer = num1 - num2
        user_answer = int(input(f"What is {num1} - {num2}? "))
        
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    
    print(f"Your total score is {score}/5.")

# Function for Multiplication Game
def multiplication_game():
    score = 0
    print("Welcome to the Multiplication Game! Solve as many problems as you can.")
    
    for _ in range(5):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        answer = num1 * num2
        user_answer = int(input(f"What is {num1} * {num2}? "))
        
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    
    print(f"Your total score is {score}/5.")

# Function for Division Game
def division_game():
    score = 0
    print("Welcome to the Division Game! Solve as many problems as you can.")
    
    for _ in range(5):
        num2 = random.randint(1, 12)
        num1 = num2 * random.randint(1, 12)  # Ensure num1 is a multiple of num2
        answer = num1 // num2
        user_answer = int(input(f"What is {num1} / {num2}? "))
        
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    
    print(f"Your total score is {score}/5.")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Choose a game (1-6): ")
        
        if choice == '1':
            hi_lo_game()
        elif choice == '2':
            addition_game()
        elif choice == '3':
            subtraction_game()
        elif choice == '4':
            multiplication_game()
        elif choice == '5':
            division_game()
        elif choice == '6':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")
        print("\n")  # Add a newline for better readability

if __name__ == "__main__": # Run the main function
    main() 