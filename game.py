from commands import *
from dungeon import Dungeon
from enemy import Enemy
from game_data import GameData
from location import Location
from player import Player

class Game:
    def __init__(self):
        self.data = GameData()
        self.player = Player("Hero")
        self.location = self.create_location("goblin_cave")

    def create_enemy(self, enemy_name):
        enemy_data = self.data.enemies.get(enemy_name)
        if enemy_data:
            return Enemy(
                name=enemy_data["name"],
                health=enemy_data["health"],
                attack=enemy_data["attack"],
                xp_reward=enemy_data["xp_reward"],
                gold_reward=enemy_data["gold_reward"]
            )
        else:
            print(f"Enemy '{enemy_name}' not found.")
            return None
        
    def create_location(self, location_name):
        location_data = self.data.locations.get(location_name)
        if location_data:
            if location_data["type"] == "Dungeon":
                return Dungeon(
                    name=location_data["name"],
                    description=location_data["description"],
                    difficulty=location_data["difficulty"]
                )
            else:
                return Location(
                    name=location_data["name"],
                    description=location_data["description"]
                )
        else:
            print(f"Location '{location_name}' not found.")
            return None

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

        room = self.location.get_current_room()
        enemy = room.enemies[0]

        damage = self.player.calculate_attack_damage()
        enemy.take_damage(damage)
        print(f"You attack the {enemy.name} for {damage} damage!")

        if enemy.health <= 0:
            print(f"You have defeated the {enemy.name}!")
            self.player.gain_xp(enemy.xp_reward)
            self.player.gain_gold(enemy.gold_reward)
            room.enemies.pop(0)
            return

        self.enemy_turn()

    # Command to flee from an enemy
    def cmd_flee(self):
        if not self.check_if_in_combat():
            print("You are not in combat.")
            return

        room = self.location.get_current_room()
        enemy = room.enemies[0]

        print(f"You flee from the {enemy.name}!")

        room.enemies.pop(0)

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

        room = self.location.get_current_room()
        enemy = room.enemies[0]

        print(
            f"{enemy.name} "
            f"(HP: {enemy.health}/{enemy.max_health})"
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
                self.location = self.create_location("town")
                print("You leave the dungeon and return to town.")
        else:
            print("You are not in a dungeon.")

    # Travel command to move between locations
    def cmd_travel(self, location_name):
        self.location = self.create_location(location_name)
        if self.location:
            print(f"You travel to {self.location.name}.")
        else:
            print("Unknown location.")

    # Enemy turn logic for combat
    def enemy_turn(self):
        if not self.check_if_in_combat():
            return
        
        room = self.location.get_current_room()
        enemy = room.enemies[0]

        damage = enemy.calculate_attack_damage()
        self.player.take_damage(damage)

        print(f"The {enemy.name} attacks you for {damage} damage!")

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
