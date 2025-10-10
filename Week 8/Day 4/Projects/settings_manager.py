# Save and load user settings to/from a json file
import json
import os

SETTINGS_FILE = "settings.json"
DEFAULT_SETTINGS = {
    "theme": "light",
    "notifications": True,
    "language": "en"
}

def load_settings(file=SETTINGS_FILE):
    """
    Loads settings from the specified JSON file.
    If the file does not exist or is invalid, returns an empty dictionary.
    """
    if os.path.exists(file):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: {file} contains invalid data.")
        except Exception as e:
            print(f"Error reading {file}: {e}")
    return {}

def save_settings(settings, file=SETTINGS_FILE):
    """
    Saves settings to the specified JSON file.
    """
    try:
        with open(file, "w") as f:
            json.dump(settings, f, indent=4)
    except Exception as e:
        print(f"Error writing to {file}: {e}")

def reset_settings(file=SETTINGS_FILE):
    """
    Resets settings by deleting the settings file if it exists.
    """
    if os.path.exists(file):
        try:
            os.remove(file)
            print("Settings reset successfully.")
        except Exception as e:
            print(f"Error resetting settings: {e}")
    else:
        print("No settings file to reset.")

def update_setting(key, value, file=SETTINGS_FILE):
    """
    Updates a specific setting in the settings file.
    """
    try:
        settings = load_settings(file)
        settings[key] = value
        save_settings(settings, file)
    except Exception as e:
        print(f"Error updating setting: {e}")

def get_setting(key, default=None, file=SETTINGS_FILE):
    """
    Retrieves a specific setting from the settings file.
    Returns the default value if the key does not exist.
    """
    try:
        settings = load_settings(file)
        return settings.get(key, default)
    except Exception as e:
        print(f"Error retrieving setting: {e}")
        return default
    
# Example usage
save_settings(DEFAULT_SETTINGS)
print(load_settings())

