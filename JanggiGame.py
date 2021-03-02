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
        Creates a JanggiGame.
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


class Player:
    """
    Represents a Janggi player.

    Data members: See __init__
    Methods: get_color, get_pieces, add_piece, remove_piece,
             set_allowed_destinations, _init_pieces
    """
    def __init__(self, color):
        """
        Creates a Janggi Player and calls _init_pieces to initialize the Piece
        objects and add them to the player's pieces set

        Private data members:
            allowed_destinations: set of destinations that the player's pieces
                can legally reach given the current state of the board
            color: (str) 'blue' or 'red'
            pieces: set of Piece objects
        """
        self._allowed_destinations = set()
        self._color = color
        self._pieces = set()
        self._init_pieces()

    def get_color(self):
        """Returns the Player's color"""
        return self._color

    def get_pieces(self):
        """Returns the Player's set of Piece objects"""
        return self._pieces

    def add_piece(self, piece):
        """Takes a Piece object and adds it to the Player's pieces set"""
        pieces = self.get_pieces()
        pieces.add(piece)

    def remove_piece(self, piece):
        """Takes a Piece object and removes it from the Player's pieces set"""
        pieces = self.get_pieces()
        pieces.remove(piece)

    def set_allowed_destinations(self, allowed_destinations):
        """Sets the Player's allowed_destinations set to the set parameter"""
        self._allowed_destinations = allowed_destinations

    def _init_pieces(self):
        """Initializes the Player's pieces in their starting positions and adds
        them to the pieces set"""
        color = self.get_color()
        if color == 'blue':
            pieces = {Soldier('bso1', 'a7'), Soldier('bso2', 'c7'),
                      Soldier('bso3', 'e7'), Soldier('bso4', 'g7'),
                      Soldier('bso5', 'i7'), Cannon('bca1', 'b8'),
                      Cannon('bca2', 'h8'), General('bge1', 'e9'),
                      Chariot('bch1', 'a10'), Elephant('bel1', 'b10'),
                      Horse('bho1', 'c10'), Guard('bgu1', 'd10'),
                      Guard('bgu2', 'f10'), Elephant('bel2', 'g10'),
                      Horse('bho2', 'h10'), Chariot('bch2', 'i10')}
        else:
            pieces = {Soldier('rso1', 'a4'), Soldier('rso2', 'c4'),
                      Soldier('rso3', 'e4'), Soldier('rso4', 'g4'),
                      Soldier('rso5', 'i4'), Cannon('rca1', 'b3'),
                      Cannon('rca2', 'h3'), General('rge1', 'e2'),
                      Chariot('rch1', 'a1'), Elephant('rel1', 'b1'),
                      Horse('rho1', 'c1'), Guard('rgu1', 'd1'),
                      Guard('rgu2', 'f1'), Elephant('rel2', 'g1'),
                      Horse('rho2', 'h1'), Chariot('rch2', 'i1')}

        self._pieces = pieces


