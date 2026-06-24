COMMANDS = {
    "help": {
        "description": "Display help for a specific command",
        "args": ["command"],
        "handler": "cmd_help"
    },
    "stats": {
        "description": "Display your stats",
        "args": [],
        "handler": "cmd_stats"
    },
    "location": {
        "description": "Display your current location",
        "args": [],
        "handler": "cmd_location"
    },
    "quit": {
        "description": "Quit the game",
        "args": [],
        "handler": "cmd_quit"
    }
}