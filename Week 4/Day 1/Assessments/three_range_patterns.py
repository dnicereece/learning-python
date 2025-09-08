# Create workout timer that counts reps, rest, and sets
for set_number in range(1, 4): # Loop through 3 sets
    print(f"Set {set_number}:")
    for rep in range(1, 6): # Loop through 5 reps
        print(f"  Rep {rep}")
    for rest in range(1, 30): # Loop through 30 seconds of rest
        if rest % 1 == 0: # Print every second
            print(f"    Rest {rest} seconds")
print("Workout complete!") # Indicate workout is complete