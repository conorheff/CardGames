"""
cardgames base module.

Main classes and objects will be placed here

Main classes

    Card (child classes monster, spell, trap)
    Game (turns, life points)
    Simulator (simulates a game between two players)
    Deck (Contains cards)

Module works by simulating a simple game of classic YuGiOh between two players

Firstly, a deck is constructed at random for both players (subject to constraints, ie 40 cards etc)

Secondly, a game is constructed where each player makes moves in turn. Game ends when either LP = 0 or card_count = 0

Finally, data about the game is saved to a db

"""


