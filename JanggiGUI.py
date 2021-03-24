from JanggiGame import *
import pygame

game = JanggiGame()
board = game.get_board()

pygame.init()

fps = 30

width, height = 900, 1000
rows, cols = 10, 9
board_size = width//cols
screen = pygame.display.set_mode((width, height))  # create window
pygame.display.set_caption('Janggi')

board_img = pygame.image.load('images/board.png')  # returns a Surface
board_img.convert_alpha()  # per-pixel transparency
board_rect = board_img.get_rect()  # get Rect for storing coordinates
board_rect.center = width // 2, height // 2  # center the image

# load images
bca_img = pygame.image.load('images/blue_cannon.png')
bch_img = pygame.image.load('images/blue_chariot.png')
bel_img = pygame.image.load('images/blue_elephant.png')
bge_img = pygame.image.load('images/blue_general.png')
bgu_img = pygame.image.load('images/blue_guard.png')
bho_img = pygame.image.load('images/blue_horse.png')
bso_img = pygame.image.load('images/blue_soldier.png')
rca_img = pygame.image.load('images/red_cannon.png')
rch_img = pygame.image.load('images/red_chariot.png')
rel_img = pygame.image.load('images/red_elephant.png')
rge_img = pygame.image.load('images/red_general.png')
rgu_img = pygame.image.load('images/red_guard.png')
rho_img = pygame.image.load('images/red_horse.png')
rso_img = pygame.image.load('images/red_soldier.png')

def position_to_xy(position):
    """Takes a position (str) and returns a tuple of x, y coordinates indicating
    where a piece should be drawn."""
    col = ord(position[0]) - ord('a')
    row = int(position[1:]) - 1
    x = col * width // cols - 10
    y = row * height // rows - 3
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

# Alternative drawing method using rect for each piece
#bso_rect = bso_img.get_rect()
#bso_rect.center = 8 * width / cols + 50, 8 * height / rows + 50
#def draw_piece():
#screen.blit(bso_img, bso_rect)

def is_own_piece(piece_id):
    """Takes a piece_id and returns True if it belongs to the player whose turn
    it is."""
    pieces_dict = game.get_current_player().get_pieces()
    if piece_id in pieces_dict:
        return True
    return False

def id_to_allowed_destinations(piece_id):
    """Takes a piece_id and returns a list of positions (strings) that the piece
    is allowed to move to."""
    #    pieces_dict = game.get_current_player().get_pieces()
    #    if piece_id in pieces_dict:
    # get piece object
    piece = game.get_current_player().get_pieces()[piece_id]

    # return list of allowed destinations
    return piece.get_allowed_moves().keys()

def draw_allowed_destinations(piece_id):
    """Takes a piece_id and draws circles at the positions that the piece is
    allowed to move to."""
    rgb = (0, 255, 0)
    size = 10
    allowed_destinations = id_to_allowed_destinations(piece_id)

    for position in allowed_destinations:
        xy = position_to_xy(position)
        xy_shifted = (xy[0] + 60, xy[1] + 53)
        pygame.draw.circle(screen, rgb, xy_shifted, size)

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

    screen.fill((150,150,150))  # background color
    screen.blit(board_img, board_rect)  # draw the board
    draw_pieces()

    if piece_selected:
        draw_allowed_destinations(selected_piece_id)

    pygame.display.flip()  # update the display (#TODO could use display.update())

pygame.quit()
