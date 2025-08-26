# Unit Converter: Feet to Meters

print("Welcome to the Feet to Meters Converter!")
feet = input("Enter length in feet: ")  # input returns a string

# Convert input to float for calculation
feet = float(feet)

# Conversion: 1 foot = 0.3048 meters
meters = feet * 0.3048

print(f"{feet} feet is equal to {meters}")