# Author: Travis Harris
# Date: 3/27/2021
# Description: Implementation of the board game Janggi, with a class (JanggiGame)
# for playing the game. Other classes include Board, PLayer, Piece, and one for
# each piece type. Running this file will start the game in terminal mode, which
# accepts positions (e.g., a1, i10) indicating which piece to move and where to
# move it. Turns can be passed by specifying the same position to move to and
# from. To run the game in GUI mode, run JanggiGUI.py instead.
# The game ends by checkmate. Movement rules are described in the docstrings for
# each individual piece's class, and on Wikipedia. JanggiGUI highlights allowed
# moves, making it beginner-friendly.

class JanggiGame:
    """
    An implementation of the board game Janggi. Has two Player objects and
    a Board object that it initializes to start the game. The game is played
    by using this class's make_move method. This class keeps track of the turn,
    whether the generals are in check, and determines if the game is over. It
    must interact with the Board and the Player to determine where the pieces
    are and what their allowed moves are. It also communicates with the Player's
    General objects because it needs to pass information from the opposing
    Player to the General.

    Data members: See __init__
    Methods: get_game_state, set_game_state, get_turn, get_num_turns, next_turn,
        get_board, get_red_player, get_blue_player, get_current_player,
        get_opponent, is_in_check, is_checkmate, make_move, undo_move,
        update_generals
    """
    def __init__(self):
        """
        Creates a JanggiGame.
        Private data members:
            game_state: (str) 'UNFINISHED', 'RED_WON', or 'BLUE_WON'
            turn: represents whose turn it is, (str) 'red' or 'blue'
            num_turns: the number of turns that have been played (int)
            board: Board object
            red_player: Player object
            blue_player: Player object
        """
        self._game_state = 'UNFINISHED'
        self._turn = 'blue'
        self._num_turns = 0
        self._board = Board()
        self._red_player = Player('red', self._board)
        self._blue_player = Player('blue', self._board)
        self.update_generals()  # initialize general's allowed moves

    def get_turn(self):
        """Returns the turn (str), which may be 'blue' or 'red' depending on
        which player's turn it is."""
        return self._turn

    def get_num_turns(self):
        """Returns the number of turns that have been played (int)"""
        return self._num_turns

    def next_turn(self):
        """If the turn is 'blue', sets the turn to 'red' (str), and vice
        versa."""
        turn = self.get_turn()
        if turn == 'blue':
            self._turn = 'red'
        else:
            self._turn = 'blue'

        # increment the number of turns that have been played
        self._num_turns += 1

    def get_board(self):
        """Returns the board object."""
        return self._board

    def get_red_player(self):
        """Returns the Player object for the red player."""
        return self._red_player

    def get_blue_player(self):
        """Returns the Player object for the blue player."""
        return self._blue_player

    def get_current_player(self):
        """Returns the Player object for the player whose turn it is."""
        if self.get_turn() == 'red':
            return self.get_red_player()
        return self.get_blue_player()

    def get_opponent(self):
        """Returns the Player object for the player whose turn it is not."""
        if self.get_turn() == 'red':
            return self.get_blue_player()
        return self.get_red_player()

    def get_game_state(self):
        """Returns game state (str) which may be 'UNFINISHED', 'RED_WON', or
        BLUE_WON'."""
        return self._game_state

    def set_game_state(self, game_state):
        """Sets the game state to the specified game_state (str)."""
        self._game_state = game_state

    def is_in_check(self, color):
        """Takes a color (str) 'blue' or 'red' and returns True if the
        corresponding player is in check, otherwise False. In check means the
        general could be captured by the opponent on their next move."""
        if color == 'red':
            opponent = self.get_blue_player()
        else:
            opponent = self.get_red_player()

        if len(opponent.get_pieces_checking()) > 0:
            return True
        return False

    def is_checkmate(self):
        """
        Returns True if the player whose turn it is has their opponent in
        checkmate (i.e., if the player has won the game), otherwise returns
        False. Checkmate is when the opponent's general is in check and would
        not be able to get out of it on their next move because the general has
        no allowed moves, or there are no moves that can block or capture the
        piece(s) that has the general in check.
        """
        board = self.get_board()
        current_player = self.get_current_player()
        pieces_checking = current_player.get_pieces_checking()

        opponent = self.get_opponent()
        opponent_color = opponent.get_color()
        opponent_pieces = opponent.get_pieces()
        opponent_allowed_destinations = opponent.get_allowed_destinations()

        if opponent_color == 'red':
            general = opponent_pieces['rge1']
        else:
            general = opponent_pieces['bge1']

        # if general has an allowed move it can get out of check
        if len(general.get_allowed_moves()) > 0:
            return False

        # check whether only one piece has the general in check
        if len(pieces_checking) == 1:

            # if the piece can be captured, it's not a checkmate
            if pieces_checking[0].get_position() in opponent_allowed_destinations:
                return False

            # if the piece is a cannon, check whether it is jumping an
            # opponent's piece. If that piece can be moved, the cannon no
            # longer has the general in check
            if pieces_checking[0].get_piece_id()[1:3] == 'ca':
                path_to_general = pieces_checking[0].get_path_to_general()
                for position in path_to_general:
                    piece_id_in_path = board.get_occupation(position)
                    if piece_id_in_path is not None:
                        if piece_id_in_path[0] == opponent_color[0]:
                            piece_in_path = opponent_pieces[piece_id_in_path]
                            if len(piece_in_path.get_allowed_moves()) > 0:
                                return False

        # check whether all pieces with the general in check can be blocked
        # in a single move. Don't include soldiers, because they can't be
        # blocked.
        # First, get list of path_to_general sets
        path_to_general_sets = [piece.get_path_to_general() for piece in
                           pieces_checking if piece.get_piece_id()[1:3] != 'so']

        # get positions the opponent must reach to block all paths
        # if there is only one piece with the general in check, the
        # positions_to_block will just be that piece's path_to_general
        if path_to_general_sets != []:
            positions_to_block = set.intersection(*path_to_general_sets)
            if len(positions_to_block) > 0:
                blocking_destinations = positions_to_block & \
                                        opponent_allowed_destinations
                if len(blocking_destinations) > 0:
                    return False

        return True

    def make_move(self, from_pos, to_pos):
        """
        Moves a piece from its current position to an allowed position, and may
        capture an opposing piece. The piece being moved must belong to the
        player whose turn it is and it must not result in the player putting
        themself in check. Determines if the move results in checkmate and
        updates the game_state, board, players, and pieces before updating
        the turn.

        Parameters: from_pos and to_pos are strings representing positions
            (e.g., 'b3')
        Returns: True if the move is allowed, otherwise False.
        """
        # input validation
        for pos in [from_pos, to_pos]:
            if pos == '':
                print('No position specified')
                return False
            if len(pos) < 2 or len(pos) > 3:
                print('Invalid board position')
                return False
            if pos[0] < 'a' or pos[0] > 'i' or \
                    int(pos[1:]) < 1 or int(pos[1:]) > 10:
                print('Invalid board position')
                return False

        # confirm game is unfinished
        if self.get_game_state() != 'UNFINISHED':
            print('The game is already finished.')
            return False

        # allow passing turns
        color = self.get_turn()
        in_check = self.is_in_check(color)
        if from_pos == to_pos:
            if in_check:
                print('Player is in check. Passing is not allowed.')
                return False

            self.next_turn()
            return True

        # confirm that there is a piece to move
        board = self.get_board()
        piece_id = board.get_occupation(from_pos)
        if piece_id is None:
            print("The position to move from is empty.")
            return False

        # confirm that the piece belongs to the player
        current_player = self.get_current_player()
        if piece_id not in current_player.get_pieces():
            print("The piece belongs to the other player.")
            return False

        # determine whether the general is being moved
        general_moving = False

        if color == 'red':
            general = current_player.get_pieces()['rge1']
        else:
            general = current_player.get_pieces()['bge1']

        if piece_id[1:3] == 'ge':
            general_moving = True

            # determine whether the general's move is allowed
            if to_pos not in general.get_allowed_moves():
                print("The general can't move to that position.")
                return False

        # determine whether the move is allowed
        # this already will deny moves to positions occupied by a piece of the
        # same color
        piece = current_player.get_pieces()[piece_id]
        if to_pos not in piece.get_allowed_moves():
            print("The piece can't move to that position.")
            return False

        # if a piece is captured, remove it from the opponent's pieces
        opponent = self.get_opponent()
        captured_piece_id = board.get_occupation(to_pos)
        if captured_piece_id is not None:
            opponent.remove_piece(captured_piece_id)

        # update the board and the moved piece's position attribute
        board.move_piece(from_pos, to_pos)
        if general_moving:
            board.set_general_position(color, to_pos)
        piece.set_position(to_pos)

        # update the pieces and players based on the state of the board after
        # the move
        opponent.update_pieces()
        current_player.update_pieces()
        self.update_generals()

        # the move must not put or leave the current player in check
        if self.is_in_check(color):
            print('The move is not allowed because it puts or leaves the player'
                  ' in check.')
            self.undo_move(from_pos, to_pos, captured_piece_id)
            return False

        # determine whether the move won the game
        opponent_color = opponent.get_color()
        if self.is_in_check(opponent_color):
            print("The move put the other player in check.")
            if self.is_checkmate():
                print("Checkmate!")
                if opponent_color == 'red':
                    self.set_game_state('BLUE_WON')
                else:
                    self.set_game_state('RED_WON')

        self.next_turn()
        return True

    def undo_move(self, original_from_pos, original_to_pos, captured_piece_id):
        """
        Reverts the latest move that was from the original_from_pos to the
        original_to_pos (str positions). If the latest move did not result in
        a capture, captured_piece_id must be None. Otherwise the piece in the
        original_to_pos is moved back and the captured_piece_id (str) is used to
        initialize the piece, place it on the board where it was before, and
        add it back to its player.
        """
        # update the piece's position attribute and its position on the board
        board = self.get_board()
        piece_id = board.get_occupation(original_to_pos)
        current_player = self.get_current_player()
        piece = current_player.get_pieces()[piece_id]
        piece.set_position(original_from_pos)

        # if the general was moved, set the board's general_position
        color = current_player.get_color()
        if original_to_pos == board.get_general_position(color):
            board.set_general_position(color, original_from_pos)

        # update the moved piece's position on the board
        board.move_piece(original_to_pos, original_from_pos)

        # add a captured piece back
        opponent = self.get_opponent()
        if captured_piece_id is not None:

            # add it back to the board
            board.set_occupation(captured_piece_id, original_to_pos)

            # initialize the piece and add it back to the player
            opponent.add_piece(captured_piece_id, original_to_pos)

        # update the pieces and players based on the state of the board after
        # the move is undone
        opponent.update_pieces()
        current_player.update_pieces()
        self.update_generals()

    def update_generals(self):
        """Updates each general's allowed_moves based on the current state of
        the board. Does not allow moves that put the general in check."""
        board = self.get_board()
        red_player = self.get_red_player()
        blue_player = self.get_blue_player()
        players_general_ids = [(red_player, blue_player, 'rge1'),
                               (blue_player, red_player, 'bge1')]

        for player1, player2, general_id in players_general_ids:
            general = player1.get_pieces()[general_id]
            color = general_id[0]
            hyp_moves = general.get_hyp_moves()
            allowed_moves = hyp_moves.copy()
            opponent_palace_destinations = player2.get_allowed_palace_destinations()

            # eliminate moves that put the general in check
            for destination in hyp_moves:
                if destination in opponent_palace_destinations:
                    del allowed_moves[destination]
                    continue

                # eliminate moves with the destination occupied by a piece of
                # the same color
                piece_id_at_destination = board.get_occupation(destination)
                if piece_id_at_destination is not None:
                    if piece_id_at_destination[0] == color:
                        del allowed_moves[destination]

            general.set_allowed_moves(allowed_moves)

            # update each player's allowed_destinations
            allowed_destinations = player1.get_allowed_destinations()
            allowed_destinations |= set(allowed_moves)


