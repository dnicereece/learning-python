# Create five usefule functions and practice calling them

# Define a function to check if a word is a palindrome
def is_palindrome(word):
    return word.lower().strip() == word.lower().strip() [::-1] # Strip spaces and ignore case. Check if word reads the same forwards and backwards

# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32 # Use the formula to convert Celsius to Fahrenheit

# Define a function to capitalize the first letter of each word in a sentence
def capitalize_sentence(sentence):
    return sentence.title() # Use the title method to capitalize each word

# Define an alternate function to capitalize the first letter of each word in a sentence
def capitalize_sentence_alternate(sentence2):
    return " ".join(word.capitalize() for word in sentence2.split()) # Split the sentence into words, capitalize each word, and join them back together

# Define a function to find the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Define a function to calculate how much to tip at a restaurant
def calculate_tip(amount, percentage):
    return round(amount * (percentage / 100), 2)

# Call the functions with example inputs and print the results
print(is_palindrome("Racecar"))
print(celsius_to_fahrenheit(25))
print(capitalize_sentence("hello world from python"))
print(capitalize_sentence("They're here today!"))
print(capitalize_sentence_alternate("hello world from python"))
print(capitalize_sentence_alternate("they're here today!"))
print(factorial(5))
print(calculate_tip(100, 15))