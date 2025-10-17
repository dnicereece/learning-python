# Game statistics module to track player count and high scores using class variables and instance variables and class decorators
class GameStats:
    # Class variable to keep track of total players
    total_players = 0

    def __init__(self, player_name):
        # Instance variable
        self.player_name = player_name
        self.high_score = 0
        # Increment the class variable when a new player is created
        GameStats.total_players += 1

    @classmethod
    def get_total_players(cls):
        return cls.total_players

    @staticmethod
    def game_rules():
        return "Players must achieve high scores to win the game."
    
# Creating multiple GameStats objects
player1 = GameStats("Alice")
player2 = GameStats("Bob")
player3 = GameStats("Charlie")

# Displaying player information
print(f"Player 1: {player1.player_name}, High Score: {player1.high_score}")
print(f"Player 2: {player2.player_name}, High Score: {player2.high_score}")
print(f"Player 3: {player3.player_name}, High Score: {player3.high_score}")

# Displaying total players
print(f"Total Players: {GameStats.get_total_players()}")

# Displaying game rules
print(GameStats.game_rules())