import pygame
from classes import ValidWords, Solution

# constants
WIDTH = 500
HEIGHT = 700
BOX_SIZE = 53
KEY_SIZE = 36

TOP_MARGIN = 50
MARGIN = 100  # window margin
BOX_MARGIN = 8  # margin between boxes
KEY_MARGIN = 6
WINDOW_KEY_MARGIN = 40


WHITE = (255, 255, 255)
GRAY = (133, 146, 158)
DARK = (52, 73, 94)
GREEN = (12, 191, 29)
YELLOW = (255, 191, 0)

TRIES = 6
WORD_LEN = 5

FIRST_LETTERS = 'QWERTYUIOP'
SECOND_LETTERS = 'ASDFGHJKL'

# Initialize pygame and create <screen>
pygame.init()
pygame.display.set_caption('Wordle')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont('free sans bold', BOX_SIZE)
SOLUTION_FONT = pygame.font.SysFont('free sans bold', 35)
KEY_FONT = pygame.font.SysFont('free sans bold', 25)


def display_text(character, color, center_value, font):
    if font == 'normal':
        letter = FONT.render(character, False, color)
    else:
        letter = SOLUTION_FONT.render(character, False, color)
    surface = letter.get_rect(center=center_value)
    screen.blit(letter, surface)


class Button:
    def __init__(self, pos: tuple, measurements: tuple, sign: str) -> None:
        x, y = pos
        width, height = measurements
        center_value = (x + width // 2, y + height // 2)
        self.sign = KEY_FONT.render(sign, False, WHITE)
        self.surface = self.sign.get_rect(center=center_value)
        self.area = pygame.Rect(x, y, 40, 40)
        self.width = width
        self.height = height
        self.letter = sign

    def display(self):
        x, y = pygame.mouse.get_pos()
        if self.area.x <= x <= self.area.x + self.width \
           and self.area.y <= y <= self.area.y + self.height:
            pygame.draw.rect(screen, DARK, self.area, border_radius=2)
        else:
            pygame.draw.rect(screen, GRAY, self.area, border_radius=2)
        screen.blit(self.sign, self.surface)


def main():
    # variables
    input = ''
    guessed_words = []
    game_status = False

    # solution
    solution = Solution()
    guessword = solution.guessword
    print(guessword)

    # loop
    showing = True
    while showing:
        screen.fill(WHITE)

        y = TOP_MARGIN
        for i in range(TRIES):
            x = MARGIN
            if i < len(guessed_words):
                word = guessed_words[i]
                colors = solution.get_colors(word)
            for j in range(WORD_LEN):
                # display boxes
                box = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)
                pygame.draw.rect(screen, DARK, box, width=2, border_radius=3)
                center_value = (x + BOX_SIZE//2, y + BOX_SIZE//2)

                # display <guessed_words> and <input>
                if i < len(guessed_words):
                    color = colors[j]
                    pygame.draw.rect(screen, color, box, border_radius=3)
                    display_text(word[j], WHITE, center_value, 'normal')
                elif i == len(guessed_words) and j < len(input):
                    display_text(input[j], DARK, center_value, 'normal')

                x += BOX_SIZE + BOX_MARGIN
            y += BOX_SIZE + BOX_MARGIN

        # keyboard's first row
        FIRST_ROW = []
        y += KEY_SIZE
        x = WINDOW_KEY_MARGIN
        for letter in FIRST_LETTERS:
            button = Button((x, y), (KEY_SIZE, KEY_SIZE), letter)
            FIRST_ROW.append(button)
            x += KEY_SIZE + KEY_MARGIN
        for button in FIRST_ROW:
            button.display()

        # keyboard's second row
        SECOND_ROW = []
        y += KEY_SIZE + KEY_MARGIN
        x = WINDOW_KEY_MARGIN + KEY_SIZE // 2
        for letter in SECOND_LETTERS:
            button = Button((x, y), (KEY_SIZE, KEY_SIZE), letter)
            SECOND_ROW.append(button)
            x += KEY_SIZE + KEY_MARGIN
        for button in SECOND_ROW:
            button.display()

        # keyboard's last row

        # display answer if failed to guess
        if len(guessed_words) == TRIES and guessed_words[TRIES-1] != guessword:
            game_status = True
            center_value = (250, 550)
            display_text(guessword, DARK, center_value, 'solution')

        for event in pygame.event.get():
            # close the window
            if event.type == pygame.QUIT:
                showing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in FIRST_ROW:
                    if button.area.collidepoint(event.pos):
                        if len(input) < WORD_LEN:
                            input += button.letter
                for button in SECOND_ROW:
                    if button.area.collidepoint(event.pos):
                        if len(input) < WORD_LEN:
                            input += button.letter

            elif event.type == pygame.KEYDOWN:
                # press enter to enter guess
                if event.key == pygame.K_RETURN:
                    if ValidWords().is_valid(input):
                        guessed_words.append(input)
                        if input == guessword:
                            game_status = True
                        input = ''
                # handling backspace
                elif event.key == pygame.K_BACKSPACE:
                    if len(input) > 0:
                        input = input[:-1]
                # get input
                elif len(input) < WORD_LEN and not game_status:
                    letter = str(event.unicode.upper())
                    if letter.isalpha():
                        input += event.unicode.upper()

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
