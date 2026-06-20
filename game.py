from commands import *

class Game:
    def __init__(self):
        self.hp = 100
        self.gold = 50

    def cmd_look(self):
        print("You are standing in a small village.")

    def cmd_inventory(self):
        print(f"HP: {self.hp}")
        print(f"Gold: {self.gold}")

    def cmd_attack(self, target):
        print(f"You swing your sword at {target}!")

    def cmd_rest(self):
        self.hp = min(100, self.hp + 20)
        print(f"You rest and recover health. HP = {self.hp}")

    def handle_command(self, command_name, *args):
        parts = command_name.split()

        if not parts:
            return

        command_name = parts[0] if parts else ""
        args = parts[1:] if len(parts) > 1 else []

        command = COMMANDS.get(command_name)

        if not command:
            print("Unknown command.")
            return
        
        expected_args = len(command["args"])
        
        if len(args) < expected_args:
            print(f"Usage: {command_name} {' '.join(f'<{a}>' for a in command['args'])}")
            return

        handler = getattr(self, command["handler"], None)

        if handler:
            handler(*args)

    def run(self):
        print("Welcome to Sword & Coin!")

        while True:
            user_input = input("> ").strip().lower()

            if user_input == "quit":
                break

            self.handle_command(user_input)
