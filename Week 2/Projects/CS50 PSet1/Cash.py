# Prompt the user for change owed in cents
while True:
    cents = input("Change owed (cents): ")
    # Validate input to ensure it's a non-negative integer
    if cents.isdigit():
        cents = int(cents)
        if cents >= 0:
            break
    print("Please enter a non-negative integer.")

# Calculate how many quarters you should give customer
quarters = cents // 25
# Subtract the value of those quarters from the total
cents = cents - (quarters * 25)

# Calculate how many dimes you should give customer
dimes = cents // 10
# Subtract the value of those dimes from the total
cents = cents - (dimes * 10)

# Calculate how many nickels you should give customer
nickels = cents // 5
# Subtract the value of those nickels from the total
cents = cents - (nickels * 5)

# Calculate how many pennies you should give customer
pennies = cents // 1
# Subtract the value of those pennies from the total
cents = cents - (pennies * 1)

# Sum the number of quarters, dimes, nickels, and pennies used
coins = quarters + dimes + nickels + pennies
# Print that sum
print(coins)