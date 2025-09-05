# Create a decision tree when unable to focus

mood = input("How are you feeling today, happy or sad? ").strip().lower()
energy = input("What is your energy level, high or low? ").strip().lower()
environment = input("What is your current environment, quiet or noisy? ").strip().lower()
# Suggest an activity based on the inputs
if mood == "happy" and energy == "high" and environment == "quiet":
    print("You might enjoy going for a run or doing a workout.")
elif mood == "happy" and energy == "high" and environment == "noisy":
    print("You might enjoy dancing or going to a social event.")
elif mood == "happy" and energy == "low" and environment == "quiet":
    print("You might enjoy reading a book or meditating.")
elif mood == "happy" and energy == "low" and environment == "noisy":
    print("You might enjoy watching a movie or listening to music.")
elif mood == "sad" and energy == "high" and environment == "quiet":
    print("You might enjoy journaling or doing a creative activity.")
elif mood == "sad" and energy == "high" and environment == "noisy":
    print("You might enjoy going for a walk or doing some light exercise.")
elif mood == "sad" and energy == "low" and environment == "quiet":
    print("You might enjoy taking a nap or practicing deep breathing.")
elif mood == "sad" and energy == "low" and environment == "noisy":
    print("You might enjoy calling a friend or doing a fun activity.")
else:
    print("Invalid input. Please enter valid options for mood, energy, and environment.")