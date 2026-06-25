from data_loader import load_data

class GameData:
    def __init__(self):
        self.items = load_data("data/items.json")
        self.enemies = load_data("data/enemies.json")
        self.locations = load_data("data/locations.json")