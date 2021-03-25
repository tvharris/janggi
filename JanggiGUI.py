from JanggiGame import *
import pygame

game = JanggiGame()
board = game.get_board()

pygame.init()
fps = 30

# change board_target_height to adjust the game resolution
# 1000 is native and sharpest
board_target_height = 1000
full_width, full_height = 900, 1000
scale_factor = board_target_height / full_height
width, height = round(scale_factor * full_width), round(scale_factor * full_height)
rows, cols = 10, 9

# height of screen space below board for displaying text
full_text_box_size = 50
text_box_size = round(scale_factor * full_text_box_size)

# create the window
screen = pygame.display.set_mode((width, height + text_box_size))
pygame.display.set_caption('Janggi')  # window title

# load the image as a Surface
board_img = pygame.image.load('images/board.png').convert()
board_img = pygame.transform.smoothscale(board_img, (width, height))

# define colors and font
font = pygame.font.Font(None, round(scale_factor * 44))
red = (200, 0, 0)
blue = (0, 0, 150)
green = (0, 255, 0)
grey = (200, 200, 200)
black = (0, 0, 0)

# load images as Surfaces
bca_img = pygame.image.load('images/blue_cannon.png').convert_alpha()
bch_img = pygame.image.load('images/blue_chariot.png').convert_alpha()
bel_img = pygame.image.load('images/blue_elephant.png').convert_alpha()
bge_img = pygame.image.load('images/blue_general.png').convert_alpha()
bgu_img = pygame.image.load('images/blue_guard.png').convert_alpha()
bho_img = pygame.image.load('images/blue_horse.png').convert_alpha()
bso_img = pygame.image.load('images/blue_soldier.png').convert_alpha()
rca_img = pygame.image.load('images/red_cannon.png').convert_alpha()
rch_img = pygame.image.load('images/red_chariot.png').convert_alpha()
rel_img = pygame.image.load('images/red_elephant.png').convert_alpha()
rge_img = pygame.image.load('images/red_general.png').convert_alpha()
rgu_img = pygame.image.load('images/red_guard.png').convert_alpha()
rho_img = pygame.image.load('images/red_horse.png').convert_alpha()
rso_img = pygame.image.load('images/red_soldier.png').convert_alpha()

# scale Surfaces
bca_img = pygame.transform.smoothscale(bca_img, (round(scale_factor * bca_img.get_width()), round(scale_factor * bca_img.get_height())))
bch_img = pygame.transform.smoothscale(bch_img, (round(scale_factor * bch_img.get_width()), round(scale_factor * bch_img.get_height())))
bel_img = pygame.transform.smoothscale(bel_img, (round(scale_factor * bel_img.get_width()), round(scale_factor * bel_img.get_height())))
bge_img = pygame.transform.smoothscale(bge_img, (round(scale_factor * bge_img.get_width()), round(scale_factor * bge_img.get_height())))
bgu_img = pygame.transform.smoothscale(bgu_img, (round(scale_factor * bgu_img.get_width()), round(scale_factor * bgu_img.get_height())))
bho_img = pygame.transform.smoothscale(bho_img, (round(scale_factor * bho_img.get_width()), round(scale_factor * bho_img.get_height())))
bso_img = pygame.transform.smoothscale(bso_img, (round(scale_factor * bso_img.get_width()), round(scale_factor * bso_img.get_height())))
rca_img = pygame.transform.smoothscale(rca_img, (round(scale_factor * rca_img.get_width()), round(scale_factor * rca_img.get_height())))
rch_img = pygame.transform.smoothscale(rch_img, (round(scale_factor * rch_img.get_width()), round(scale_factor * rch_img.get_height())))
rel_img = pygame.transform.smoothscale(rel_img, (round(scale_factor * rel_img.get_width()), round(scale_factor * rel_img.get_height())))
rge_img = pygame.transform.smoothscale(rge_img, (round(scale_factor * rge_img.get_width()), round(scale_factor * rge_img.get_height())))
rgu_img = pygame.transform.smoothscale(rgu_img, (round(scale_factor * rgu_img.get_width()), round(scale_factor * rgu_img.get_height())))
rho_img = pygame.transform.smoothscale(rho_img, (round(scale_factor * rho_img.get_width()), round(scale_factor * rho_img.get_height())))
rso_img = pygame.transform.smoothscale(rso_img, (round(scale_factor * rso_img.get_width()), round(scale_factor * rso_img.get_height())))

