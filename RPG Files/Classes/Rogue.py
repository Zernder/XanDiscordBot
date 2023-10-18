class Rogue:
    def __init__(self):
        # Define base attributes for the Rogue class
        self.class_name = "rogue"
        self.level = 1
        self.experience = 0
        self.base_stats = {
            "health": 75,
            "attack": 10,
            "defense": 8,
            "agility": 15,
            "dexterity": 15,
            "stealth": 12
        }
        self.abilities = {}  # Dictionary to store abilities and their descriptions

    # Rest of the class remains the same...


    # Rest of the class remains the same...

        self.abilities = {}  # Dictionary to store abilities and their descriptions

    def level_up(self):
        # Implement leveling up logic here
        # Increase attributes, unlock abilities, etc.
        self.level += 1
        self.experience = 0  # Reset experience to 0 at each level up
        # Example: Increase agility and dexterity at each level up
        self.base_stats["agility"] += 3
        self.base_stats["dexterity"] += 3

        # Define abilities and their levels here
        abilities = {
            "Backstab": 5,
            "Evasion": 10,
            "Stealthy Approach": 15,
            "Precision Strike": 20,
            "Shadowstep": 25,
            "Poisoned Blades": 30,
            "Smoke Bomb": 35,
            "Assassinate": 40,
            "Disarm Traps": 45,
            "Acrobatic Maneuvers": 50,
            "Blinding Powder": 55,
            "Camouflage": 60,
            "Sprint": 65,
            "Ambush": 70,
            "Dirty Tricks": 75,
            "Vanish": 80,
            "Lethal Strike": 85,
            "Infiltration": 90,
            "Master of Shadows": 95,
            "Death's Embrace": 100,
        }

        # Add unlocked abilities to the character's abilities dictionary
        for ability, level_required in abilities.items():
            if self.level >= level_required:
                self.abilities[ability] = f"Execute a cunning {ability.lower()} maneuver."

    def create_character(self, character_name):
        # Create a new character of the Rogue class
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
rogue = Rogue()
character = rogue.create_character("Sly Rogue")
print(character)
