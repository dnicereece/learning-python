# Check temperature and suggest clothing
# Define the function
def suggest_clothing(temperature):
    if temperature < 32:
        return "Wear a heavy coat, gloves, and a hat."
    elif 32 <= temperature < 50:
        return "Wear a coat and a scarf."
    elif 50 <= temperature < 65:
        return "A light jacket or sweater is fine."
    else:
        return "Wear shorts and a t-shirt."
# Get user input and display the suggestion
temp = float(input("Enter the temperature in Farenheight: "))
suggestion = suggest_clothing(temp)
print(f"At {temp}°F, {suggestion}")
# Get user input and display the suggestion