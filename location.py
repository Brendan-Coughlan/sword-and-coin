class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display(self):
        print(f"You are at {self.name}.")
        print(self.description)