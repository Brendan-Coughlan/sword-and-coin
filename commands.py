COMMANDS = {
    "help": {
        "description": "Display help for a specific command",
        "args": ["command"],
        "handler": "cmd_help"
    },
    "inventory": {
        "description": "Display your inventory",
        "args": [],
        "handler": "cmd_inventory"
    },
    "quit": {
        "description": "Quit the game",
        "args": [],
        "handler": "cmd_quit"
    }
}