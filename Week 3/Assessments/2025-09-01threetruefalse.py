# Determine if a number is even, prime, or a multiple of 3
number = int(input("Enter a number: "))

# Boolean checks
is_even = (number % 2 == 0)
is_multiple_of_3 = (number % 3 == 0)
    # Prime check
if number > 1:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
else:
    is_prime = False

# Print results
print(f"Is the number even? {is_even}")
print(f"Is the number prime? {is_prime}")
print(f"Is the number a multiple of 3? {is_multiple_of_3}")

