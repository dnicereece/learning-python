# Create program that collects and displays favorite movies.
# Define the menu
def display_menu():
    """
    Display the favorite movies menu options.
    """
    print("\nFavorite Movies Menu:")
    print("1. Add movie(s)")
    print("2. View movies")
    print("3. Remove movie by index")
    print("4. Sort movies alphabetically")
    print("5. Insert movie at specific index")
    print("0. Exit\n")
# Define the function to add an item and convert to title case
def add_movie(movies):
    """
    Add a movie to the list after converting the title to title case.
    """
    movies_to_add = input("Enter the movie title or titles, separated by a comma: ").strip().title()
    if movies_to_add:
        movies.extend(movie.strip() for movie in movies_to_add.split(","))
        print(f'Added "{movies_to_add}" to the favorite movies list.')
    else:
        print("No movie title entered. Please try again.")
# Define the function to view items
def view_movies(movies):
    """
    Display the list of favorite movies.
    """
    if movies:
        print("Favorite Movies:")
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. {movie}")
    else:
        print("No favorite movies found.")
# Define the function to remove an item based on index
def remove_movie(movies):
    """
    Remove a movie from the list based on its index.
    """
    view_movies(movies)
    try:
        index = int(input("Enter the index of the movie to remove: ")) - 1
        if 0 <= index < len(movies):
            removed_movie = movies.pop(index)
            print(f'Removed "{removed_movie}" from the favorite movies list.')
            view_movies(movies)
        else:
            print("Index out of range. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric index.")
# Define the function to sort the list alphabetically
def sort_movies(movies):
    """
    Sort the list of favorite movies alphabetically.
    """
    movies.sort()
    print("Sorted the favorite movies list alphabetically.")
    view_movies(movies)
# Define the function to insert an item at a specific index
def insert_movie(movies):
    """
    Insert a movie into the list at a specific index.
    """
    view_movies(movies)
    try:
        index = int(input(f"Enter the index to insert the movie at. Enter {len(movies) + 1} if adding to the end: ")) - 1
        movie = input("Enter the movie title: ").strip().title()
        if 0 <= index <= len(movies) and movie:
            movies.insert(index, movie)
            print(f'Inserted "{movie}" into the favorite movies list at index {index + 1}.')
            view_movies(movies)
        else:
            print("Invalid index or movie title. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric index.")
# Map menu choices to functions
actions = {
    "1": add_movie,
    "2": view_movies,
    "3": remove_movie,
    "4": sort_movies,
    "5": insert_movie,
}
# Define the main function to run the favorite movies program
def main():
    favorite_movies = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "0":
            print("Exiting the program. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(favorite_movies)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()