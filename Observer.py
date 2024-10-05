# Observer.py
class Observer:
    """
    Observer class that will be notified of occasion triggers.
    """
    def update(self, occasion):
        """
        Print a message when an occasion is reached.
        """
        print(f"[INFO] Occasion '{occasion.name}' has been reached at {occasion.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
