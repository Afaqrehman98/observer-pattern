# OccasionNotifier.py
import time
from datetime import datetime


class OccasionNotifier:
    """
    Observable class that stores occasions and notifies observers when
    an occasion time is reached.
    """
    def __init__(self):
        self.occasions = []  # List of Occasion objects
        self.observers = []  # List of observer objects

    def add_occasion(self, occasion):
        """
        Add an occasion to the notifier's list.
        """
        self.occasions.append(occasion)
        print(f"[DEBUG] Added occasion: {occasion.name} at {occasion.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    def add_observer(self, observer):
        """
        Add an observer to be notified when occasions are triggered.
        """
        self.observers.append(observer)
        print(f"[DEBUG] Observer added.")

    def notify_observers(self, occasion):
        """
        Notify all observers that the occasion time has been reached.
        """
        for observer in self.observers:
            observer.update(occasion)

    def start(self):
        """
        Start checking for occasions periodically.
        """
        print("[INFO] Notifier started. Waiting for occasions...")
        while self.occasions:
            now = datetime.now()  # Get the current local time
            print(f"[DEBUG] Current Local Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            for occasion in self.occasions[:]:
                # If the current time is greater than or equal to the occasion timestamp
                if now >= occasion.timestamp:
                    print(f"[DEBUG] Occasion '{occasion.name}' reached.")
                    self.notify_observers(occasion)
                    self.occasions.remove(occasion)  # Remove the occasion once notified
            time.sleep(1)  # Sleep for 1 second between checks
        print("[INFO] No more occasions to notify.")
