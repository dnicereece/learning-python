# Create and rock paper scissors game
import random

while True:
    print("Welcome to Rock, Paper, Scissors! Please choose your weapon.")
    user_choice = input("Type 'rock', 'paper', or 'scissors': ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes' or 'y':
        running = False
        print("Thanks for playing! Goodbye.")   