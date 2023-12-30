import pygame
from classes import ValidWords, Solution

# constants
WIDTH = 500
HEIGHT = 600
BOX_SIZE = 72

MARGIN = 50  # window margin
BOX_MARGIN = 10  # margin between boxes

WHITE = (255, 255, 255)
GRAY = (133, 146, 158)
BLACK = (0, 0, 0)
GREEN = (12, 191, 29)
YELLOW = (255, 191, 0)

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

    # solution
    solution = Solution()
    guessword = solution.guessword
    print(guessword)

    # loop
    showing = True
    while showing:
        screen.fill(WHITE)

        y = MARGIN
        for i in range(TRIES):
            x = MARGIN
            if i < len(guessed_words):
                word = guessed_words[i]
                colors = solution.get_colors(word)
            for j in range(WORD_LEN):
                # display boxes
                box = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)
                pygame.draw.rect(screen, BLACK, box, width=2, border_radius=3)
                center_value = (x + BOX_SIZE//2, y + BOX_SIZE//2)

                # display <guessed_words> and <input>
                if i < len(guessed_words):
                    color = colors[j]
                    pygame.draw.rect(screen, color, box, border_radius=3)
                    letter = FONT.render(word[j], False, WHITE)
                    surface = letter.get_rect(center=center_value)
                    screen.blit(letter, surface)
                elif i == len(guessed_words) and j < len(input):
                    letter = FONT.render(input[j], False, BLACK)
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
                    if ValidWords().is_valid(input):
                        guessed_words.append(input)
                        input = ''
                # handling backspace
                elif event.key == pygame.K_BACKSPACE:
                    if len(input) > 0:
                        input = input[:-1]
                # get input
                elif len(input) < WORD_LEN:
                    letter = str(event.unicode.upper())
                    if letter.isalpha():
                        input += event.unicode.upper()

        pygame.display.flip()


if __name__ == '__main__':
    main()
