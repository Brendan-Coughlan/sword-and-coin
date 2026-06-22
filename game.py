from commands import *
from player import Player

class Game:
    def __init__(self):
        self.player = Player(name="Hero", starting_gold=50)

    def cmd_quit(self):
        print("Thanks for playing!")
        exit(0)

    def cmd_help(self, command):
        if command in COMMANDS:
            info = COMMANDS[command]
            args = " ".join(f"<{arg}>" for arg in info["args"])
            print(f"  {command} {args} - {info['description']}")
        else:
            print("Command not found.")

    def cmd_inventory(self):
        self.player.display_stats()

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

    def run(self):
        print("Welcome to Sword & Coin!")

        while True:
            user_input = input("> ").strip().lower()

            self.handle_command(user_input)
