"""
In Python, the distinction between class variables and instance variables lies in their scope 
and how they are shared among objects of a class.
"""

# Class Variables:

# Definition: 
"""
Class variables are defined directly within the class body, outside of any methods.
"""
# Scope: 
"""
They are shared by all instances (objects) of that class. Modifying a class variable through 
the class or any instance will affect its value for all other instances.
"""
# Purpose: 
"""
Class variables are typically used for data that is common to all instances, such as constants, 
default values, or shared configurations.
"""
class Car:
    # Class variable
    wheels = 4 

    def __init__(self, color):
        self.color = color # Instance variable

car1 = Car("red")
car2 = Car("blue")

print(f"Car 1 wheels: {car1.wheels}") # Output: Car 1 wheels: 4
print(f"Car 2 wheels: {car2.wheels}") # Output: Car 2 wheels: 4

Car.wheels = 6 # Modifying the class variable
print(f"Car 1 wheels after modification: {car1.wheels}") # Output: Car 1 wheels after modification: 6

# Instance Variables:

# Definition: 
"""
Instance variables are defined within the methods of a class, typically within the __init__ 
method, using the self keyword.
"""
# Scope: 
"""
They are unique to each instance of the class. Each object has its own copy of instance 
variables, and changes to an instance variable in one object do not affect other objects.
"""
# Purpose: 
"""
Instance variables are used to store data that is specific to a particular object, representing 
its individual state or characteristics.
"""
class Car:
    wheels = 4 

    def __init__(self, color):
        # Instance variable
        self.color = color 

car1 = Car("red")
car2 = Car("blue")

print(f"Car 1 color: {car1.color}") # Output: Car 1 color: red
print(f"Car 2 color: {car2.color}") # Output: Car 2 color: blue

car1.color = "green" # Modifying an instance variable for car1
print(f"Car 1 color after modification: {car1.color}") # Output: Car 1 color after modification: green
print(f"Car 2 color after modification: {car2.color}") # Output: Car 2 color after modification: blue (unchanged)