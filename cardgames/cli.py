"""CLI interface for cardgames project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

from .duelist import Duelist
from .deck import Deck
from .game import Game

def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m cardgames` and `$ cardgames `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """

    dummy_deck = Deck()
    dummy_deck.construct_dueling_deck()

    yugi = Duelist(name='Yugi', deck=dummy_deck)
    kaiba = Duelist(name='Kaiba',deck=dummy_deck)


    duel = Game(player_1=yugi, player_2=kaiba)
    duel.turn()

