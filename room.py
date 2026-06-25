from enemy import Enemy
from item import Item

class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.description = f"This is room {room_number}."
        self.enemies = [
            Enemy("Goblin", hp=30, strength=5, defense=2, xp_reward=10, gold_reward=5)
        ]
        self.loot = [
            Item("Goblin Ear", "A trophy from a defeated goblin", value=5)
        ]
        self.cleared = False

    def display(self):
        print(self.description)

        if self.enemies or self.loot:
            print(
                f"This room contains {len(self.enemies)} enemies and {len(self.loot)} loot items."
            )
        else:
            print("This room is empty.")