class Board:
    """
    Represents a Janggi board.
    This class keeps track of the positions of all pieces and can be used to
    print the board. A Board object is created by the JanggiGame and is passed
    to the Players and the Pieces because they all need access in order to see
    what Piece is in a given position.

    Data members: See __init__
    Methods: get_general_position, set_general_position, move_piece, get_board,
        display_board, get_occupation, set_occupation, clear_position,
        _init_board_dict
    """
    def __init__(self):
        """
        Creates a Janggi Board.
        Private data member:
            board: dictionary organized as {position (str): piece_id (str)} for
                all positions on a Janggi board. The board is initialized with
                the pieces in their starting positions for a Janggi game.
            general_position: dictionary organized as
                {color (str): position (str)}
        """
        self._general_position = {'red': 'e2', 'blue': 'e9'}
        self._board = self._init_board_dict()

    def _init_board_dict(self):
        """Returns the board dictionary {position (str): piece_id (str)}
        with the pieces in their starting positions."""

        board = {'a1': 'rch1', 'b1': 'rel1', 'c1': 'rho1', 'd1': 'rgu1',
                 'f1': 'rgu2', 'g1': 'rel2', 'h1': 'rho2', 'i1': 'rch2',
                 'e2': 'rge1', 'b3': 'rca1', 'h3': 'rca2', 'a4': 'rso1',
                 'c4': 'rso2', 'e4': 'rso3', 'g4': 'rso4', 'i4': 'rso5',
                 'a7': 'bso1', 'c7': 'bso2', 'e7': 'bso3', 'g7': 'bso4',
                 'i7': 'bso5', 'b8': 'bca1', 'h8': 'bca2', 'e9': 'bge1',
                 'a10': 'bch1', 'b10': 'bel1', 'c10': 'bho1', 'd10': 'bgu1',
                 'f10': 'bgu2', 'g10': 'bel2', 'h10': 'bho2', 'i10': 'bch2'}

        # unoccupied positions are indicated by '----'
        for col in 'abcdefghi':
            for row in range(1, 11):
                position = col + str(row)
                if position not in board:
                    board[position] = '----'

        return board

    def get_general_position(self, color):
        """Takes a color (str 'red' or 'blue') and returns the position of
        the corresponding general."""
        if color == 'red':
            return self._general_position['red']
        return self._general_position['blue']

    def set_general_position(self, color, position):
        """Takes a position (str) and a color (str 'red' or 'blue') of a general
        and updates the general_position dictionary."""
        if color == 'red':
            self._general_position['red'] = position
        else:
            self._general_position['blue'] = position

    def get_board(self):
        """Returns the board dictionary."""
        return self._board

    def get_occupation(self, position):
        """Takes a position (str) and returns the piece_id (str) of the piece
        occupying the position, or returns None if the position is
        unoccupied."""
        board = self.get_board()
        if board[position] == '----':
            return None
        return board[position]

    def set_occupation(self, piece_id, position):
        """Takes a piece_id (str) and a position (str) and updates the board
        dictionary."""
        self._board[position] = piece_id

    def clear_position(self, position):
        """Takes a position (str) and clears it by setting its value in the
        board dictionary to '----'."""
        self.set_occupation('----', position)

    def move_piece(self, from_pos, to_pos):
        """
        Takes positions (str) to move a piece from and to, and updates the
        board. If the piece that is moving is a general, updates the
        general_position dictionary.
        Returns the piece_id (str) of a captured piece, or None if the
        destination was unoccupied.
        """
        moving_piece_id = self.get_occupation(from_pos)
        captured_piece_id = self.get_occupation(to_pos)  # None if no capture

        # if moving piece is a general update its position in the
        # general_position dictionary
        if moving_piece_id[1:3] == 'ge':
            if moving_piece_id[0] == 'r':
                color = 'red'
            else:
                color = 'blue'
            self.set_general_position(color, to_pos)

        # update the board
        self.clear_position(from_pos)
        self.set_occupation(moving_piece_id, to_pos)

        return captured_piece_id

    def display_board(self):
        """Displays the board with the pieces in their current positions."""
        board = self.get_board()

        # print the column headers
        print('     a    b    c    d    e    f    g    h    i')

        # print the board, one row at a time, by first making a list for the row
        for row in range(1, 11):

            # start row with number
            row_list = [str(row)]

            # extra space after single digits so they match the '10 '
            if row < 10:
                row_list.append('')

            # fill the row_list
            for col in 'abcdefghi':
                position = col + str(row)
                row_list.append(board[position])

            # display piece_ids in row_list separated by spaces
            print(*row_list)

        # finish with blank line
        print()


