# Occasion.py
from datetime import datetime


class Occasion:
    def __init__(self, name, timestamp):
        self.name = name
        try:
            # Parse timestamp string into a datetime object (local time)
            self.timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
            print(f"[DEBUG] Parsed timestamp for '{self.name}': {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        except ValueError as e:
            print(f"[ERROR] Error parsing timestamp for '{self.name}': {e}")
            self.timestamp = None
