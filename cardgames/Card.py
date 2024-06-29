"""

    Card class for the game

"""

class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}"

    def play(self):
        pass


class MonsterCard(Card):
    def __init__(self, name, description, attack, defence):
        super().__init__(name, description)
        self.attack = attack
        self.defence = defence


class SpellCard(Card):
    def __init__(self, name, description, effect):
        super().__init__(name, description)
        self.effect = effect


class TrapCard(Card):
    def __init__(self, name, description, trigger, effect):
        super().__init__(name, description)
        self.trigger = trigger
        self.effect = effect

    def play(self):
        return f"Setting trap {self.name} with trigger: {self.trigger} and effect {self.effect}"

