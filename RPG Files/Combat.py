import random

class Combat:
    @staticmethod
    def basic_attack(attacker, target):
        damage = random.randint(5, 15)
        return f"{attacker} attacks {target} and deals {damage} damage!"

    @staticmethod
    def defend(defender):
        return f"{defender} defends against the incoming attack!"

    @staticmethod
    def flee(fugitive):
        return f"{fugitive} flees from the battle!"
