from inventory import Inventory

class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.xp = 0
        self.level = 1
        self.health = 100
        self.max_health = 100
        self.strength = 10
        self.defense = 5
        self.luck = 1
        self.inventory = Inventory()

    def display_stats(self):
        print(f"{self.name}'s Stats:")
        print(f"  Health: {self.health}/{self.max_health}")
        print(f"  Strength: {self.strength}")
        print(f"  Defense: {self.defense}")
        print(f"  Luck: {self.luck}")

    def gain_xp(self, amount):
        self.xp += amount
        print(f"You gained {amount} XP!")

        # Check for level up
        if self.xp >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.strength += 5
        self.defense += 3
        self.luck += 1

        print(f"Congratulations! You've reached level {self.level}!")

    def take_damage(self, amount):
        damage_taken = max(0, amount - self.defense)
        self.health -= damage_taken
        print(f"You took {damage_taken} damage!")

        if self.health <= 0:
            print("You have been defeated!")

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
        print(f"You healed {amount} health!")

    def gain_gold(self, amount):
        self.gold += amount
        print(f"You gained {amount} gold!")

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            print(f"You spent {amount} gold!")
            return True
        else:
            print("Not enough gold!")
            return False
        
    def add_item(self, item):
        self.inventory.add_item(item)
        print(f"You received: {item.name}!")
    
    def remove_item(self, item_name):
        if self.inventory.remove_item(item_name):
            print(f"You removed: {item_name} from your inventory.")
        else:
            print(f"{item_name} not found in your inventory.")

    def display_inventory(self):
        self.inventory.display()