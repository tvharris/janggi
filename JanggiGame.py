# Author: Travis Harris
# Date: 2/26/2021
# Description: Implement the board game Janggi, with a class (JanggiGame) for
# playing the game.

class JanggiGame:
    """
    An implementation of the board game Janggi.

    Data members: See __init__
    Methods: get_game_state, is_in_check, make_move
    """

    def __init__(self):
        """
        Private data members:
            game_state:
            in_check:
        """


    def get_game_state(self):
        """Returns game state which may be 'UNFINISHED', 'RED_WON', or
        BLUE_WON'."""


    def is_in_check(self, player):
        """Returns True of the player ('red' or 'blue') is in check, otherwise
        False."""


    def make_move(self, from, to):
        """
        Moves a piece from its current position to an allowed position, and may
        capture an opposing piece.
        Parameters: from and to are strings representing positions (e.g., 'b3')
        Returns: True if the move is allowed, otherwise False.
        """