# Greet user and ask if they would like to write a story
print("Hello! Would you like to write a story? (yes/no)")

# Get user input
answer = input().lower()

# If user answers yes, proceed to ask for words to fill in the story
if answer.lower() == "yes":
    print("Great! Let's get started.")
    
    # Ask for a series of words to fill in the story
    name = input("Enter a name: ").strip().title()
    
    place = input("Enter a place: " ).strip().capitalize()

    adjective = input("Enter an adjective: ").strip().lower()

    food = input("Enter a type of food: ").strip().lower()

    verb = input("Enter a verb: ").strip().lower()
    
    # Create the story using the provided words
    story = f"""One day, {name} went to {place}.
    It was a very {adjective} day, perfect for eating {food}.
    While {verb}ing, {name} shouted, "What a wonderful day!" """
    
    # Print the completed story
    print(story)