class Piece:
    """
    Represents a Janggi piece.

    Data members: See __init__
    Methods: get_position, set_position, get_hyp_moves, get piece_id
        position_u, position_d, position_l, position_r,
        position_ul, position_ur, position_dl, position_dr
    """
    def __init__(self, piece_id, position):
        """
        Creates a Janggi Piece.
        Private data members:
            piece_id: string with format 'cxx#' where
                c is the color 'r' or 'b',
                xx is the piece: cannon = 'ca', chariot = 'ch', elephant = 'el',
                                 general = 'ge', guard = 'gu', horse = 'ho',
                                 soldier = 'so'
                # is a number 1-5, for distinguishing between the same type
                    of piece
            position: position on the board as 2 or 3-char string, with a letter
                for the column, and number for the row (e.g., 'a1').
            hyp_moves: dictionary of hypothetical moves the piece can make with
                destination positions as keys and lists of intermediate
                positions that must be passed en route as values
                ({dest: [interm1, interm2]}). Hypothetical moves do not consider
                positions of other pieces.
        """
        self._piece_id = piece_id
        self._position = position
        self._hyp_moves = {}

    def get_piece_id(self):
        """Returns the piece_id"""
        return self._piece_id

    def get_position(self):
        """Returns the position on the board as 2 or 3-char string, with a letter
        for the column, and number for the row (e.g., 'a1')"""
        return self._position

    def set_position(self, position):
        """Sets the position on the board to the specified 2 or 3-char string,
        with a letter for the column, and number for the row (e.g., 'a1')"""
        self._position = position

    def get_hyp_moves(self):
        """Returns the hyp_moves dictionary."""
        return self._hyp_moves

    def position_u(self, position = None):
        """Returns the position directly above the piece's current position on
        the board as a 2 or 3-char string. If the piece is already at the top of
        the board, returns None. Optionally takes a starting position."""
        if position is None:
            position = self.get_position()
        if position[1:] == '1':  # already at top of board
            return None

        position_u = position[0] + str(int(position[1:]) - 1)  # decrement row
        return position_u

    def position_d(self, position = None):
        """Returns the position directly below the piece's current position on
        the board as a 2 or 3-char string. If the piece is already at the bottom
        of the board, returns None. Optionally takes a starting position."""
        if position is None:
            position = self.get_position()
        if position[1:] == '10':  # already at bottom of board
            return None

        position_d = position[0] + str(int(position[1:]) + 1)  # increment row
        return position_d

    def position_l(self, position = None):
        """Returns the position directly to the left of the piece's current
        position on the board as a 2 or 3-char string. If the piece is already
        at the far left on the board, returns None. Optionally takes a starting
        position."""
        if position is None:
            position = self.get_position()
        if position[0] == 'a':
            return None

        position_l = chr(ord(position[0]) - 1) + position[1:]  # decrement letter
        return position_l

    def position_r(self, position = None):
        """Returns the position directly to the right of the piece's current
        position on the board as a 2 or 3-char string. If the piece is already
        at the far right on the board, returns None. Optionally takes a starting
        position."""
        if position is None:
            position = self.get_position()
        if position[0] == 'i':
            return None

        position_r = chr(ord(position[0]) + 1) + position[1:]  # increment letter
        return position_r

    def position_ul(self, position = None):
        """Returns the position diagonally up and left of the current position
        on the board as a 2 or 3-char string. If the piece is already at the far
        left or top of the board, returns None. Optionally takes a starting
        position"""
        if position is None:
            position = self.get_position()
        if position[0] == 'a' or position[1:] == '1':  # already at left or top
            return None

        position_ul = chr(ord(position[0]) - 1) + str(int(position[1:]) - 1)
        return position_ul

    def position_ur(self, position = None):
        """Returns the position diagonally up and left of the current position
        on the board as a 2 or 3-char string. If the piece is already at the far
        right or top of the board, returns None. Optionally takes a starting
        position"""
        if position is None:
            position = self.get_position()
        if position[0] == 'i' or position[1:] == '1':  # already at right or top
            return None

        position_ur = chr(ord(position[0]) + 1) + str(int(position[1:]) - 1)
        return position_ur

    def position_dl(self, position = None):
        """Returns the position diagonally up and left of the current position
        on the board as a 2 or 3-char string. If the piece is already at the far
        left or bottom of the board, returns None. Optionally takes a starting
        position"""
        if position is None:
            position = self.get_position()
        if position[0] == 'a' or position[1:] == '10':  # already at edge
            return None

        position_dl = chr(ord(position[0]) - 1) + str(int(position[1:]) + 1)
        return position_dl

    def position_dr(self, position = None):
        """Returns the position diagonally up and left of the current position
        on the board as a 2 or 3-char string. If the piece is already at the far
        right or bottom of the board, returns None. Optionally takes a starting
        position"""
        if position is None:
            position = self.get_position()
        if position[0] == 'i' or position[1:] == '10':  # already at edge
            return None

        position_dr = chr(ord(position[0]) + 1) + str(int(position[1:]) + 1)
        return position_dr


