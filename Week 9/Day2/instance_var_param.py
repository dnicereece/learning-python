"""
In Python, instance variables and parameters serve distinct roles within the context of classes 
and functions.
"""

# Instance Variables
"""
-Instance variables are variables that belong to a specific instance (object) of a class. Each 
object created from a class will have its own independent set of instance variables.

-They are typically defined and initialized within the __init__ method of a class, prefixed 
with self., which refers to the current instance of the class.

-Instance variables store the unique state or data for each individual object.
"""

class Dog:
    def __init__(self, name, breed):
        self.name = name  # self.name is an instance variable
        self.breed = breed # self.breed is an instance variable

my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Lucy", "Labrador")

print(my_dog.name)  # Output: Buddy
print(your_dog.name) # Output: Lucy

# Parameters
"""
-Parameters are variables defined in a function or method signature that act as placeholders 
for the values (arguments) that will be passed into the function when it is called.

-They define the types and number of inputs a function expects.

-Parameters are local to the function or method in which they are defined and their scope is 
limited to that specific execution.
"""
def greet(name): # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice") # "Alice" is an argument passed to the 'name' parameter
greet("Bob")   # "Bob" is another argument passed to the 'name' parameter

# Key Differences:

## Scope and Ownership: 
"""
Instance variables are owned by and persist with each object instance, while parameters are 
temporary placeholders within a function's execution.
"""
## Purpose: 
"""
Instance variables store the state of an object, while parameters receive input values for a 
function or method to process.
"""
## Declaration: 
"""
Instance variables are declared with self. within a class method (usually __init__), whereas 
parameters are declared in the function or method signature.
"""