class Player:
    """
    Represents a Janggi player.
    There are two Players in the game. They each have a collection of Piece
    objects which they initialize in their starting positions. The Player has a
    method to make all of its Pieces update their data members based on the
    current state of the board. The Player keeps sets of allowed_destinations
    which are used by the JanggiGame and the opposing Player's General to
    determine whether they are in check or checkmate. The Player is passed the
    Board from the JanggiGame so that it can pass it on to the Pieces which need
    it to determine whether positions are occupied.

    Data members: See __init__
    Methods: get_color, get_pieces, get_pieces_checking, set_pieces_checking,
        get_board, get_allowed_destinations, set_allowed_destinations,
        get_allowed_palace_destinations, set_allowed_palace_destinations,
        add_piece, remove_piece, update_pieces, _init_pieces
    """
    def __init__(self, color, board):
        """
        Creates a Janggi Player and calls _init_pieces to initialize the Piece
        objects and add them to the player's pieces dictionary

        Private data members:
            allowed_destinations: set of destinations that the player's pieces
                can legally reach given the current state of the board
            allowed_palace_destinations = set of destinations in the opponent's
                palace that can be reached in a legal move or one that would
                be legal except it is occupied by a piece that belongs to the
                player
            color: (str) 'blue' or 'red'
            pieces: dictionary with piece_id as keys and Piece objects as values
            pieces_checking: list of Piece objects that have the opposing
                general in check
            board: Board object
        """
        self._allowed_destinations = set()
        self._allowed_palace_destinations = set()
        self._color = color
        self._pieces = {}
        self._pieces_checking = []
        self._board = board
        self._init_pieces(board)

    def get_color(self):
        """Returns the Player's color"""
        return self._color

    def get_pieces(self):
        """Returns the Player's pieces dictionary"""
        return self._pieces

    def get_pieces_checking(self):
        """Returns the Player's list of Piece objects with the opponent's
        general in check"""
        return self._pieces_checking

    def set_pieces_checking(self, pieces_checking):
        """Sets the Player's pieces_checking to the list parameter"""
        self._pieces_checking = pieces_checking

    def add_piece(self, piece_id, position):
        """Takes a piece_id (str) and a position (str) and adds the piece_id and
        corresponding Piece object to the Player's pieces dictionary. The Piece
        is initialized with the given piece_id and position."""
        pieces = self.get_pieces()
        board = self.get_board()

        if piece_id[1:3] == 'ca':
            pieces[piece_id] = Cannon(piece_id, position, board)
        elif piece_id[1:3] == 'ch':
            pieces[piece_id] = Chariot(piece_id, position, board)
        elif piece_id[1:3] == 'el':
            pieces[piece_id] = Elephant(piece_id, position, board)
        elif piece_id[1:3] == 'gu':
            pieces[piece_id] = Guard(piece_id, position, board)
        elif piece_id[1:3] == 'ho':
            pieces[piece_id] = Horse(piece_id, position, board)
        elif piece_id[1:3] == 'so':
            pieces[piece_id] = Soldier(piece_id, position, board)

    def remove_piece(self, piece_id):
        """Takes a piece_id and removes it from the Player's pieces dictionary
        along with the corresponding Piece object"""
        pieces = self.get_pieces()
        del pieces[piece_id]

    def get_allowed_destinations(self):
        """Returns the allowed_destinations set"""
        return self._allowed_destinations

    def set_allowed_destinations(self, allowed_destinations):
        """Sets the Player's allowed_destinations set to the set parameter"""
        self._allowed_destinations = allowed_destinations

    def get_allowed_palace_destinations(self):
        """Returns the allowed_palace_destinations set"""
        return self._allowed_palace_destinations

    def set_allowed_palace_destinations(self, allowed_palace_destinations):
        """Sets the Player's allowed_destinations set to the set parameter"""
        self._allowed_palace_destinations = allowed_palace_destinations

    def get_board(self):
        """Returns the Board object."""
        return self._board

    def update_pieces(self):
        """
        Updates each of the Player's pieces so that all of their data
        members reflect the current state of the board, and updates the Player's
        pieces_checking, allowed_destinations, and allowed_palace destinations
        """
        pieces = self.get_pieces().values()  # pieces is now a list of objects
        allowed_destinations = set()
        allowed_palace_destinations = set()
        pieces_checking = []

        color = self.get_color()
        board = self.get_board()
        if color == 'red':
            opposing_general_position = board.get_general_position('blue')
        else:
            opposing_general_position = board.get_general_position('red')

        for piece in pieces:
            piece.update_hyp_moves()
            piece.update_allowed_moves()
            piece.update_allowed_palace_destinations()

            # add the piece's destinations to the player's sets
            allowed_destinations |= set(piece.get_allowed_moves())
            allowed_palace_destinations |= piece.get_allowed_palace_destinations()

            # if the piece has the opposing general in check add it to the
            # Player's pieces_checking
            if piece.is_checking(opposing_general_position):
                pieces_checking.append(piece)

        self.set_allowed_destinations(allowed_destinations)
        self.set_allowed_palace_destinations(allowed_palace_destinations)
        self.set_pieces_checking(pieces_checking)

    def _init_pieces(self, board):
        """Initializes the Player's pieces in their starting positions and adds
        them to the pieces dictionary."""
        color = self.get_color()

        if color == 'blue':
            pieces = {'bso1': Soldier('bso1', 'a7', board), 'bso2': Soldier('bso2', 'c7', board),
                      'bso3': Soldier('bso3', 'e7', board), 'bso4': Soldier('bso4', 'g7', board),
                      'bso5': Soldier('bso5', 'i7', board), 'bca1': Cannon('bca1', 'b8', board),
                      'bca2': Cannon('bca2', 'h8', board), 'bge1': General('bge1', 'e9', board),
                      'bch1': Chariot('bch1', 'a10', board), 'bel1': Elephant('bel1', 'b10', board),
                      'bho1': Horse('bho1', 'c10', board), 'bgu1': Guard('bgu1', 'd10', board),
                      'bgu2': Guard('bgu2', 'f10', board), 'bel2': Elephant('bel2', 'g10', board),
                      'bho2': Horse('bho2', 'h10', board), 'bch2': Chariot('bch2', 'i10', board)}
        else:
            pieces = {'rso1': Soldier('rso1', 'a4', board), 'rso2': Soldier('rso2', 'c4', board),
                      'rso3': Soldier('rso3', 'e4', board), 'rso4': Soldier('rso4', 'g4', board),
                      'rso5': Soldier('rso5', 'i4', board), 'rca1': Cannon('rca1', 'b3', board),
                      'rca2': Cannon('rca2', 'h3', board), 'rge1': General('rge1', 'e2', board),
                      'rch1': Chariot('rch1', 'a1', board), 'rel1': Elephant('rel1', 'b1', board),
                      'rho1': Horse('rho1', 'c1', board), 'rgu1': Guard('rgu1', 'd1', board),
                      'rgu2': Guard('rgu2', 'f1', board), 'rel2': Elephant('rel2', 'g1', board),
                      'rho2': Horse('rho2', 'h1', board), 'rch2': Chariot('rch2', 'i1', board)}

        self._pieces = pieces
        allowed_destinations = set()

        for piece in pieces.values():
            piece.update_hyp_moves()
            piece.update_allowed_moves()
            allowed_destinations |= set(piece.get_allowed_moves())

        self.set_allowed_destinations(allowed_destinations)