class Cannon(Piece):
    """
    Represents a cannon, a sub-class of Piece.
    Cannons can move horizontally or vertically any number of positions, but
    they must jump exactly one other piece, which may not be another cannon.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position):
        """
        Creates a Cannon with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cca#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'a1'
        """
        super().__init__(piece_id, position)

    def update_hyp_moves(self):
        """Updates and returns the piece's hypothetical moves dictionary. These
        moves do not consider the locations of other pieces."""
        hyp_moves = {}

        # iterate through all possible destinations, saving them with their
        # corresponding intermediate positions as {dest.: [interm1, interm2, ...]}
        for next_position in [self.position_u, self.position_d,
                              self.position_l, self.position_r]:
            # start at adjacent position because cannon can't move to it
            destination = next_position()
            intermediates = []
            while next_position(destination) is not None:
                # previous destination is intermediate of next destination
                intermediates.append(destination)
                destination = next_position(destination)
                # add destination and its intermediates to dictionary
                hyp_moves[destination] = list(intermediates)

        # cannons can jump diagonally from the corners of the palace
        position = self.get_position()
        if position == 'd1' or position == 'd8':
            next_position = self.position_dr
        if position == 'f1' or position == 'f8':
            next_position = self.position_dl
        if position == 'd3' or position == 'd10':
            next_position = self.position_ur
        if position == 'f3' or position == 'f10':
            next_position = self.position_ul

        intermediate = next_position()  # center of a palace
        destination = next_position(intermediate)

        hyp_moves[destination] = [intermediate]

        self._hyp_moves = hyp_moves
        return hyp_moves


class Chariot(Piece):
    """
    Represents a chariot, a sub-class of Piece.
    Chariots can move horizontally or vertically any number of positions, but
    they may not jump over another piece.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position):
        """
        Creates a Chariot with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cch#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'a1'
        """
        super().__init__(piece_id, position)

    def update_hyp_moves(self):
        """Updates and returns the piece's hypothetical moves dictionary. These
        moves do not consider the locations of other pieces."""
        hyp_moves = {}

        # iterate through all possible destinations, saving them with their
        # corresponding intermediate positions as {dest.: [interm1, interm2, ...]}
        for next_position in [self.position_u, self.position_d,
                              self.position_l, self.position_r]:
            # initialize the destination
            destination = self.get_position()
            intermediates = []
            while next_position(destination) is not None:
                destination = next_position(destination)
                # add destination and its intermediates to dictionary
                hyp_moves[destination] = list(intermediates)
                # previous destination is intermediate of next destination
                intermediates.append(destination)

        # diagonal moves from the corners of a palace
        position = self.get_position()
        red_corners = {'d1', 'f1', 'd3', 'f3'}
        blue_corners = {'d8', 'f8', 'd10', 'f10'}
        if position in red_corners or position in blue_corners:
            if position == 'd1' or position == 'd8':
                next_position = self.position_dr
            if position == 'f1' or position == 'f8':
                next_position = self.position_dl
            if position == 'd3' or position == 'd10':
                next_position = self.position_ur
            if position == 'f3' or position == 'f10':
                next_position = self.position_ul

            destination = next_position()
            hyp_moves[destination] = []  # add center of palace to dict
            hyp_moves[next_position(destination)] = [destination]  # opp. corner

        # diagonal moves from the center of a palace
        red_center = 'e2'
        blue_center = 'e9'
        if position == blue_center:
            for corner in blue_corners:
                hyp_moves[corner] = []

        if position == red_center:
            for corner in red_corners:
                hyp_moves[corner] = []

        self._hyp_moves = hyp_moves
        return hyp_moves


