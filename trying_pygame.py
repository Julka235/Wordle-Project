import pygame

# sizes
WIDTH = 500
HEIGHT = 600
BOX_SIZE = 72

# margins
BIG_MARGIN = 50  # window margin
BOX_MARGIN = 10  # margin between boxes

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# constant numbers
TRIES = 6
WORD_LEN = 5

# initialize pygame
pygame.init()
pygame.display.set_caption('Wordle')

# create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

show = True
while show:
    screen.fill(WHITE)

    # display boxes
    y = BIG_MARGIN
    for i in range(TRIES):
        x = BIG_MARGIN
        for j in range(WORD_LEN):
            box = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)
            pygame.draw.rect(screen, BLACK, box, width=3)
            x += BOX_SIZE + BOX_MARGIN
        y += BOX_SIZE + BOX_MARGIN

    # update the screen
    pygame.display.flip()

    # close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            show = False
