# Create a chatbot that answers yes/no questions
print("Hello! I can answer your yes/no questions.")

import random # Import module to generate random responses

# Loop to keep the chatbot running
while True: 
    question = input("Please ask your question. Type 'exit' to quit: ")
    if question.lower() == "exit":
        print("Goodbye!")
        break
    elif question.strip(): 
        answer = random.choice(["Yes", "No",])
        print(f"Bot: {answer}") 
    else:
        print("Bot: Please ask yes or no questions!")