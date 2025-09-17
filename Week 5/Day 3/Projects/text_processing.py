# Create a text processing toolkit using functions
print("Welcome to the Text Processing Toolkit!")
# Define a function to display the menu system
def menu():
    print("\nMenu:")
    print("1. Count Words")
    print("2. Count Characters")
    print("3. Most Common Character")
    print("4. Enter new text to Analyze")
    print("5. Exit")
# Define a function to count the number of words in a text
def count_words(text):
    return len(text.split()) # Return the number of words by splitting the text based on spaces
# Define a function to find the character counnt in a text
def count_char(text):
    return len(text) # Return the number of characters in the text
# Define a function to find the most common character in a text
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
# Define the main function to get user input and call the appropriate function
def main():
    text = "" # Initialize an empty string to hold the text input
    while True:
        menu()
        if not text:
            text = input("Enter the text to analyze: ") # Get text input from the user
        choice = input("Please select an option (1-5): ")
        if choice == '1':
            print(f"Word Count: {count_words(text)}")
        elif choice == '2':
            print(f"Character Count: {count_char(text)}")
        elif choice == '3':
            common_char, count = most_common_char(text) # Get the most common character and its count
            print(f"Most Common Character: '{common_char}' appears {count} times")
        elif choice == '4':
            text = input("Enter the new text to analyze: ")
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
# Run the text processing program
if __name__ == "__main__":
    main()