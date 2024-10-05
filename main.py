# main.py
from datetime import timedelta, datetime

from Observer import Observer
from Occasion import Occasion
from OccasionNotifier import OccasionNotifier


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Current local time
    current_time = datetime.now()
    print(f"[INFO] Current Local Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # List of occasions with their name and timestamp set a few minutes ahead
    occasions_data = [
        {
            "name": "occasion 1",
            "timestamp": (current_time + timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%M:%S.%f")
        },
        {
            "name": "occasion 2",
            "timestamp": (current_time + timedelta(minutes=2)).strftime("%Y-%m-%dT%H:%M:%S.%f")
        },
    ]

    # Create an OccasionNotifier and Observer
    notifier = OccasionNotifier()
    observer = Observer()

    # Add the observer to the notifier
    notifier.add_observer(observer)

    # Create Occasion objects from the data and add them to the notifier
    for occ in occasions_data:
        try:
            occasion = Occasion(occ["name"], occ["timestamp"])
            notifier.add_occasion(occasion)
            print(f"[INFO] Added occasion: {occasion.name} at {occasion.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        except ValueError as e:
            print(f"[ERROR] Error parsing timestamp for {occ['name']}: {e}")

    # Start the notifier to begin checking for occasions
    notifier.start()
