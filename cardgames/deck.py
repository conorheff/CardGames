"""

    Class for constructing a player's deck

    For now I will use a dummy deck constructer
    with basic effects and random names and atk/def

    Will then use a web scraper to create a db of possible cards

"""

import numpy as np
import random
import pandas as pd
from .card import MonsterCard, SpellCard, TrapCard

class Deck:
    def __init__(self, card_count=40, monster_count=20, spell_count=10, trap_count=10):
        self.card_count = card_count
        self.monster_count = monster_count
        self.spell_count = spell_count
        self.trap_count = trap_count
        self.monsters = []
        self.spells = []
        self.traps = []
        self.deck_list = []

        if monster_count+spell_count+trap_count != card_count :
            raise Exception("Deck size must equal number of cards!")

    def construct_dueling_deck(self):
        max_atk = 3000
        min_atk = 100
        max_def = 2500
        min_def = 1000

        for i in range(0, self.monster_count):
            self.monsters.append(create_monster(min_atk, max_atk, min_def, max_def))

        for i in range(0, self.spell_count):
            self.spells.append(create_spell())

        for i in range(0, self.trap_count):
            self.traps.append(create_trap())

        self.deck_list = self.monsters + self.spells + self.traps
        random.shuffle(self.deck_list)

    def deck_to_dataframe(self) -> pd.DataFrame:
        names = [None]*self.card_count
        attack = [None]*self.card_count
        defence = [None]*self.card_count
        types = [None]*self.card_count

        for i in range(self.card_count):
            names[i] = self.deck_list[i].name
            if isinstance(self.deck_list[i], MonsterCard) :
                attack[i] = self.deck_list[i].attack[0]
                defence[i] = self.deck_list[i].defence[0]
                types[i] = 'Monster'
            elif isinstance(self.deck_list[i], SpellCard) :
                types[i] = 'Spell'
            elif isinstance(self.deck_list[i], TrapCard) :
                types[i] = 'Trap'
            else:
                raise Exception('Error - Unknown Card type!')

        deck_dict = {
            "Name": names,
            "ATK" : attack,
            "DEF" : defence,
            "Type": types
        }
        return pd.DataFrame(deck_dict)


def generate_random_numbers(min_val, max_val, size):
    # Ensure min_val and max_val are multiples of 100
    min_val = (min_val + 99) // 100 * 100  # Round up to the nearest 100
    max_val = max_val // 100 * 100  # Round down to the nearest 100

    if min_val > max_val:
        raise ValueError("min_val must be less than or equal to max_val after rounding to nearest 100")

    # Generate random numbers in the range [min_val // 100, max_val // 100] and multiply by 100
    random_numbers = np.random.randint(min_val // 100, (max_val // 100) + 1, size) * 100
    return random_numbers

def create_monster(min_atk, max_atk, min_def, max_def):

    ATK = generate_random_numbers(min_atk, max_atk, 1)
    DEF = generate_random_numbers(min_def, max_def, 1)

    NAME = 'Monster'
    DESCRIPTION = 'This monster is powerfull'

    return MonsterCard(NAME, DESCRIPTION, ATK, DEF)

def create_spell():

    NAME = 'Pot of Greed'
    DESCRIPTION = 'Player draws 2 cards'
    EFFECT = 'Player Draw 2 Card'

    return SpellCard(NAME, DESCRIPTION, EFFECT)

def create_trap():

    NAME = 'Destroy'
    DESCRIPTION = 'Destroys your opponent monster upon attack'

    TRIGGER = 'Opponent Monster Attack'
    EFFECT = 'Destroy Opponent Monster'

    return TrapCard(NAME, DESCRIPTION, TRIGGER, EFFECT)
