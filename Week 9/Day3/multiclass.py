"""
Creating multiple objects from a single class in Python involves repeatedly calling the class 
constructor, which is the class name followed by parentheses, and assigning each resulting 
object to a distinct variable. Each call to the constructor creates a new, independent instance 
of that class.
"""
# Example
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating multiple Dog objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador")
dog3 = Dog("Max", "German Shepherd")

# Each object is distinct and can have different attribute values
print(f"{dog1.name} is a {dog1.breed}.")
print(f"{dog2.name} is a {dog2.breed}.")

# Each object can also call its own methods
dog1.bark()
dog3.bark()


# In this example:
"""
-A Dog class is defined with an __init__ method to initialize name and breed attributes, and a 
bark method.

-dog1, dog2, and dog3 are created as separate instances of the Dog class by calling Dog() with 
different arguments.

-Each object (dog1, dog2, dog3) holds its own unique data (name and breed) and can independently 
invoke the bark() method.

This process allows for the creation of numerous objects from a single class blueprint, each 
representing a unique entity with its own state.
"""