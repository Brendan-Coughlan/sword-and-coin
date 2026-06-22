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

    def display_stats(self):
        print(f"{self.name}'s Stats:")
        for stat, value in self.stats.items():
            print(f"  {stat.capitalize()}: {value}")
        print(f"  Gold: {self.gold}")