# Check if a number is positive or negative
# Define the functionto
def is_positive_or_negative(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
# Get user input and display the result
num = float(input("Enter a number: "))
result = is_positive_or_negative(num)
print(f"The number {num} is {result}.")
