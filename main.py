import pygame
from classes import ValidWords

# constants
WIDTH = 500
HEIGHT = 600
BOX_SIZE = 72

MARGIN = 50  # window margin
BOX_MARGIN = 10  # margin between boxes

WHITE = (255, 255, 255)
GRAY = (133, 146, 158)
BLACK = (0, 0, 0)

TRIES = 6
WORD_LEN = 5


def main():
    # Initialize pygame and create <screen>
    pygame.init()
    pygame.display.set_caption('Wordle')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    FONT = pygame.font.SysFont('free sans bold', BOX_SIZE)

    # variables
    input = ''
    guessed_words = []

    # loop
    showing = True
    while showing:
        screen.fill(WHITE)

        y = MARGIN
        for i in range(TRIES):
            x = MARGIN
            for j in range(WORD_LEN):
                # display boxes
                box = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)
                pygame.draw.rect(screen, BLACK, box, width=2, border_radius=3)

                # display guesses
                if i < len(guessed_words):
                    pygame.draw.rect(screen, GRAY, box, border_radius=3)
                    center_value = (x + BOX_SIZE//2, y + BOX_SIZE//2)
                    letter = FONT.render(guessed_words[i][j], False, WHITE)
                    surface = letter.get_rect(center=center_value)
                    screen.blit(letter, surface)

                x += BOX_SIZE + BOX_MARGIN
            y += BOX_SIZE + BOX_MARGIN

        for event in pygame.event.get():
            # close the window
            if event.type == pygame.QUIT:
                showing = False

            elif event.type == pygame.KEYDOWN:
                # press enter to enter guess
                if event.key == pygame.K_RETURN:
                    print('yay')
                    if ValidWords().is_valid(input):
                        guessed_words.append(input)
                        input = ''

                # get input
                elif len(input) < 5:
                    letter = str(event.unicode.upper())
                    if letter.isalpha():
                        input += event.unicode.upper()
                    print(input)

        # update the screen
        pygame.display.flip()


if __name__ == '__main__':
    main()
