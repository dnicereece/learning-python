# Library class system with book and library classes

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.info())

# Creating multiple Book objects
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald") 

# Creating a Library object
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Showing all books in the library
library.show_books()


