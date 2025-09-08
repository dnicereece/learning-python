# Restaurant recommendation using several criteria

# Get cusine preference, price range, and distance from user
cuisine = input("What type of cuisine do you prefer, Italian, Chinese, or Mexican? ").strip().lower()
price_range = input("What is your price range (cheap, moderate, expensive)? ").strip().lower()
distance = input("How far are you willing to travel (near, moderate, far)? ").strip().lower()

# Recommend a restaurant based on the criteria
if cuisine == "italian" and price_range == "cheap" and distance == "near":
    print("We recommend 'Luigi's Pizzeria'.")
elif cuisine == "italian" and price_range == "cheap" and distance == "moderate":
    print("We recommend 'Pasta House'.")
elif cuisine == "italian" and price_range == "cheap" and distance == "far":
    print("We recommend 'Mama Mia's'.")
elif cuisine == "italian" and price_range == "moderate" and distance == "near":
    print("We recommend 'Olive Garden'.")
elif cuisine == "italian" and price_range == "moderate" and distance == "moderate":
    print("We recommend 'Carrabba's'.")
elif cuisine == "italian" and price_range == "moderate" and distance == "far":
    print("We recommend 'Maggiano's Little Italy'.")
elif cuisine == "italian" and price_range == "expensive" and distance == "near":
    print("We recommend 'Ristorante Italiano'.")
elif cuisine == "italian" and price_range == "expensive" and distance == "moderate":
    print("We recommend 'Il Fornaio'.")
elif cuisine == "italian" and price_range == "expensive" and distance == "far":
    print("We recommend 'Buca di Beppo'.")
elif cuisine == "chinese" and price_range == "cheap" and distance == "near":
    print("We recommend 'Panda Express'.")
elif cuisine == "chinese" and price_range == "cheap" and distance == "moderate":
    print("We recommend 'Great Wall'.")
elif cuisine == "chinese" and price_range == "cheap" and distance == "far":
    print("We recommend 'Dragon City'.")
elif cuisine == "chinese" and price_range == "moderate" and distance == "near":
    print("We recommend 'P.F. Chang's'.")
elif cuisine == "chinese" and price_range == "moderate" and distance == "moderate":
    print("We recommend 'Hakkasan'.")
elif cuisine == "chinese" and price_range == "moderate" and distance == "far":
    print("We recommend 'Din Tai Fung'.")
elif cuisine == "chinese" and price_range == "expensive" and distance == "near":
    print("We recommend 'Mr. Chow'.")
elif cuisine == "chinese" and price_range == "expensive" and distance == "moderate":
    print("We recommend 'Mott 32'.")
elif cuisine == "chinese" and price_range == "expensive" and distance == "far":
    print("We recommend 'The Eight'.")
elif cuisine == "mexican" and price_range == "cheap" and distance == "near":
    print("We recommend 'Taco Bell'.")
elif cuisine == "mexican" and price_range == "cheap" and distance == "moderate":
    print("We recommend 'El Pollo Loco'.")
elif cuisine == "mexican" and price_range == "cheap" and distance == "far":
    print("We recommend 'Qdoba Mexican Eats'.")
elif cuisine == "mexican" and price_range == "moderate" and distance == "near":
    print("We recommend 'Chipotle Mexican Grill'.")
elif cuisine == "mexican" and price_range == "moderate" and distance == "moderate":
    print("We recommend 'Moe's Southwest Grill'.")
elif cuisine == "mexican" and price_range == "moderate" and distance == "far":
    print("We recommend 'On The Border'.")
elif cuisine == "mexican" and price_range == "expensive" and distance == "near":
    print("We recommend 'Cantina Laredo'.")
elif cuisine == "mexican" and price_range == "expensive" and distance == "moderate":
    print("We recommend 'Frontera Grill'.")
elif cuisine == "mexican" and price_range == "expensive" and distance == "far":
    print("We recommend 'Del Frisco's Double Eagle Steakhouse'.")
else:
    print("Sorry, we have no recommendations based on your criteria.")
        