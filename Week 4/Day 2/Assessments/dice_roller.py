# Create a program that only stops when the user chooses to quit
# Random dice roller for table top games
# Import the random module to generate random numbers
import random

print("Welcome to the D&D Dice Roller!")

# Loop until the user decides to quit
while True:
    print("\nChoose a die to roll: ")
    print("1. d4")
    print("2. d6")
    print("3. d8")
    print("4. d10")
    print("5. d12")
    print("6. d20")
    print("7. d100")
    print("8. Quit")

    choice = input("Enter your choice: ").strip() # Using string methods to validate input

    if choice == '1':
        result = random.randint(1, 4) 
        print(f"You rolled a d4 and got: {result}")
    elif choice == '2':
        result = random.randint(1, 6)
        print(f"You rolled a d6 and got: {result}")
    elif choice == '3':
        result = random.randint(1, 8)
        print(f"You rolled a d8 and got: {result}")
    elif choice == '4':
        result = random.randint(1, 10)
        print(f"You rolled a d10 and got: {result}")
    elif choice == '5':
        result = random.randint(1, 12)
        print(f"You rolled a d12 and got: {result}")
    elif choice == '6':
        result = random.randint(1, 20)
        print(f"You rolled a d20 and got: {result}")
    elif choice == '7':
        result = random.randint(1, 100)
        print(f"You rolled a d100 and got: {result}")
    elif choice == '8':
        print("Thank you for using the D&D Dice Roller. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")