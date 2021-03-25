from JanggiGame import *
import pygame
import os

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

# define colors and font
font = pygame.font.Font(None, round(scale_factor * 44))
red = (200, 0, 0)
blue = (0, 0, 150)
green = (0, 255, 0)
grey = (200, 200, 200)
dark_grey = (100, 100, 100)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (230, 230, 0)

# load piece and board images as Surfaces
images = {}
image_dir = 'images/'
for image in os.listdir(image_dir):
    surface_name = image[:-4] + '_img'
    if os.path.isfile(image_dir + image):
        images[surface_name] = pygame.image.load(image_dir + image).convert_alpha()

# scale Surfaces
for surface_name, surface in images.items():
    scaled_surface = pygame.transform.smoothscale(surface,
                        (round(scale_factor * surface.get_width()),
                         round(scale_factor * surface.get_height())))
    images[surface_name] = scaled_surface

# create pass button
pass_button_x = scale_factor * 406
pass_button_y = scale_factor * 1005
pass_button_width = scale_factor * 80
pass_button_height = scale_factor * 40
pass_button = pygame.Rect(pass_button_x, pass_button_y, pass_button_width, pass_button_height)
pass_button_text = font.render('Pass', True, white)

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
        text_surface = font.render("Checkmate! Blue won!", True, blue)

    else:
        text_surface = font.render("Checkmate! Red won!", True, red)

    screen.blit(text_surface, text_xy)

def draw_check():
    """Displays text indicating that a player is in check."""
    text_xy = (round(scale_factor * (full_width - 120)),
               round(scale_factor * (full_height + 10)))

    # create filled rectangular background for text
    box_x = scale_factor * 770
    box_y = scale_factor * 1005
    box_width = scale_factor * 125
    box_height = scale_factor * 40
    text_box = pygame.Rect(box_x, box_y, box_width, box_height)

    # draw the rectangle and text
    if game.is_in_check(game.get_turn()):
        pygame.draw.rect(screen, yellow, text_box)
        text_surface = font.render("Check!", True, black)
        screen.blit(text_surface, text_xy)

def draw_pass_button():
    """Displays the pass button."""
    text_xy = (pass_button_x + round(scale_factor * 5),
    round(scale_factor * (full_height + 10)))

    pygame.draw.rect(screen, dark_grey, pass_button)
    screen.blit(pass_button_text, text_xy)


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
    surface_name = piece_id[:3] + '_img'
    return images[surface_name]

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
    is allowed to move to."""
    # get piece object
    piece = game.get_current_player().get_pieces()[piece_id]

    # get "allowed" moves, which include those that put or leave the player
    # in check
    allowed_moves = piece.get_allowed_moves()

    # allowed_destinations are those that are truly legal
    allowed_destinations = []

    # build allowed_destinations by excluding moves from allowed_moves that put
    # or leave the player in check
    # each "allowed" move is attempted and undone
    for position in allowed_moves.keys():
        captured_piece_id = board.get_occupation(position)
        if captured_piece_id == '----':  # no capture
            if game.make_move(from_pos, position):
                game.next_turn()  # because make_move changes the turn
                game.undo_move(from_pos, position, None)
                allowed_destinations.append(position)
        else:
            if game.make_move(from_pos, position):
                game.next_turn()
                game.undo_move(from_pos, position, captured_piece_id)
                allowed_destinations.append(position)

    # return list of allowed destinations
    return allowed_destinations

def draw_allowed_destinations(allowed_destinations):
    """Takes a piece_id and draws circles at the positions that the piece is
    allowed to move to."""
    size = round(scale_factor * 10)

    for position in allowed_destinations:
        xy = position_to_xy(position)
        xy_shifted = (xy[0] + round(scale_factor * 60),
                      xy[1] + round(scale_factor * 53))
        pygame.draw.circle(screen, green, xy_shifted, size)

def highlight_selected(position):
    """Takes the position of a piece to be highlighted and draws a circle
    around it."""
    xy = position_to_xy(position)
    xy_shifted = (xy[0] + round(scale_factor * 60), xy[1] + round(scale_factor * 53))
    size = round(scale_factor * 55)
    thickness = round(scale_factor * 3)
    pygame.draw.circle(screen, green, xy_shifted, size, thickness)

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
            mouse_pos = pygame.mouse.get_pos()

            if pass_button.collidepoint(mouse_pos):
                color = game.get_turn()
                in_check = game.is_in_check(color)
                if not in_check:
                    piece_selected = False
                    game.next_turn()

            elif mouse_pos[1] < height:
                if not piece_selected:
                    from_xy = mouse_pos
                    from_pos = xy_to_position(from_xy)
                    selected_piece_id = board.get_occupation(from_pos)
                    if is_own_piece(selected_piece_id):
                        piece_selected = True

                        # get allowed destinations here so it only has to be
                        # done once when a piece is selected
                        allowed_destinations = id_to_allowed_destinations(selected_piece_id)
                else:
                    to_xy = mouse_pos
                    to_pos = xy_to_position(to_xy)
                    piece_selected = False
                    if from_pos != to_pos:
                        game.make_move(from_pos, to_pos)

    screen.fill(grey)  # text background
    draw_pass_button()
    draw_game_state()  # display text indicating whose turn or who won

    # determine if player is in check and display text if so
    draw_check()

    screen.blit(images['board_img'], (0, 0))  # draw the board
    draw_pieces()

    if piece_selected:
        highlight_selected(from_pos)
        draw_allowed_destinations(allowed_destinations)

    pygame.display.flip()  # update the display (#TODO could use display.update())

pygame.quit()
