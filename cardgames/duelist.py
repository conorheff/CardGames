"""

    Represents a player in the game

"""

from .deck import Deck

class Duelist:

    def __init__(self, name, LP=2000, deck=None, status="PLAYING"):
        self.name = name
        self.LP = LP
        self.deck = deck
        self.status = status
        self.hand = deck.deck_list[0:5]
        del self.deck.deck_list[0:5]

    def __str__(self):
        return f"This is {self.name}'s current hand : {self.hand}"

    def current_hand(self):
        print(f"\n========{self.name}'s Hand========\n")
        for i in range(len(self.hand)):
            print(self.hand[i])

    def read_deck(self):
        print(self.deck.deck_to_dataframe())

    def damage(self, damage):
        self.LP = self.LP - damage
        if self.LP <= 0:
            self.status = "LOSE"

    def draw_card(self):

        assert self.deck.deck_list 

        self.hand.append(self.deck.deck_list[0])
        del self.deck.deck_list[0]

        if not self.deck.deck_list :
            self.status = "LOSE"

