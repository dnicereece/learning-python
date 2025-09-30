# Create a configuration manager to store and retrieve settings using dictionary mehtods and iteration.

settings = {
    "theme": "dark",
    "font_size": 14,
    "font_family": "Arial",
    "language": "en",
}

# Function to update a setting
def update_setting(key, value):
    settings[key] = value

# Function to retrieve a setting
def get_setting(key):
    return settings.get(key, None)

# Function to list all settings
def list_settings():
    for key, value in settings.items():
        print(f"{key}: {value}")

# Update some settings
update_setting("font_size", 16)
update_setting("language", "fr")

# Retrieve and print a specific setting
print(f"Font Size: {get_setting('font_size')}") # Outputs: Font Size: 16
print(f"Language: {get_setting('language')}") # Outputs: Language: fr

# List all settings
print("Current Settings:")
list_settings() 
# Outputs: Current Settings:
#          theme: dark
#          font_size: 16
#          font_family: Arial
#          language: fr

# Clear all settings
settings.clear()
print(f"Settings after clear: {settings}") # Outputs: Settings after clear: {}

# Reinitialize settings
settings = {
    "theme": "dark",
    "font_size": 14,
    "font_family": "Arial",
    "language": "en",
}

# Create a copy of settings
settings_copy = settings.copy()
print(f"Copied Settings: {settings_copy}") # Outputs: Copied Settings: {'theme': 'dark', 'font_size': 14, 'font_family': 'Arial', 'language': 'en'}

# Create new settings from keys
new_keys = ['theme', 'font_size', 'notifications']
new_settings = dict.fromkeys(new_keys, None)
print(f"New Settings from keys: {new_settings}") # Outputs: New Settings from keys: {'theme': None, 'font_size': None, 'notifications': None}

# Update new settings with actual values
new_settings.update(settings)
print(f"Updated New Settings: {new_settings}") # Outputs: Updated New Settings: {'theme': 'dark', 'font_size': 14, 'notifications': None, 'font_family': 'Arial', 'language': 'en'}

# Add value for notifications
new_settings['notifications'] = True
print(f"Final New Settings: {new_settings}") # Outputs: Final New Settings: {'theme': 'dark', 'font_size': 14, 'notifications': True, 'font_family: 'Arial', 'language': 'en'}