from enemy import Enemy

class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.description = f"This is room {room_number}."
        self.enemies = [
            Enemy("Goblin", hp=30, strength=5, defense=2, xp_reward=10, gold_reward=5)
        ]
        self.loot = []
        self.cleared = False

    def display(self):
        print(self.description)

        if self.enemies:
            print("An enemy lurks here.")
        elif self.loot:
            print("You spot something valuable.")
        else:
            print("The room is empty.")