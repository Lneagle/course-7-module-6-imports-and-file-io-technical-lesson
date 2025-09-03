from datetime import datetime
import os

LOG_PATH = "data/user_logs.txt"

def log_action(action, log_file=LOG_PATH):
    """Append a user action with a timestamp to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a") as file:
            file.write(f"[{timestamp}] {action}\n")
    except FileNotFoundError:
        with open(log_file, "w") as file:
            file.write(f"[{timestamp}] {action}\n")
    # TODO: Print confirmation message to the user

def search_logs(keyword, log_file=LOG_PATH):
    """Search the log file for lines that match a keyword."""
    try:
        with open(log_file, "r") as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found.")

log_action("User logged in")
log_action("User updated profile")
search_logs("profile")