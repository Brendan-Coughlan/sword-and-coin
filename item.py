class Item:
    def __init__(self, id, name, description, value):
        self.id = id
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.description} (Value: {self.value} gold)"