class Elephant(Piece):
    """
    Represents an elephant, a sub-class of Piece.
    Elephants move horizontally or vertically one space and then two spaces
    diagonally outward to arrive at their destination. They may not jump other
    pieces.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position):
        """
        Creates an Elephant with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cel#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'a1'
        """
        super().__init__(piece_id, position)

    def update_hyp_moves(self):
        """Updates and returns the piece's hypothetical moves dictionary. These
        moves do not consider the locations of other pieces."""
        hyp_moves = {}

        # each horizontal/vertical direction splits into two diagonal directions
        for next_position, branch_positions in {
            self.position_u: [self.position_ul, self.position_ur],
            self.position_d: [self.position_dl, self.position_dr],
            self.position_l: [self.position_ul, self.position_dl],
            self.position_r: [self.position_ur, self.position_dr]
            }.items():

            # the first intermediate is adjacent
            intermediate_1 = next_position()
            if intermediate_1 is not None:

                # for each diagonal direction, take two more steps to arrive at
                # the destination and pass a second intermediate
                for branch_position in branch_positions:
                    intermediate_2 = branch_position(intermediate_1)
                    if intermediate_2 is not None:
                        destination = branch_position(intermediate_2)
                        if destination is not None:
                            hyp_moves[destination] = \
                                [intermediate_1, intermediate_2]

        self._hyp_moves = hyp_moves
        return hyp_moves


class General(Piece):
    """
    Represents a General, a sub-class of Piece.
    Generals are confined to the palace. They can move one step horizontally or
    vertically. They can also move diagonally if they are at a corner or center
    of the palace.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position):
        """
        Creates a General with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cge1', where the first c is the color r or b
            position: (str) board position, e.g., 'e2'
        """
        super().__init__(piece_id, position)

    def update_hyp_moves(self):
        """Updates and returns the piece's hypothetical moves dictionary. These
        moves do not consider the locations of other pieces."""
        hyp_moves = {}
        color = self.get_piece_id()[0]  # 'b' or 'r'

        # iterate through horizontal and vertical destinations
        for next_position in [self.position_u, self.position_d,
                              self.position_l, self.position_r]:

            destination = next_position()
            if destination is not None:

                # check whether destination is in the palace
                if destination[0] < 'd' or destination[0] > 'f':
                    continue
                if color == 'b' and int(destination[1:]) < 8:
                    continue
                if color == 'r' and int(destination[1:]) > 3:
                    continue

                hyp_moves[destination] = []  # one step so no intermediates

        # diagonal destinations
        position = self.get_position()
        if color == 'r':
            red_corners = {'d1', 'f1', 'd3', 'f3'}
            red_center = 'e2'

            if position in red_corners:
                hyp_moves[red_center] = []
            if position == red_center:
                for corner in red_corners:
                    hyp_moves[corner] = []

        else:  # color == 'b'
            blue_corners = {'d8', 'f8', 'd10', 'f10'}
            blue_center = 'e9'

            if position in blue_corners:
                hyp_moves[blue_center] = []
            if position == blue_center:
                for corner in blue_corners:
                    hyp_moves[corner] = []

        self._hyp_moves = hyp_moves
        return hyp_moves


