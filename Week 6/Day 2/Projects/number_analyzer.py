# Create a practice program to analyze a list of numbers and generate statistics such as average, maximum, and minimum.
# Practice difference between 'for i in range' and 'for item in list'
# Get user input for a list of numbers
print("Enter numbers. Press Enter on a blank line to finish.")
numbers = []
while True:
    raw = input("> ").strip()
    if raw == "":
        break
    try:
        numbers.append(float(raw))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if not numbers:
    print("No numbers were entered.")
    exit()

# Using 'for item in list to find sum and average
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(f"Sum: {total}")
print(f"Average: {average}")

# Using 'for i in range' to find max and min
max_num = numbers[0]
min_num = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max_num:
            max_num = numbers[i]
    if numbers[i] < min_num:
            min_num = numbers[i]
print(f"Max: {max_num}")
print(f"Min: {min_num}")
