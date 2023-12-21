import pygame

# size of the displayed window
WIDTH = 500
HEIGHT = 500

# init pygame
pygame.init()
pygame.display.set_caption('Wordle')

# create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

show = True
while show:
    # update the screen
    pygame.display.flip()

    # close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            show = False
