from location import Location
import random

class Room:
    def __init__(self, room_number, event_type):
        self.room_number = room_number
        self.event_type = event_type
        self.cleared = False

    def display(self):
        print(f"=== Room {self.room_number} ===")

        if self.event_type == "enemy":
            print("An enemy lurks here.")

        elif self.event_type == "loot":
            print("You spot something valuable.")

        elif self.event_type == "trap":
            print("Something feels dangerous.")

        else:
            print("The room is empty.")