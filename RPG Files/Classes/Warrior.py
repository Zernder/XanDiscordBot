class Warrior:
    def __init__(self):
        # Define base attributes for the Warrior class
        self.class_name = "warrior"
        self.level = 1
        self.experience = 0
        self.base_stats = {
            "health": 100,
            "attack": 10,
            "defense": 10,
            "strength": 15,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }
        self.abilities = {}  # Dictionary to store abilities and their descriptions

    def level_up(self):
        # Implement leveling up logic here
        # Increase attributes, unlock abilities, etc.
        self.level += 1
        self.experience = 0  # Reset experience to 0 at each level up
        # Example: Increase health and attack at each level up
        self.base_stats["health"] += 10
        self.base_stats["attack"] += 5

        # Define abilities and their levels here
        abilities = {
            "Slash": 5,
            "Block": 10,
            "Cleave": 15,
            "Rage": 20,
            "Counterattack": 25,
            "Whirlwind": 30,
            "Berserk": 35,
            "War Cry": 40,
            "Execute": 45,
            "Mighty Blow": 50,
            "Tough Skin": 55,
            "Resilience": 60,
            "Adrenaline Rush": 65,
            "Brutal Strike": 70,
            "Armored Stance": 75,
            "Frenzy": 80,
            "Retaliation": 85,
            "Thunder Strike": 90,
            "Master of Blades": 95,
            "Warlord's Wrath": 100,
        }

        # Add unlocked abilities to the character's abilities dictionary
        for ability, level_required in abilities.items():
            if self.level >= level_required:
                self.abilities[ability] = f"Unleash a powerful {ability.lower()} attack."

    def create_character(self, character_name):
        # Create a new character of the Warrior class
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
warrior = Warrior()
character = warrior.create_character("Brave Kevin")
print(character)
