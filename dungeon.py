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


        room = Room(self.current_room)

        self.rooms[self.current_room] = room

        return room
    
    def get_current_room(self):
        return self.rooms.get(self.current_room, None)

    def move_forward(self):
        room = self.generate_room()

        room.display()

        return room

    def display(self):
        super().display()
        print(f"Difficulty: {self.difficulty}")
        print(f"Current Room: {self.current_room}")