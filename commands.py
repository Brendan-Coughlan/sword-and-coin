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
    },
    "forward": {
        "description": "Move forward in the dungeon",
        "args": [],
        "handler": "cmd_forward"
    },
    "leave": {
        "description": "Leave the dungeon and return to the main area",
        "args": [],
        "handler": "cmd_leave"
    },
    "travel": {
        "description": "Travel to a different location",
        "args": ["location_name"],
        "handler": "cmd_travel"
    },
    "attack": {
        "description": "Attack an enemy",
        "args": [],
        "handler": "cmd_attack"
    },
    "flee": {
        "description": "Flee from an enemy",
        "args": [],
        "handler": "cmd_flee"
    },
    "enemy": {
        "description": "Display the current enemy's stats",
        "args": [],
        "handler": "cmd_enemy"
    }
}