class Piece:
    """
    Represents a Janggi piece.
    This is the parent class of each type of Janggi piece. They inherit all
    the methods and data members of this class. Pieces need access to the board
    because they have methods to determine their allowed moves based on its
    current state.

    Data members: See __init__
    Methods: get_position, set_position, get_hyp_moves, set_hyp_moves,
        get_path_to_general, set_path_to_general, get piece_id,
        get_allowed_moves, set_allowed_moves, update_allowed_moves,
        get_allowed_palace_destinations, set_allowed_palace_destinations,
        update_allowed_palace_destinations, get_board, is_checking
        position_u, position_d, position_l, position_r,
        position_ul, position_ur, position_dl, position_dr
    """
    def __init__(self, piece_id, position, board):
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
            allowed_moves: dictionary of moves the piece can make based on the
                positions of all other pieces on the board. The format is the
                same as for hyp_moves ({dest: [interm1, interm2]}).
            allowed_palace_destinations = set of destinations in the opponent's
                palace that can be reached in a legal move or one that would
                be legal except it is occupied by a piece that belongs to the
                player
            path_to_general = set of intermediate positions along the allowed
                path from the piece to the opposing general
        """
        self._piece_id = piece_id
        self._position = position
        self._hyp_moves = {}
        self._allowed_moves = {}
        self._allowed_palace_destinations = set()
        self._board = board
        self._path_to_general = set()

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

    def get_path_to_general(self):
        """Returns the path_to_general set."""
        return self._path_to_general

    def set_path_to_general(self, path_to_general):
        """Takes a set (path_to_general) and sets the path_to_general data
        member."""
        self._path_to_general = path_to_general

    def is_checking(self, opposing_general_position):
        """Takes the opposing general's position (str) and returns True if it
        is an allowed destination, otherwise returns False. If True, also
        updates the path_to_general set with the intermediate positions
        along the move."""
        allowed_moves = self.get_allowed_moves()
        if opposing_general_position in allowed_moves:
            intermediates = allowed_moves[opposing_general_position]
            self.set_path_to_general(set(intermediates))
            return True

        return False

    def get_hyp_moves(self):
        """Returns the hyp_moves dictionary."""
        return self._hyp_moves

    def set_hyp_moves(self, hyp_moves):
        """Sets hyp_moves to the specified dictionary"""
        self._hyp_moves = hyp_moves

    def get_allowed_moves(self):
        """Returns the allowed_moves dictionary"""
        return self._allowed_moves

    def set_allowed_moves(self, allowed_moves):
        """Sets allowed_moves to the specified dictionary"""
        self._allowed_moves = allowed_moves

    def get_allowed_palace_destinations(self):
        """Returns the allowed_palace_destinations set"""
        return self._allowed_palace_destinations

    def set_allowed_palace_destinations(self, allowed_palace_destinations):
        """Sets the Player's allowed_destinations set to the set parameter"""
        self._allowed_palace_destinations = allowed_palace_destinations

    def get_board(self):
        """Returns the Board object"""
        return self._board

    def update_allowed_palace_destinations(self):
        """Updates the piece's set of allowed_palace_destinations. These are
        positions in the opposing palace that the piece can move to, including
        those that are occupied by a piece of the same color."""
        piece_id = self.get_piece_id()
        color = piece_id[0]
        board = self.get_board()
        hyp_moves = self.get_hyp_moves()
        allowed_moves = hyp_moves.copy()

        red_palace = {'d1', 'e1', 'f1', 'd2', 'e2', 'f2', 'd3', 'e3', 'f3'}
        blue_palace = {'d8', 'e8', 'f8', 'd9', 'e9', 'f9', 'd10', 'e10', 'f10'}

        # eliminate moves with an occupied intermediate position unless the
        # general is the intermediate, because the general uses this info
        # to determine where it can't move, and it shouldn't be able to move
        # away from, say, a chariot that has it in check
        for destination, intermediates in hyp_moves.items():
            for intermediate in intermediates:
                piece_id_at_intermediate = board.get_occupation(intermediate)
                if piece_id_at_intermediate is not None:
                    if piece_id_at_intermediate[1:3] != 'ge':
                        if destination in allowed_moves:  # not yet deleted
                            del allowed_moves[destination]

        # find intersection of allowed_moves and the opposing player's palace
        if color == 'r':
            allowed_palace_destinations = set(allowed_moves) & blue_palace
        else:
            allowed_palace_destinations = set(allowed_moves) & red_palace

        self.set_allowed_palace_destinations(allowed_palace_destinations)

    def update_allowed_moves(self):
        """Updates the piece's allowed moves dictionary. Allowed moves are legal
         based on the current state of the board."""
        piece_id = self.get_piece_id()
        color = piece_id[0]
        board = self.get_board()
        hyp_moves = self.get_hyp_moves()
        allowed_moves = hyp_moves.copy()

        # eliminate moves with the destination occupied by a piece of the same
        # color
        for destination in hyp_moves:
            piece_id_at_destination = board.get_occupation(destination)
            if piece_id_at_destination is not None:
                if piece_id_at_destination[0] == color:
                    del allowed_moves[destination]

        # prevent iterating through already eliminated moves
        hyp_moves = allowed_moves.copy()

        # eliminate moves with an occupied intermediate position
        for destination, intermediates in hyp_moves.items():
            for intermediate in intermediates:
                if board.get_occupation(intermediate) is not None:
                    if destination in allowed_moves:  # not yet deleted
                        del allowed_moves[destination]

        self.set_allowed_moves(allowed_moves)

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
    They can move diagonally between corners of the palace.

    Data members: See __init__
    Methods: inherited methods, update_hyp_moves, and overriding versions of
        update_allowed_moves and update_allowed_palace_destinations
    """
    def __init__(self, piece_id, position, board):
        """
        Creates a Cannon with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cca#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'a1'
        """
        super().__init__(piece_id, position, board)

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

        # diagonal jumps from the corners of a palace
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

            intermediate = next_position()  # center of a palace
            destination = next_position(intermediate)
            hyp_moves[destination] = [intermediate]

        self.set_hyp_moves(hyp_moves)

    def update_allowed_moves(self):
        """Updates and returns the piece's allowed moves dictionary. Allowed
        moves are legal based on the current state of the board. This method
        overrides the method inherited from Piece, because cannons have special
        rules: They must jump one piece and it can't be a cannon."""
        piece_id = self.get_piece_id()
        color = piece_id[0]
        board = self.get_board()
        hyp_moves = self.get_hyp_moves()
        allowed_moves = hyp_moves.copy()

        # eliminate moves with the destination occupied by a cannon or a piece
        # of the same color
        for destination in hyp_moves:
            piece_id_at_destination = board.get_occupation(destination)
            if piece_id_at_destination is not None:
                if piece_id_at_destination[0] == color or \
                        piece_id_at_destination[1:3] == 'ca':
                    del allowed_moves[destination]

        # prevent iterating through already eliminated moves
        hyp_moves = allowed_moves.copy()

        # eliminate moves without an occupied intermediate position
        for destination, intermediates in hyp_moves.items():
            for intermediate in intermediates:
                # if there is an intermediate, proceed to the next destination
                if board.get_occupation(intermediate) is not None:
                    break
                # if current intermediate position is the last one in the list,
                # then the path has no intermediates occupied
                elif intermediate == intermediates[-1]:
                    del allowed_moves[destination]

        # prevent iterating through already eliminated moves
        hyp_moves = allowed_moves.copy()

        # eliminate moves with >1 occupied intermediate position
        # and those with only 1 if it is a cannon
        for destination, intermediates in hyp_moves.items():
            num_intermediate_pieces = 0  # initialize counter
            for intermediate in intermediates:
                piece_id_at_intermediate = board.get_occupation(intermediate)
                if piece_id_at_intermediate is not None:
                    num_intermediate_pieces += 1
                    if piece_id_at_intermediate[1:3] == 'ca' or \
                            num_intermediate_pieces > 1:
                            if destination in allowed_moves:  # not yet deleted
                                del allowed_moves[destination]

        self.set_allowed_moves(allowed_moves)

    def update_allowed_palace_destinations(self):
        """Updates the piece's set of allowed_palace_destinations. These are
        positions in the opposing palace that the piece can move to, including
        those that are occupied by a piece of the same color."""
        piece_id = self.get_piece_id()
        color = piece_id[0]
        board = self.get_board()
        hyp_moves = self.get_hyp_moves()
        allowed_moves = hyp_moves.copy()

        red_palace = {'d1', 'e1', 'f1', 'd2', 'e2', 'f2', 'd3', 'e3', 'f3'}
        blue_palace = {'d8', 'e8', 'f8', 'd9', 'e9', 'f9', 'd10', 'e10', 'f10'}

        # eliminate moves without an occupied intermediate position
        for destination, intermediates in hyp_moves.items():
            for intermediate in intermediates:
                # if there is an intermediate, proceed to the next destination
                if board.get_occupation(intermediate) is not None:
                    break
                # if current intermediate position is the last one in the list,
                # then the path has no intermediates occupied
                elif intermediate == intermediates[-1]:
                    del allowed_moves[destination]

        # prevent iterating through already eliminated moves
        hyp_moves = allowed_moves.copy()

        # Eliminate moves with >1 occupied intermediate position
        # and those with only 1 if it is a cannon.
        # Also eliminate if the 1 piece is a general and it's the first
        # intermediate encountered, because the purpose
        # of allowed_palace_destinations is for the general to see where it
        # can go; the general should be able to move away from a cannon even if
        # the cannon can jump it.
        for destination, intermediates in hyp_moves.items():
            num_intermediate_pieces = 0  # initialize counter
            for intermediate in intermediates:
                piece_id_at_intermediate = board.get_occupation(intermediate)
                if piece_id_at_intermediate is not None:
                    num_intermediate_pieces += 1
                    if piece_id_at_intermediate[1:3] == 'ge':
                        num_intermediate_pieces -= 1
                    if piece_id_at_intermediate[1:3] == 'ca' or \
                            (piece_id_at_intermediate[1:3] == 'ge' and \
                            num_intermediate_pieces == 0) or \
                            num_intermediate_pieces > 1:
                        if destination in allowed_moves:  # not yet deleted
                            del allowed_moves[destination]

        # find intersection of allowed_moves and the opposing player's palace
        if color == 'r':
            allowed_palace_destinations = set(allowed_moves) & blue_palace
        else:
            allowed_palace_destinations = set(allowed_moves) & red_palace

        self.set_allowed_palace_destinations(allowed_palace_destinations)

