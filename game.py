from commands import *
from dungeon import Dungeon
from enemy import Enemy
from item import Item
from location import Location
from player import Player

TOWN = Location("Town", "A bustling town with shops and NPCs.")
DUNGEON = Dungeon("Dungeon", "A damp cave filled with goblins.", difficulty=1)

ITEMS = {
    "goblin_ear": Item("goblin_ear", "Goblin Ear", "A trophy from a defeated goblin", value=5),
}

class Game:
    def __init__(self):
        self.player = Player("Hero")
        self.location = DUNGEON

    def check_if_in_dungeon(self):
        return isinstance(self.location, Dungeon)

    def check_if_in_combat(self):
        if isinstance(self.location, Dungeon):
            if self.location.get_current_room() and self.location.get_current_room().enemies:
                return True
        return False

    # Command to display the player's current balance
    def cmd_balance(self):
        print(f"Your current balance is: {self.player.gold} gold.")

    # Command to display the player's current XP
    def cmd_xp(self):
        print(f"Your current XP is: {self.player.xp} XP.")

    # Command to attack an enemy
    def cmd_attack(self):
        if not self.check_if_in_dungeon():
            print("You can't attack here.")
            return

        if not self.check_if_in_combat():
            print("There is no enemy to attack.")
            return

        damage = self.player.calculate_attack_damage()
        self.location.get_current_room().enemies[0].take_damage(damage)
        print(f"You attack the {self.location.get_current_room().enemies[0].name} for {damage} damage!")

        if self.location.get_current_room().enemies[0].health <= 0:
            print(f"You have defeated the {self.location.get_current_room().enemies[0].name}!")
            self.player.gain_xp(self.location.get_current_room().enemies[0].xp_reward)
            self.player.gain_gold(self.location.get_current_room().enemies[0].gold_reward)
            self.location.get_current_room().enemies.pop(0)
            return

        self.enemy_turn()

    # Command to flee from an enemy
    def cmd_flee(self):
        if not self.check_if_in_combat():
            print("You are not in combat.")
            return

        print(f"You flee from the {self.location.get_current_room().enemies[0].name}!")

        self.current_enemy = None

    # Command to quit the game
    def cmd_quit(self):
        print("Thanks for playing!")
        exit(0)

    # Command to display the player's current location
    def cmd_location(self):
        self.location.display()

    # Stats command to display player stats
    def cmd_stats(self):
        self.player.display_stats()

    # Command to display the current enemy's stats
    def cmd_enemy(self):
        if not self.check_if_in_combat():
            print("No enemy present.")
            return

        print(
            f"{self.location.get_current_room().enemies[0].name} "
            f"(HP: {self.location.get_current_room().enemies[0].health}/{self.location.get_current_room().enemies[0].max_health})"
        )

    # Forward command to move deeper into the dungeon
    def cmd_forward(self):
        if not self.check_if_in_dungeon():
            print("You can't move forward from here.")
            return

        if self.check_if_in_combat():
            print("You must defeat the current enemy before moving forward!")
            return

        room = self.location.move_forward()

    # Leave command to exit the dungeon and return to town
    def cmd_leave(self):
        if self.check_if_in_dungeon():
            if self.check_if_in_combat():
                print("You must defeat the current enemy before leaving the dungeon!")
                return
            else:
                self.location = TOWN
                print("You leave the dungeon and return to town.")
        else:
            print("You are not in a dungeon.")

    # Travel command to move between locations
    def cmd_travel(self, location_name):
        if self.location.name.lower() == location_name.lower():
            print(f"You are already in {location_name}.")
            return

        if location_name.lower() == "dungeon":
            self.location = DUNGEON
            print("You travel to the dungeon.")
        elif location_name.lower() == "town":
            self.location = TOWN
            print("You travel to the town.")
        else:
            print(f"Unknown location: {location_name}")

    # Enemy turn logic for combat
    def enemy_turn(self):
        if not self.check_if_in_combat():
            return

        damage = self.location.get_current_room().enemies[0].calculate_attack_damage()
        self.player.take_damage(damage)

        print(f"The {self.location.get_current_room().enemies[0].name} attacks you for {damage} damage!")

        if self.player.health <= 0:
            print("You have been defeated! Game Over.")
            exit(0)

    # Command to display help for a specific command
    def cmd_help(self, command):
        if command in COMMANDS:
            info = COMMANDS[command]
            args = " ".join(f"<{arg}>" for arg in info["args"])
            print(f"  {command} {args} - {info['description']}")
        else:
            print("Command not found.")

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
            print()
            handler(*args)
            print()

    # Run the game loop, continuously prompting for user input and handling commands
    def run(self):
        print("Welcome to Sword & Coin!")

        while True:
            user_input = input("> ").strip().lower()

            self.handle_command(user_input)
