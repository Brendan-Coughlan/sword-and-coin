COMMANDS = {
    "help": {
        "description": "Display available commands",
        "args": [],
        "handler": "cmd_help"
    },
    "look": {
        "description": "Look around the current location",
        "args": [],
        "handler": "cmd_look"
    },
    "inventory": {
        "description": "Display your inventory",
        "args": [],
        "handler": "cmd_inventory"
    },
    "attack": {
        "description": "Attack an enemy",
        "args": ["target"],
        "handler": "cmd_attack"
    },
    "rest": {
        "description": "Rest and recover health",
        "args": [],
        "handler": "cmd_rest"
    }
}