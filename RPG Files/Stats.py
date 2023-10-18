# stats.py

class Stats:
    def __init__(self, base_stats):
        self.base_stats = base_stats
        self.stats = base_stats.copy()
        self.level = 1
        self.experience = 0
        self.attribute_points = 0  # Track available attribute points

    def level_up(self):
        # Implement leveling up logic here
        # Increase attributes, unlock abilities, etc.
        self.level += 1
        self.attribute_points += 2  # Gain 2 attribute points on level up
        # Example: Increase health and attack at each level up
        self.stats["health"] += 10
        self.stats["attack"] += 5

    def allocate_experience(self, amount):
        # Allocate experience points and potentially trigger level-up
        self.experience += amount
        # Example: Check if the character should level up
        if self.experience >= self.level * 100:  # Adjust the experience needed as needed
            self.level_up()

    def increase_attribute(self, attribute_name):
        # Increase a chosen attribute by 1 point
        if self.attribute_points > 0 and attribute_name in self.stats:
            self.stats[attribute_name] += 1
            self.attribute_points -= 1
