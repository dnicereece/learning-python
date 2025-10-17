"""
Multiple objects in Python can interact with each other in various ways, primarily through 
method calls, attribute access, and shared data structures.
"""

# Passing Objects as Arguments:
"""
One common way for objects to interact is by passing one object as an argument to a method of 
another object. This allows the receiving object to access the attributes and call the methods 
of the passed object.
"""
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        damage = 10
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} now has {self.health} health.")

player = Character("Hero", 100)
enemy = Character("Goblin", 50)

player.attack(enemy)

#  Composition (Has-A Relationship):
"""
One object can contain another object as an attribute, establishing a "has-a" relationship. 
This allows the containing object to delegate tasks or access data from the contained object.
"""
class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self, make):
        self.make = make
        self.engine = Engine() # Car has an Engine

    def drive(self):
        self.engine.start()
        print(f"The {self.make} car is driving.")

my_car = Car("Toyota")
my_car.drive()

# Shared Data Structures:
"""
Objects can interact by modifying and accessing shared data structures, such as lists, 
dictionaries, or custom data structures, that are accessible to multiple objects.
"""
class DataProducer:
    def __init__(self, shared_list):
        self.shared_list = shared_list

    def produce_data(self, item):
        self.shared_list.append(item)
        print(f"Produced: {item}")

class DataConsumer:
    def __init__(self, shared_list):
        self.shared_list = shared_list

    def consume_data(self):
        if self.shared_list:
            item = self.shared_list.pop(0)
            print(f"Consumed: {item}")
        else:
            print("No data to consume.")

shared_data = []
producer = DataProducer(shared_data)
consumer = DataConsumer(shared_data)

producer.produce_data("Item A")
consumer.consume_data()
producer.produce_data("Item B")
consumer.consume_data()

#Event-Driven Interaction (Observer Pattern):
"""
For more complex interactions, especially when one object needs to notify others about changes 
or events, the Observer pattern can be used. One object (the "subject") maintains a list of 
dependent objects (the "observers") and notifies them of any state changes.
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Observer {self.name} received: {message}")

subject = Subject()
obs1 = Observer("A")
obs2 = Observer("B")

subject.attach(obs1)
subject.attach(obs2)

subject.notify("Something important happened!")