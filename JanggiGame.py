# Author: Travis Harris
# Date: 2/26/2021
# Description: Implement the board game Janggi, with a class (JanggiGame) for
# playing the game.

class JanggiGame:
    """
    An implementation of the board game Janggi.

    Data members: See __init__
    Methods: get_game_state, is_in_check, make_move, display_board
    """

    def __init__(self):
        """
        Private data members:
            game_state:
            in_check:
            board:
        """
        self._board = {'a1': 'rch1', 'b1': 'rel1', 'c1': 'rho1', 'd1': 'rgu1', 'e1': 'x',
                       'f1': 'rgu2', 'g1': 'rel2', 'h1': 'rho2', 'i1': 'rch1',
                       'a2': 'x', 'b2': 'x', 'c2': 'x', 'd2': 'x', 'e2': 'rge',
                       'f2': 'x', 'g2': 'x', 'h2': 'x', 'i2': 'x',
                       'a3': 'x', 'b3': 'rca1', 'c3': 'x', 'd3': 'x', 'e3': 'x',
                       'f3': 'x', 'g3': 'x', 'h3': 'rca2', 'i3': 'x',
                       'a4': 'rso1', 'b4': 'x', 'c4': 'rso2', 'd4': 'x', 'e4': 'rso3',
                       'f4': 'x', 'g4': 'rso4', 'h4': 'x', 'i4': 'rso5',
                       'a5': 'x', 'b5': 'x', 'c5': 'x', 'd5': 'x', 'e5': 'x',
                       'f5': 'x', 'g5': 'x', 'h5': 'x', 'i5': 'x',
                       'a6': 'x', 'b6': 'x', 'c6': 'x', 'd6': 'x', 'e6': 'x',
                       'f6': 'x', 'g6': 'x', 'h6': 'x', 'i6': 'x',
                       'a7': 'bso1', 'b7': 'x', 'c7': 'bso2', 'd7': 'x', 'e7': 'bso3',
                       'f7': 'x', 'g7': 'bso4', 'h7': 'x', 'i7': 'bso5',
                       'a8': 'x', 'b8': 'bca1', 'c8': 'x', 'd8': 'x', 'e8': 'x',
                       'f8': 'x', 'g8': 'x', 'h8': 'bca2', 'i8': 'x',
                       'a9': 'x', 'b9': 'x', 'c9': 'x', 'd9': 'x', 'e9': 'bge',
                       'f9': 'x', 'g9': 'x', 'h9': 'x', 'i9': 'x',
                       'a10': 'bch1', 'b10': 'bel1', 'c10': 'bho1', 'd10': 'bgu1', 'e10': 'x',
                       'f10': 'bgu2', 'g10': 'bel2', 'h10': 'bho2', 'i10': 'bch2',

    def get_game_state(self):
        """Returns game state which may be 'UNFINISHED', 'RED_WON', or
        BLUE_WON'."""


    def is_in_check(self, player):
        """Returns True of the player ('red' or 'blue') is in check, otherwise
        False."""


    def make_move(self, from_pos, to_pos):
        """
        Moves a piece from its current position to an allowed position, and may
        capture an opposing piece.
        Parameters: from_pos and to_pos are strings representing positions
            (e.g., 'b3')
        Returns: True if the move is allowed, otherwise False.
        """

    def display_board(self):
        """Displays the board with the pieces in their current positions."""
        print('     a    b    c    d    e    f    g    h    i\n'
              '1    +----+----+----+----+----+----+----+----+\n'
              '     |    |    |    |  \ | /  |    |    |    |\n'
              '2    +----+----+----+----+----+----+----+----+\n'
              '     |    |    |    |  / | \  |    |    |    |\n'
              '10   +----+----+----+----+----+----+----+----+')

def main():
    game = JanggiGame()
    game.display_board()

if __name__ == '__main__':
    main()
