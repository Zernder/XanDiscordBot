class Monk:
    def __init__(self):
        # Define base attributes for the Monk class
        self.class_name = "monk"
        self.level = 1
        self.experience = 0
        self.base_stats = {
            "health": 80,
            "attack": 12,
            "defense": 8,
            "agility": 15,
            "dexterity": 12,
            "spirituality": 15
        }
        self.abilities = {}  # Dictionary to store abilities and their descriptions

    # Rest of the class remains the same...


    def level_up(self):
        # Implement leveling up logic here
        # Increase attributes, unlock abilities, etc.
        self.level += 1
        self.experience = 0  # Reset experience to 0 at each level up
        # Example: Increase agility and dexterity at each level up
        self.base_stats["agility"] += 3
        self.base_stats["dexterity"] += 2

        # Define abilities and their levels here
        abilities = {
            "Martial Strike": 5,
            "Evasion": 10,
            "Inner Peace": 15,
            "Chi Burst": 20,
            "Whirlwind Kick": 25,
            "Ki Focus": 30,
            "Serenity": 35,
            "Dragon Palm": 40,
            "Mystic Step": 45,
            "Tiger Claw": 50,
            "Blinding Speed": 55,
            "Harmony of Body": 60,
            "Thunderous Roar": 65,
            "Cyclone Strike": 70,
            "Zen Meditation": 75,
            "Dragon Dance": 80,
            "Tornado Kick": 85,
            "Enlightenment": 90,
            "Divine Presence": 95,
            "Ascension": 100,
        }

        # Add unlocked abilities to the character's abilities dictionary
        for ability, level_required in abilities.items():
            if self.level >= level_required:
                self.abilities[ability] = f"Unleash a powerful {ability.lower()} attack."

    def create_character(self, character_name):
        # Create a new character of the Monk class
        # Initialize character attributes and return the character dictionary
        character = {
            "name": character_name,
            "class": self.class_name,
            "level": self.level,
            "experience": self.experience,
            **self.base_stats  # Include base stats in the character
        }
        return character

# Example usage:
monk = Monk()
character = monk.create_character("Zen Master")
print(character)
