# Player and Enemy Character Classes for a Game

class PlayerCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self):
        return f"{self.name} attacks with a sword!"
    
    def defend(self):
        return f"{self.name} raises a shield to defend!"

class EnemyCharacter:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def attack(self):
        return f"{self.name} lunges at you with claws!"
    
    def defend(self):
        return f"{self.name} braces for impact!"

# Creating multiple PlayerCharacter objects
player1 = PlayerCharacter("Archer", 5)
player2 = PlayerCharacter("Mage", 7)
player3 = PlayerCharacter("Warrior", 10)

# Creating multiple EnemyCharacter objects
enemy1 = EnemyCharacter("Goblin", 3)
enemy2 = EnemyCharacter("Troll", 8)
enemy3 = EnemyCharacter("Dragon", 15)

# Displaying PlayerCharacter information and attacks
print(f"{player1.name}, Level: {player1.level}")
print(player1.attack())
print(f"{player2.name}, Level: {player2.level}")
print(player2.attack())
print(f"{player3.name}, Level: {player3.level}")
print(player3.attack())

# Displaying EnemyCharacter information and attacks
print(f"{enemy1.name}, Strength: {enemy1.strength}")
print(enemy1.attack())
print(f"{enemy2.name}, Strength: {enemy2.strength}")
print(enemy2.attack())
print(f"{enemy3.name}, Strength: {enemy3.strength}")
print(enemy3.attack())

# Characters attacking each other
print(f"{player1.name} vs {enemy1.name}:")
print(player1.attack())
print(enemy1.defend())