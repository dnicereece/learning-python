# Configuration Save Module that stores program settings in a JSON file

# Configuration system for persistent settings storage
# Imports
import json
import os

file_path = "/Users/denisereece/Documents/Intern To Junior Dev 2025/GitHub/learning-python/Week 8/Day 1/Projects/config.json"

# Function to load configuration from a file
def load_config(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            config = json.load(file)
            return config
    else:
        return {}
    
# Function to save configuration to a file
def save_config(file_path, config):
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)

# Function to set a configuration option
def set_config_option(config, key, value):
    config[key] = value
    return config

# Function to get a configuration option
def get_config_option(config, key):
    return config.get(key, None)

# Function to display all configuration options
def display_config(config):
    if not config:
        print("No configuration options available.")
    else:
        print("\nCurrent Configuration:")
        for key, value in config.items():
            print(f"{key}: {value}")

# Example usage
config = load_config(file_path)
display_config(config)
set_config_option(config, "theme", "light")
set_config_option(config, "font_size", 16)
set_config_option(config, "language", "fr")
save_config(file_path, config)
display_config(config)