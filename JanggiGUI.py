import pygame
pygame.init()

fps = 60

width, height = 600, 640
rows, cols = 10, 9
board_size = width//cols
screen = pygame.display.set_mode((width, height))  # create window
pygame.display.set_caption('Janggi')

board = pygame.image.load('images/board.png')  # returns a Surface
board.convert_alpha()  # per-pixel transparency
board_rect = board.get_rect()  # get Rect for storing coordinates
board_rect.center = width // 2, height // 2  # center the image

running = True
clock = pygame.time.Clock()  # use to set fps later
while running:
    clock.tick(fps)

    # allow close button to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        pass

    screen.fill((150,150,150))  # background color
    screen.blit(board, board_rect)  # draw the image
    pygame.display.flip()  # update the display

pygame.quit()

if __name__ == '__main__':
    main()
