from commands import *
from dungeon import Dungeon
from enemy import Enemy
from location import Location
from player import Player


class Game:
    def __init__(self):
        self.town = Location("Town", "A bustling town with shops and NPCs.")
        self.dungeon = Dungeon(
            "Dungeon", "A damp cave filled with goblins.", difficulty=1
        )

        self.goblin = Enemy(
            "Goblin", hp=30, strength=5, defense=2, xp_reward=10, gold_reward=5
        )

        self.player = Player("Hero")
        self.location = self.dungeon

    # Command to quit the game
    def cmd_quit(self):
        print("Thanks for playing!")
        exit(0)

    # Command to display the player's current location
    def cmd_location(self):
        self.location.display()

    # Command to display help for a specific command
    def cmd_help(self, command):
        if command in COMMANDS:
            info = COMMANDS[command]
            args = " ".join(f"<{arg}>" for arg in info["args"])
            print(f"  {command} {args} - {info['description']}")
        else:
            print("Command not found.")

    # Stats command to display player stats
    def cmd_stats(self):
        self.player.display_stats()

    # Forward command to move deeper into the dungeon
    def cmd_forward(self):
        if isinstance(self.location, Dungeon):
            self.location.move_forward()
        else:
            print("You can't move forward from here.")

    # Leave command to exit the dungeon and return to town
    def cmd_leave(self):
        if isinstance(self.location, Dungeon):
            self.location = self.town
            print("You leave the dungeon and return to town.")
        else:
            print("You are not in a dungeon.")

    # Travel command to move between locations
    def cmd_travel(self, location_name):
        if self.location.name.lower() == location_name.lower():
            print(f"You are already in {location_name}.")
            return

        if location_name.lower() == "dungeon":
            self.location = self.dungeon
            print("You travel to the dungeon.")
        elif location_name.lower() == "town":
            self.location = self.town
            print("You travel to the town.")
        else:
            print(f"Unknown location: {location_name}")

    # Handle user input and execute the corresponding command
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
            print(
                f"Usage: {command_name} {' '.join(f'<{a}>' for a in command['args'])}"
            )
            return

        handler = getattr(self, command["handler"], None)

        if handler:
            handler(*args)

    # Run the game loop, continuously prompting for user input and handling commands
    def run(self):
        print("Welcome to Sword & Coin!")

        while True:
            user_input = input("> ").strip().lower()

            self.handle_command(user_input)
