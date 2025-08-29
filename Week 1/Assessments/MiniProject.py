# This code will greet the user and ask if they want to see ascii art
print("Hello! Welcome to the gallery. Press 'y' to see some ASCII art or any other key to exit.")

# Prompt user for input
user_input = input("Your choice: ")

# Define some ASCII art pieces
ascii_arts = [
    r"""
     /\_/\
    ( o.o )
     > ^ <
    """,
    r"""
     __
    /  \
    |  |
    \__/
    """,
    r"""
    .-.
   (o o)
    |=|
   __|__
  //.=.\\
 // .=. \\
 \\ .=. //
  \\(_)// 
    """,
    r"""
     _____
    /     \
   | () () |
    \  ^  /
     |||||
     |||||
    """,
    r"""
      _____
     /     \
    |  o o  |
    |   ^   |
     \ \_/ /
      -----
    """
]

# If user wants to see ASCII art, display it, using a loop
if user_input.lower() == 'y':
    # Loop through the ASCII art pieces and display them one by one
    for i, art in enumerate(ascii_arts):
        # Display the ASCII art piece
        print(f"Piece {i+1}:\n{art}")
        # Ask if the user wants to see the next piece
        if i < len(ascii_arts) - 1:
            # Prompt user to continue or exit
            cont = input("Press 'y' to see the next piece or any other key to exit: ")
            # If user does not want to continue, exit the loop
            if cont.lower() != 'y':
                # Exit the loop and say goodbye
                print("Goodbye!")
                #
                break

    # If the user has seen all pieces, say goodbye
    else:
        print("End of gallery. Goodbye!")

# If user does not want to see ASCII art, say goodbye
else:
    print("Goodbye!")