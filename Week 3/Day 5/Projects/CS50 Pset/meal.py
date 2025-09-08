# Create a program that determines a meal suggestion based on time of day
# Define the main function
def main():
    # Define the time variable and get user input
    time = input("What time is it (in 24-hour format, e.g., 13:00)? ").strip()
    if time >= "7" and time <= "8":
        print("breakfast")
    elif time >= "12" and time <= "13":
        print("lunch")
    elif time >= "18" and time <= "19":
        print("dinner")
    else:
        print("snack")


# Define a helper function to convert time to a float
def convert(time):
    hours, minutes = time.split(":") # Split the time into hours and minutes
    return float(hours) + ((minutes) / 60) # Convert to float

# Call the main function
if __name__ == "__main__":
    main()