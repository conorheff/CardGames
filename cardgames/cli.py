"""CLI interface for cardgames project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

from .Deck import Deck

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
    yugi_moto_deck = Deck(duelist='Yugi')
    yugi_moto_deck.construct_dueling_deck()
  
    print(yugi_moto_deck.deck_to_dataframe())
