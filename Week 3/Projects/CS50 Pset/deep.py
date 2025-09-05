# Ask the user for the answer to the Great Question of Life, the Universe, and Everything
answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
# Respond based on the user's input
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
    