import json
import os

# Configuration manager that validates file contents.

class ConfigValidationError(Exception):
    pass

class ConfigManager:
    def __init__(self, config_path, required_keys=None):
        self.config_path = config_path
        self.required_keys = required_keys or []
        self.config = self._load_and_validate()

    def _load_and_validate(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        with open(self.config_path, 'r') as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError as e:
                raise ConfigValidationError(f"Invalid JSON: {e}")

        missing_keys = [key for key in self.required_keys if key not in config]
        if missing_keys:
            raise ConfigValidationError(f"Missing required keys: {missing_keys}")

        return config

    def get(self, key, default=None):
        return self.config.get(key, default)

# config.json: {"host": "localhost", "port": 8080}
manager = ConfigManager("config.json", required_keys=["host", "port"])
host = manager.get("host")
port = manager.get("port")

print(f"Config loaded successfully:\nHost: {host}\nPort: {port}")
# Or, to print the whole config:
# print("Full config:", manager.config)