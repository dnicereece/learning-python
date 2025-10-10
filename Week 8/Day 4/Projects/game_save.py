# Game save system to preserve game state between sessions using JSON. 

import json
import os

SAVE_FILE = "game_state.json"

def save_game(state):
    """Save the game state to a JSON file."""
    with open(SAVE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def load_game():
    """Load the game state from a JSON file."""
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, "r") as f:
        return json.load(f)

# Example usage:
if __name__ == "__main__":
    # Example game state
    game_state = {
        "level": 3,
        "score": 1500,
        "player": {
            "name": "Hero",
            "health": 75,
            "inventory": ["sword", "shield", "potion"]
        }
    }
    save_game(game_state)
    loaded_state = load_game()
    print(loaded_state)