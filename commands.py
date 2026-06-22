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
    "quit": {
        "description": "Quit the game",
        "args": [],
        "handler": "cmd_quit"
    }
}