# Configuration system for persistent settings storage
# Imports
import json
import os

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

# Main function to demonstrate configuration management
def main():
    file_path = 'config_system.json'
    config = load_config(file_path)
    
    while True:
        print("\nConfiguration Manager")
        print("1. Set Configuration Option")
        print("2. Get Configuration Option")
        print("3. Display All Configurations")
        print("4. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            key = input("Enter configuration key: ")
            value = input("Enter configuration value: ")
            config = set_config_option(config, key, value)
            print(f"Configuration option '{key}' set to '{value}'.")
        elif choice == '2':
            key = input("Enter configuration key to retrieve: ")
            value = get_config_option(config, key)
            if value is not None:
                print(f"Configuration option '{key}': '{value}'")
            else:
                print(f"Configuration option '{key}' not found.")
        elif choice == '3':
            display_config(config)
        elif choice == '4':
            save_config(file_path, config)
            print("Configuration saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()