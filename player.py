from inventory import Inventory

class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.xp = 0
        self.level = 1
        self.stats = {
            "hp": 100,
            "strength": 10,
            "defense": 10,
            "luck": 5
        }
        self.inventory = Inventory()

    def display_stats(self):
        print(f"{self.name}'s Stats:")
        for stat, value in self.stats.items():
            print(f"  {stat.capitalize()}: {value}")