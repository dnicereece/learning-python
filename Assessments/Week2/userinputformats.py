# Great user and ask if they would like to see different input formats
print("Hello! Would you like to see different input formats? (yes/no)")

# Get user input
answer = input().lower()

# If user answers yes, proceed to show different input formats
if answer == "yes":
    print("Great! Let's get started.")
    
    # Ask for a short sentence
    sentence = input("Enter a short sentence: ").strip()
    print("You entered the sentence:", sentence)

    # Demonstrate title case
    title_case = sentence.title()
    print("Here is your sentence in the Title Case fromat:", title_case)

    # Demonstrate uppercase
    upper_case = sentence.upper()
    print("Here is your sentence in the UPPERCASE format:", upper_case)

    # Demonstrate lowercase
    lower_case = sentence.lower()
    print("Here is your sentence in the lowercase format:", lower_case)

    print("Thanks for trying out different input formats!")