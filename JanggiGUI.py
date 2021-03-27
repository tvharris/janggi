import JanggiGame
import pygame, os, sys

pygame.init()

# initialize the game
game = JanggiGame.JanggiGame()
board = game.get_board()

FPS = 30

# change BOARD_TARGET_HEIGHT to adjust the game resolution
# 1000 is native and sharpest
BOARD_TARGET_HEIGHT = 1000
FULL_WIDTH, FULL_HEIGHT = 900, 1000
SCALE_FACTOR = BOARD_TARGET_HEIGHT / FULL_HEIGHT
WIDTH, HEIGHT = round(SCALE_FACTOR * FULL_WIDTH), round(SCALE_FACTOR * FULL_HEIGHT)
ROWS, COLS = 10, 9

# height of screen space below board for displaying text
FULL_TEXT_BOX_SIZE = 50
TEXT_BOX_SIZE = round(SCALE_FACTOR * FULL_TEXT_BOX_SIZE)

# create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT + TEXT_BOX_SIZE))
pygame.display.set_caption('Janggi')  # window title

# define colors and font
FONT = pygame.font.Font(None, round(SCALE_FACTOR * 44))
RED = (200, 0, 0)
BLUE = (0, 0, 150)
GREEN = (0, 255, 0)
GREEN_TRANSP = (0, 255, 0, 50)
GREY = (200, 200, 200)
DARK_GREY = (100, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (230, 230, 0)

# load piece and board images as Surfaces
IMAGES = {}
image_dir = os.path.join(os.path.dirname(__file__), 'images')
for image in os.listdir(image_dir):
    image_name = image[:-4] + '_img'
    image_path = os.path.join(image_dir, image)
    if os.path.isfile(image_path):
        IMAGES[image_name] = pygame.image.load(image_path).convert_alpha()

# scale Surfaces
for surface_name, surface in IMAGES.items():
    scaled_surface = pygame.transform.smoothscale(surface,
                        (round(SCALE_FACTOR * surface.get_width()),
                         round(SCALE_FACTOR * surface.get_height())))
    IMAGES[surface_name] = scaled_surface

# create pass button
pass_button_x = SCALE_FACTOR * 406
pass_button_y = SCALE_FACTOR * 1005
pass_button_width = SCALE_FACTOR * 80
pass_button_height = SCALE_FACTOR * 40
pass_button = pygame.Rect(pass_button_x, pass_button_y, pass_button_width,
                          pass_button_height)
pass_button_text = FONT.render('Pass', True, WHITE)

def draw_game_state():
    """Displays text indicating whose turn it is or who won the game."""
    margin = round(SCALE_FACTOR * 10)
    text_xy = (margin, HEIGHT + margin)
    game_state = game.get_game_state()

    if game_state == 'UNFINISHED':
        if game.get_turn() == 'blue':
            text_surface = FONT.render("Blue player's turn", True, BLUE)
        else:
            text_surface = FONT.render("Red player's turn", True, RED)

    elif game_state == 'BLUE_WON':
        text_surface = FONT.render("Checkmate! Blue won!", True, BLUE)

    else:
        text_surface = FONT.render("Checkmate! Red won!", True, RED)

    screen.blit(text_surface, text_xy)

def draw_check():
    """Displays text indicating that a player is in check."""
    text_xy = (round(SCALE_FACTOR * (FULL_WIDTH - 120)),
               round(SCALE_FACTOR * (FULL_HEIGHT + 10)))

    # create filled rectangular background for text
    box_x = SCALE_FACTOR * 770
    box_y = SCALE_FACTOR * 1005
    box_width = SCALE_FACTOR * 125
    box_height = SCALE_FACTOR * 40
    text_box = pygame.Rect(box_x, box_y, box_width, box_height)

    # draw the rectangle and text
    if game.is_in_check(game.get_turn()):
        pygame.draw.rect(screen, YELLOW, text_box)
        text_surface = FONT.render("Check!", True, BLACK)
        screen.blit(text_surface, text_xy)

def draw_pass_button():
    """Displays the pass button."""
    text_xy = (pass_button_x + round(SCALE_FACTOR * 5),
    round(SCALE_FACTOR * (FULL_HEIGHT + 10)))

    pygame.draw.rect(screen, DARK_GREY, pass_button)
    screen.blit(pass_button_text, text_xy)

def position_to_xy(position):
    """Takes a position (str) and returns a tuple of x, y coordinates indicating
    where a piece should be drawn."""
    col = ord(position[0]) - ord('a')
    row = int(position[1:]) - 1
    x = col * WIDTH // COLS - round(SCALE_FACTOR * 10)
    y = row * HEIGHT // ROWS - round(SCALE_FACTOR * 3)
    return x, y

def xy_to_position(xy):
    """Takes a tuple of coordinates (x, y) and returns the position as a string."""
    col = xy[0] // (WIDTH // COLS)
    row = xy[1] // (HEIGHT // ROWS)
    col_str = chr(col + ord('a'))
    row_str = str(row + 1)
    return col_str + row_str

def id_to_img(piece_id):
    """Takes a piece_id and returns the Surface object for the piece's image."""
    surface_name = piece_id[:3] + '_img'
    return IMAGES[surface_name]

def draw_pieces():
    """Draws the pieces on the board according to the current state of the game."""
    for position, piece_id in board.get_board().items():
        if piece_id != '----':
            screen.blit(id_to_img(piece_id), position_to_xy(position))

def is_own_piece(piece_id):
    """Takes a piece_id and returns True if it belongs to the player whose turn
    it is, otherwise returns False."""
    pieces_dict = game.get_current_player().get_pieces()
    if piece_id in pieces_dict:
        return True
    return False

def id_to_allowed_destinations(piece_id, from_pos):
    """Takes a piece_id (str) and its position (str) and returns a list of
    positions (strings) that the piece is allowed to move to."""
    # get piece object
    piece = game.get_current_player().get_pieces()[piece_id]

    # get "allowed" moves, which include those that put or leave the player
    # in check
    allowed_moves = piece.get_allowed_moves()

    # allowed_destinations do not put or leave the player in check
    allowed_destinations = []

    # build allowed_destinations by excluding moves from allowed_moves that put
    # or leave the player in check
    # each "allowed" move is attempted and undone
    for position in allowed_moves.keys():
        captured_piece_id = board.get_occupation(position)
        if game.make_move(from_pos, position):
            game.next_turn()
            game.undo_move(from_pos, position, captured_piece_id)
            allowed_destinations.append(position)

    # return list of allowed destinations
    return allowed_destinations

def draw_allowed_destinations(allowed_destinations):
    """Takes a piece_id and draws filled, transparent circles at the positions
    that the piece is allowed to move to."""
    size = round(SCALE_FACTOR * 10)

    for position in allowed_destinations:
        xy = position_to_xy(position)
        xy_shifted = (xy[0] + round(SCALE_FACTOR * 60),
                      xy[1] + round(SCALE_FACTOR * 53))
        pygame.draw.circle(screen, GREEN, xy_shifted, size)

def highlight_selected(position):
    """Takes the position of a piece to be highlighted and draws a circle
    around it."""
    xy = position_to_xy(position)
    xy_shifted = (xy[0] + round(SCALE_FACTOR * 5), xy[1] - round(SCALE_FACTOR * 2))
    surface_dimensions = (round(SCALE_FACTOR * 110), round(SCALE_FACTOR * 110))
    circle_xy = tuple([0.5 * dim for dim in surface_dimensions])
    radius = surface_dimensions[0] // 2

    circle_surface = pygame.Surface(surface_dimensions, pygame.SRCALPHA)
    pygame.draw.circle(circle_surface, GREEN_TRANSP, circle_xy, radius)
    screen.blit(circle_surface, xy_shifted)

def main():
    """Runs the game with a GUI."""
    # set up and run game loop
    piece_selected = False
    running = True
    clock = pygame.time.Clock()  # use to set fps later
    while running:

        # allow close button to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # handle mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # enable pass button
                if pass_button.collidepoint(mouse_pos):
                    color = game.get_turn()
                    in_check = game.is_in_check(color)
                    if not in_check:
                        piece_selected = False
                        game.next_turn()

                # handle mouse clicks on board, including piece selection and
                # movement
                elif mouse_pos[1] < HEIGHT:  # clicked on board or piece
                    if not piece_selected:
                        from_xy = mouse_pos
                        from_pos = xy_to_position(from_xy)
                        selected_piece_id = board.get_occupation(from_pos)
                        if is_own_piece(selected_piece_id):
                            piece_selected = True

                            # get allowed destinations here so it only has to be
                            # done once when a piece is selected
                            allowed_destinations = id_to_allowed_destinations(
                                selected_piece_id, from_pos)

                    # piece is already selected
                    else:
                        to_xy = mouse_pos
                        to_pos = xy_to_position(to_xy)

                        # allow clicking same piece to unselect
                        piece_selected = False
                        if from_pos != to_pos:
                            game.make_move(from_pos, to_pos)

        # display the text area below the board
        screen.fill(GREY)  # background color
        draw_pass_button()  # clickable button for passing the turn
        draw_game_state()  # text indicating whose turn or who won

        # determine if player is in check and display text if so
        draw_check()

        # draw board and pieces
        screen.blit(IMAGES['board_img'], (0, 0))
        draw_pieces()

        if piece_selected:
            highlight_selected(from_pos)
            draw_allowed_destinations(allowed_destinations)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()