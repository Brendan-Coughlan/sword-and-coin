from location import Location
from room import Room
import random

class Dungeon(Location):
    def __init__(self, name, description, difficulty=1):
        super().__init__(name, description)

        self.difficulty = difficulty
        self.current_room = 0
        self.rooms = {}

    def generate_room(self):
        self.current_room += 1

        event_type = random.choices(
            ["enemy", "loot", "trap", "empty"],
            weights=[50, 25, 15, 10]
        )[0]

        room = Room(self.current_room, event_type)

        self.rooms[self.current_room] = room

        return room

    def move_forward(self):
        room = self.generate_room()

        print()
        room.display()

        return room

    def display(self):
        super().display()
        print(f"Difficulty: {self.difficulty}")
        print(f"Current Room: {self.current_room}")