class Chariot(Piece):
    """
    Represents a chariot, a sub-class of Piece.
    Chariots can move horizontally or vertically any number of positions, but
    they may not jump over another piece. They can move diagonally between
    corners of the palace.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position, board):
        """
        Creates a Chariot with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cch#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'a1'
        """
        super().__init__(piece_id, position, board)

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

        self.set_hyp_moves(hyp_moves)


class Elephant(Piece):
    """
    Represents an elephant, a sub-class of Piece.
    Elephants move horizontally or vertically one space and then two spaces
    diagonally outward to arrive at their destination. They may not jump other
    pieces.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position, board):
        """
        Creates an Elephant with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cel#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'a1'
        """
        super().__init__(piece_id, position, board)

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

        self.set_hyp_moves(hyp_moves)


class General(Piece):
    """
    Represents a General, a sub-class of Piece.
    Generals are confined to the palace. They can move one step horizontally or
    vertically. They can also move diagonally if they are at a corner or center
    of the palace.

    Data members: See __init__
    Methods: inherited methods, overriding update_allowed_moves, overriding
        update_allowed_palace_destinations, and update_hyp_moves
    """
    def __init__(self, piece_id, position, board):
        """
        Creates a General with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cge1', where the first c is the color r or b
            position: (str) board position, e.g., 'e2'
        """
        super().__init__(piece_id, position, board)

    def update_allowed_moves(self):
        """Overrides the Piece's method. The General's allowed_destinations
        are updated by JanggiGame.update_generals."""
        self.set_allowed_moves({})

    def update_allowed_palace_destinations(self):
        """Overrides the Piece's method. The General can't move out of its
        own palace."""
        pass

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

        self.set_hyp_moves(hyp_moves)


