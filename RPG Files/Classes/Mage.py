class Mage:
    def __init__(self):
        # Define base attributes for the Mage class
        self.class_name = "mage"
        self.level = 1
        self.experience = 0
        self.base_stats = {
            "health": 70,
            "attack": 8,
            "defense": 5,
            "magic_attack": 15,
            "magic_defense": 10,
            "intelligence": 15
        }
        self.abilities = {}  # Dictionary to store abilities and their descriptions

    # Rest of the class remains the same...

        self.abilities = {}  # Dictionary to store abilities and their descriptions

    def level_up(self):
        # Implement leveling up logic here
        # Increase attributes, unlock abilities, etc.
        self.level += 1
        self.experience = 0  # Reset experience to 0 at each level up
        # Example: Increase magic_attack and magic_defense at each level up
        self.base_stats["magic_attack"] += 5
        self.base_stats["magic_defense"] += 3

        # Define abilities and their levels here
        abilities = {
            "Fireball": 5,
            "Frost Nova": 10,
            "Arcane Shield": 15,
            "Lightning Bolt": 20,
            "Teleport": 25,
            "Blizzard": 30,
            "Summon Familiar": 35,
            "Chain Lightning": 40,
            "Invisibility": 45,
            "Meteor Shower": 50,
            "Time Warp": 55,
            "Mind Control": 60,
            "Polymorph": 65,
            "Energy Drain": 70,
            "Arcane Explosion": 75,
            "Elemental Mastery": 80,
            "Tornado": 85,
            "Resurrection": 90,
            "Ethereal Form": 95,
            "Apocalypse": 100,
        }

        # Add unlocked abilities to the character's abilities dictionary
        for ability, level_required in abilities.items():
            if self.level >= level_required:
                self.abilities[ability] = f"Cast a powerful {ability.lower()} spell."

    def create_character(self, character_name):
        # Create a new character of the Mage class
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
mage = Mage()
character = mage.create_character("Mystic Mage")
print(character)
