# Prompt the user to enter a number
print("Hello! Please type a number.")

# Get user input and check if it's an integer
# Check if the input is all digits
while True:
    user_input = input()
    if user_input.isdigit():
        print("Thank you for entering a number.")
        break
    else:
        print("That is not a number. Please try again.")

# After a valid number, prompt for a word
print("Now, please enter a word:")

# Check if word input is valid
while True:
    word_input = input()
    if word_input.isalpha():
        print("Thank you for entering a word.")
        break
    else:
        print("That is not a word. Please try again.")