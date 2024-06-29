"""

    Game class

    Contains info such as turns, players, phase, LP

"""

class Game:

    def __init__(self, player_1=None, player_2=None):
        self.player_1 = player_1
        self.player_2 = player_2

        self.player_1_monster_zone = []
        self.player_1_spell_trap_zone = []
        self.player_1_graveyard = []

        self.player_2_monster_zone = []
        self.player_2_spell_trap_zone = []
        self.player_2_graveyard = []

        self.player_turn = "player_1" # TODO : implement coin toss

    def turn(self):
        draw(self.player_1)
        


def draw(player):

    player.draw_card()
    player.current_hand()