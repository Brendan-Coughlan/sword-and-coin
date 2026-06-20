class Game:
    def __init__(self):
        self.hp = 100
        self.gold = 50
        self.COMMANDS = {
            "look": self.look,
            "inventory": self.inventory,
            "attack": self.attack,
            "rest": self.rest,
        }

    def look(self):
        print("You are standing in a small village.")

    def inventory(self):
        print(f"HP: {self.hp}")
        print(f"Gold: {self.gold}")

    def attack(self):
        print("You swing your sword!")

    def rest(self):
        self.hp = min(100, self.hp + 20)
        print(f"You rest and recover health. HP = {self.hp}")

    def run(self):
        print("Welcome to Sword & Coin!")

        while True:
            user_input = input("> ").strip().lower()
            
            if user_input == "quit":
                break
            
            handler = self.COMMANDS.get(user_input)
            
            if handler:
                handler()
            else:
                print("Unknown command.")
