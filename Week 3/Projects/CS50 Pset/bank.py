# Create a program that gives $0 for variations of "hello", $20 for greetings that start with "h" (but not "hello") and $100 for any other greeting.
greeting = input("Greeting: ").strip().lower()
if greeting == "hello":
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")