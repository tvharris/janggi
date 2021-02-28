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
        self._board = {'a1': 'rch1', 'b1': '----', 'c1': 'rho1', 'd1': 'rgu1', 'e1': '----',
                       'f1': 'rgu2', 'g1': 'rel2', 'h1': 'rho2', 'i1': 'rch1',
                       'a2': '----', 'b2': '----', 'c2': '----', 'd2': '----', 'e2': 'rge1',
                       'f2': '----', 'g2': '----', 'h2': '----', 'i2': '----',
                       'a3': '----', 'b3': 'rca1', 'c3': '----', 'd3': '----', 'e3': '----',
                       'f3': '----', 'g3': '----', 'h3': 'rca2', 'i3': '----',
                       'a4': 'rso1', 'b4': '----', 'c4': 'rso2', 'd4': '----', 'e4': 'rso3',
                       'f4': '----', 'g4': 'rso4', 'h4': '----', 'i4': 'rso5',
                       'a5': '----', 'b5': '----', 'c5': '----', 'd5': '----', 'e5': '----',
                       'f5': '----', 'g5': '----', 'h5': '----', 'i5': '----',
                       'a6': '----', 'b6': '----', 'c6': '----', 'd6': '----', 'e6': '----',
                       'f6': '----', 'g6': '----', 'h6': '----', 'i6': '----',
                       'a7': 'bso1', 'b7': '----', 'c7': 'bso2', 'd7': '----', 'e7': 'bso3',
                       'f7': '----', 'g7': 'bso4', 'h7': '----', 'i7': 'bso5',
                       'a8': '----', 'b8': 'bca1', 'c8': '----', 'd8': '----', 'e8': '----',
                       'f8': '----', 'g8': '----', 'h8': 'bca2', 'i8': '----',
                       'a9': '----', 'b9': '----', 'c9': '----', 'd9': '----', 'e9': 'bge1',
                       'f9': '----', 'g9': '----', 'h9': '----', 'i9': '----',
                       'a10': 'bch1', 'b10': 'bel1', 'c10': 'bho1', 'd10': 'bgu1', 'e10': '----',
                       'f10': 'bgu2', 'g10': 'bel2', 'h10': 'bho2', 'i10': 'bch2'}

    def get_board(self):
        """Returns the board dictionary."""
        return self._board

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

        # testing printing without pieces
        #print('     a    b    c    d    e    f    g    h    i\n'
        #      '1    +----+----+----+----+----+----+----+----+\n'
        #      '     |    |    |    |  \ | /  |    |    |    |\n'
        #      '2    +----+----+----+----+----+----+----+----+\n'
        #      '     |    |    |    |  / | \  |    |    |    |\n'
        #      '10   +----+----+----+----+----+----+----+----+')

        board = self.get_board()

        # print board with pieces
        print('     a    b    c    d    e    f    g    h    i\n'
              '1  %s %s %s %s %s %s %s %s %s \n'
              '2  %s %s %s %s %s %s %s %s %s \n'
              '3  %s %s %s %s %s %s %s %s %s \n'
              '4  %s %s %s %s %s %s %s %s %s \n'
              '5  %s %s %s %s %s %s %s %s %s \n'
              '6  %s %s %s %s %s %s %s %s %s \n'
              '7  %s %s %s %s %s %s %s %s %s \n'
              '8  %s %s %s %s %s %s %s %s %s \n'
              '9  %s %s %s %s %s %s %s %s %s \n'
              '10 %s %s %s %s %s %s %s %s %s \n'

              %(board.get('a1'), board.get('b1'), board.get('c1'), board.get('d1'), board.get('e1'),
                board.get('f1'), board.get('g1'), board.get('h1'), board.get('i1'),
                board.get('a2'), board.get('b2'), board.get('c2'), board.get('d2'), board.get('e2'),
                board.get('f2'), board.get('g2'), board.get('h2'), board.get('i2'),
                board.get('a3'), board.get('b3'), board.get('c3'), board.get('d3'), board.get('e3'),
                board.get('f3'), board.get('g3'), board.get('h3'), board.get('i3'),
                board.get('a4'), board.get('b4'), board.get('c4'), board.get('d4'), board.get('e4'),
                board.get('f4'), board.get('g4'), board.get('h4'), board.get('i4'),
                board.get('a5'), board.get('b5'), board.get('c5'), board.get('d5'), board.get('e5'),
                board.get('f5'), board.get('g5'), board.get('h5'), board.get('i5'),
                board.get('a6'), board.get('b6'), board.get('c6'), board.get('d6'), board.get('e6'),
                board.get('f6'), board.get('g6'), board.get('h6'), board.get('i6'),
                board.get('a7'), board.get('b7'), board.get('c7'), board.get('d7'), board.get('e7'),
                board.get('f7'), board.get('g7'), board.get('h7'), board.get('i7'),
                board.get('a8'), board.get('b8'), board.get('c8'), board.get('d8'), board.get('e8'),
                board.get('f8'), board.get('g8'), board.get('h8'), board.get('i8'),
                board.get('a9'), board.get('b9'), board.get('c9'), board.get('d9'), board.get('e9'),
                board.get('f9'), board.get('g9'), board.get('h9'), board.get('i9'),
                board.get('a10'), board.get('b10'), board.get('c10'), board.get('d10'), board.get('e10'),
                board.get('f10'), board.get('g10'), board.get('h10'), board.get('i10')
                ))

def main():
    game = JanggiGame()
    game.display_board()

if __name__ == '__main__':
    main()
