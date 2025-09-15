def greet(name):
    print(f"Hello, {name}!")
    return f"Greeting sent to {name}"

main_greeting = greet(input("Enter your name: ").title().strip())
print(main_greeting)
