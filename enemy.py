class Enemy:
    def __init__(self, name, hp, strength, defense, xp_reward, gold_reward):
        self.name = name
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward

        self.stats = {
            "hp": hp,
            "strength": strength,
            "defense": defense
        }

    def display_stats(self):
        print(f"{self.name}'s Stats:")
        for stat, value in self.stats.items():
            print(f"  {stat.capitalize()}: {value}")