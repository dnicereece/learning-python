# Logging Module that timestamps and records events to a log file

import datetime

log_file_path = "/Users/denisereece/Documents/Intern To Junior Dev 2025/GitHub/learning-python/Week 8/Day 1/Projects/log.txt"

def log_event(event):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_path, "a") as file:
        file.write(f"[{timestamp}] {event}\n")

# Example usage
log_event("Diary entry added.")
log_event("Configuration updated.")