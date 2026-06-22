from inventory import Inventory

class Player:
    def __init__(self, name, starting_gold=50):
        self.name = name
        self.gold = starting_gold
        self.stats = {
            "hp": 100,
            "strength": 10,
            "defense": 10,
            "luck": 5
        }
        self.inventory = Inventory()

    def __str__(self):
        result = f"{self.name}'s Stats:\n"
        for stat, value in self.stats.items():
            result += f"  {stat.capitalize()}: {value}\n"
        result += f"  Gold: {self.gold}"
        return result