class Guard(Piece):
    """
    Represents a Guard, a sub-class of Piece.
    Guards are confined to the palace. They can move one step horizontally or
    vertically. They can also move diagonally if they are at a corner or center
    of the palace.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position):
        """
        Creates a Guard with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cgu#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'e2'
        """
        super().__init__(piece_id, position)

    def update_hyp_moves(self):
        """Updates and returns the piece's hypothetical moves dictionary. These
        moves do not consider the locations of other pieces."""
        #TODO: This method is the same as for the general (at this time of
        # writing). May want to reduce repetition
        hyp_moves = {}
        color = self.get_piece_id()[0]  # 'b' or 'r'

        # iterate through horizontal and vertical destinations
        for next_position in [self.position_u, self.position_d,
                              self.position_l, self.position_r]:

            destination = next_position()
            if destination is not None:

                # check whether destination is in the palace
                if destination[0] < 'd' or destination[0] > 'f':
                    continue
                if color == 'b' and int(destination[1:]) < 8:
                    continue
                if color == 'r' and int(destination[1:]) > 3:
                    continue

                hyp_moves[destination] = []  # one step so no intermediates

        # diagonal destinations
        position = self.get_position()
        if color == 'r':
            red_corners = {'d1', 'f1', 'd3', 'f3'}
            red_center = 'e2'

            if position in red_corners:
                hyp_moves[red_center] = []
            if position == red_center:
                for corner in red_corners:
                    hyp_moves[corner] = []

        else:  # color == 'b'
            blue_corners = {'d8', 'f8', 'd10', 'f10'}
            blue_center = 'e9'

            if position in blue_corners:
                hyp_moves[blue_center] = []
            if position == blue_center:
                for corner in blue_corners:
                    hyp_moves[corner] = []

        self._hyp_moves = hyp_moves
        return hyp_moves


class Horse(Piece):
    """
    Represents a horse, a sub-class of Piece.
    Horses move horizontally or vertically one space and then one space
    diagonally outward to arrive at their destination. They may not jump other
    pieces.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position):
        """
        Creates a Horse with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cho#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'a1'
        """
        super().__init__(piece_id, position)

    def update_hyp_moves(self):
        """Updates and returns the piece's hypothetical moves dictionary. These
        moves do not consider the locations of other pieces."""
        hyp_moves = {}

        # each horizontal/vertical direction splits into two diagonal directions
        for next_position, branch_positions in {
            self.position_u: [self.position_ul, self.position_ur],
            self.position_d: [self.position_dl, self.position_dr],
            self.position_l: [self.position_ul, self.position_dl],
            self.position_r: [self.position_ur, self.position_dr]
        }.items():

            # the intermediate is adjacent
            intermediate = next_position()
            if intermediate is not None:

                # for each diagonal direction, take a step to the destination
                for branch_position in branch_positions:
                    destination = branch_position(intermediate)
                    if destination is not None:
                        hyp_moves[destination] = [intermediate]

        self._hyp_moves = hyp_moves
        return hyp_moves


class Soldier(Piece):
    """
    Represents a soldier, a sub-class of Piece.
    Soldiers can move forward or sideways one space.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position):
        """
        Creates a Soldier with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cso#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'a1'
        """
        super().__init__(piece_id, position)

    def update_hyp_moves(self):
        """Updates and returns the piece's hypothetical moves dictionary. These
        moves do not consider the locations of other pieces."""
        hyp_moves = {}
        color = self.get_piece_id()[0]  # 'b' or 'r'

        # forward direction depends on the color
        if color == 'b':
            forward = self.position_u
        else:
            forward = self.position_d

        # iterate through all possible destinations
        for next_position in [forward, self.position_l, self.position_r]:
            destination = next_position()
            if destination is not None:
                hyp_moves[destination] = []
                #TODO: may not want to use dictionary for soldiers, generals,
                # and guards, which never have intermediates

        # soldiers can move diagonally forward in the palace
        position = self.get_position()

        if color == 'b':
            if position == 'd3' or position == 'f3':  # palace corners
                hyp_moves['e2'] = []
            if position == 'e2':  # palace center
                hyp_moves['d1'] = []
                hyp_moves['f1'] = []

        else:  # color == 'r'
            if position == 'd8' or position == 'f8':  # palace corners
                hyp_moves['e9'] = []
            if position == 'e9':  # palace center
                hyp_moves['d10'] = []
                hyp_moves['f10'] = []

        self._hyp_moves = hyp_moves
        return hyp_moves


def main():
    #game = JanggiGame()
    #game.display_board()
    cannon = Cannon('bca1', 'd1')
    hyp_moves = cannon.update_hyp_moves()
    print(hyp_moves)
    chariot = Chariot('bch1', 'e2')
    hyp_moves = chariot.update_hyp_moves()
    print(hyp_moves)
    elephant = Elephant('bel1', 'h2')
    hyp_moves = elephant.update_hyp_moves()
    print(hyp_moves)
    horse = Horse('bho1', 'i10')
    hyp_moves = horse.update_hyp_moves()
    print(hyp_moves)
    soldier = Soldier('bso1', 'e2')
    hyp_moves = soldier.update_hyp_moves()
    print(hyp_moves)
    general = General('rge1', 'f2')
    hyp_moves = general.update_hyp_moves()
    print(hyp_moves)
    guard = Guard('rge1', 'f2')
    hyp_moves = guard.update_hyp_moves()
    print(hyp_moves)

if __name__ == '__main__':
    main()