class Guard(Piece):
    """
    Represents a Guard, a sub-class of Piece.
    Guards are confined to the palace. They can move one step horizontally or
    vertically. They can also move diagonally if they are at a corner or center
    of the palace.

    Data members: See __init__
    Methods: inherited methods, overriding update_allowed_palace_destinations
        and update_hyp_moves
    """
    def __init__(self, piece_id, position, board):
        """
        Creates a Guard with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cgu#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'e2'
        """
        super().__init__(piece_id, position, board)

    def update_allowed_palace_destinations(self):
        """Overrides the Piece's method. A Guard can't move out of its
        own palace."""
        pass

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

        self.set_hyp_moves(hyp_moves)


class Horse(Piece):
    """
    Represents a horse, a sub-class of Piece.
    Horses move horizontally or vertically one space and then one space
    diagonally outward to arrive at their destination. They may not jump other
    pieces.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position, board):
        """
        Creates a Horse with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cho#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'a1'
        """
        super().__init__(piece_id, position, board)

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

        self.set_hyp_moves(hyp_moves)


class Soldier(Piece):
    """
    Represents a soldier, a sub-class of Piece.
    Soldiers can move forward or sideways one space. They can also move
    diagonally forward between corners in the palace.

    Data members: See __init__
    Methods: inherited methods and update_hyp_moves
    """
    def __init__(self, piece_id, position, board):
        """
        Creates a Soldier with the data members of a Piece. The parameters are
        set as private data members as follows:
            piece_id: (str) 'cso#', where the first c is the color r or b
                      and # is 1 or 2
            position: (str) board position, e.g., 'a1'
        """
        super().__init__(piece_id, position, board)

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

        self.set_hyp_moves(hyp_moves)


def main():
    """Lets users play the game in the terminal."""
    # initialize the game
    game = JanggiGame()
    board = game.get_board()

    # game loop
    while True:
        # display board and prompt for user input of positions
        board.display_board()
        print("%s's turn" %game.get_turn())
        from_pos = input('Move from: ')
        to_pos = input('Move to: ')

        # execute the move
        game.make_move(from_pos, to_pos)

        # blank line before printing board for next turn
        print()

if __name__ == '__main__':
    main()
