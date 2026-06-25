class Enemy:
    def __init__(self, name, hp, strength, defense, xp_reward, gold_reward):
        self.name = name
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.hp = hp
        self.strength = strength
        self.defense = defense

    def display_stats(self):
        print(f"{self.name}'s Stats:")
        print(f"  HP: {self.hp}")
        print(f"  Strength: {self.strength}")
        print(f"  Defense: {self.defense}")

    def calculate_attack_damage(self):
        base_damage = self.strength
        
        return base_damage

    def take_damage(self, amount):
        damage_taken = amount
        self.hp -= damage_taken

        if self.hp <= 0:
            print(f"The {self.name} has been defeated!")