def draw_game_state():
    """Displays text indicating whose turn it is or who won the game."""
    margin = round(scale_factor * 10)
    text_xy = (margin, height + margin)
    game_state = game.get_game_state()

    if game_state == 'UNFINISHED':
        if game.get_turn() == 'blue':
            text_surface = font.render("Blue player's turn", True, blue)
        else:
            text_surface = font.render("Red player's turn", True, red)

    elif game_state == 'BLUE_WON':
        text_surface = font.render("Checkmate! Blue player won!", True, blue)

    else:
        text_surface = font.render("Checkmate! Red player won!", True, red)

    screen.blit(text_surface, text_xy)

def draw_check():
    """Displays text indicating that a player is in check."""
    text_xy = (round(scale_factor * (full_width - 120)),
               round(scale_factor * (full_height + 10)))

    if game.is_in_check(game.get_turn()):
        text_surface = font.render("Check!", True, black)

        screen.blit(text_surface, text_xy)

def position_to_xy(position):
    """Takes a position (str) and returns a tuple of x, y coordinates indicating
    where a piece should be drawn."""
    col = ord(position[0]) - ord('a')
    row = int(position[1:]) - 1
    x = col * width // cols - round(scale_factor * 10)
    y = row * height // rows - round(scale_factor * 3)
    return x, y

def xy_to_position(xy):
    """Takes a tuple of coordinates (x, y) and returns the position as a string."""
    col = xy[0] // (width // cols)
    row = xy[1] // (height // rows)
    col_str = chr(col + ord('a'))
    row_str = str(row + 1)
    return col_str + row_str

def id_to_img(piece_id):
    """Takes a piece_id and returns the Surface object for the piece's image."""
    img_string = piece_id[:3] + '_img'
    return globals()[img_string]

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

def id_to_allowed_destinations(piece_id):
    """Takes a piece_id and returns a list of positions (strings) that the piece
    is 'allowed' to move to. These 'allowed' destinations for pieces other than
    generals will include those that put or leave the general in check, which
    are actually not allowed."""
    # get piece object
    piece = game.get_current_player().get_pieces()[piece_id]

    # return list of allowed destinations
    return piece.get_allowed_moves().keys()

def draw_allowed_destinations(piece_id):
    """Takes a piece_id and draws circles at the positions that the piece is
    allowed to move to."""
    size = 10
    allowed_destinations = id_to_allowed_destinations(piece_id)

    for position in allowed_destinations:
        xy = position_to_xy(position)
        xy_shifted = (xy[0] + round(scale_factor * 60), xy[1] + round(scale_factor * 53))
        pygame.draw.circle(screen, green, xy_shifted, size)

# game loop
piece_selected = False
running = True
clock = pygame.time.Clock()  # use to set fps later
while running:
    clock.tick(fps)

    # allow close button to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not piece_selected:
                from_xy = pygame.mouse.get_pos()
                from_pos = xy_to_position(from_xy)
                selected_piece_id = board.get_occupation(from_pos)
                if is_own_piece(selected_piece_id):
                    piece_selected = True
            else:
                to_xy = pygame.mouse.get_pos()
                to_pos = xy_to_position(to_xy)
                piece_selected = False
                game.make_move(from_pos, to_pos)

    screen.fill(grey)  # text background
    draw_game_state()  # display text indicating whose turn or who won
    draw_check()  # display text indicating that a player is in check

    screen.blit(board_img, (0, 0))  # draw the board
    draw_pieces()

    if piece_selected:
        draw_allowed_destinations(selected_piece_id)

    pygame.display.flip()  # update the display (#TODO could use display.update())

pygame.quit()
