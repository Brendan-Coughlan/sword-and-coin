class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item] = self.items.get(item, 0) + 1

    def remove_item(self, item):
        if item in self.items:
            self.items[item] -= 1
            if self.items[item] <= 0:
                del self.items[item]
        else:
            print(f"{item.name} is not in the inventory.")

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item, quantity in self.items.items():
                print(f"- {item}: {quantity}")