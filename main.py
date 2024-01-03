import pygame
from classes import ValidWords, Solution

# CONSTANTS
WIDTH = 500
HEIGHT = 650
BOX_SIZE = 53
KEY_SIZE = 40

TOP_MARGIN = 50
MARGIN = 100  # window margin
BOX_MARGIN = 8  # margin between boxes
KEY_MARGIN = 3
WINDOW_KEY_MARGIN = 40

WHITE = (255, 255, 255)
GRAY = (133, 146, 158)
DARK = (52, 73, 94)
GREEN = (12, 191, 29)
YELLOW = (255, 191, 0)

TRIES = 6  # number of tries
WORD_LEN = 5

FIRST_LETTERS = 'QWERTYUIOP'  # first keyboard row letters
SECOND_LETTERS = 'ASDFGHJKL'  # second keyboard row letters
LAST_LETTERS = 'ZXCVBNM'  # last keyboard row letters

# dict storing what colors should be each letter on the keyboard
keyboard_colors = {}

# Initialize pygame and create <screen>
pygame.init()
pygame.display.set_caption('Wordle')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Initialize fonts
FONT = pygame.font.SysFont('free sans bold', BOX_SIZE)
SOLUTION_FONT = pygame.font.SysFont('free sans bold', 35)
KEY_FONT = pygame.font.SysFont('free sans bold', 25)


def display_text(character, color, center_value, font) -> None:
    '''
        displays <character> on the screen
        in a box colored <color>
        and chooses font based on condition with <font>
    '''
    if font == 'normal':
        letter = FONT.render(character, False, color)
    else:
        letter = SOLUTION_FONT.render(character, False, color)
    surface = letter.get_rect(center=center_value)
    screen.blit(letter, surface)


def handle_keyboard_colors(input: str, colors: tuple) -> None:
    '''
        updates <keyboard_colors>
    '''
    for i in range(5):
        if colors[i] == GRAY:
            colors[i] = DARK

        current_color = keyboard_colors.get(input[i], DARK)
        if current_color == DARK or current_color == GRAY:
            keyboard_colors[input[i]] = colors[i]
        elif current_color == YELLOW and colors[i] == GREEN:
            keyboard_colors[input[i]] = colors[i]


def handle_enter(input: str, guessed_words: list, solution: Solution) -> tuple:
    '''
        handles case when enter is pressed on keyboard:
        updates <guessed_words>, <game_status and clears <input>
        if <input> was valid
    '''
    if ValidWords().is_valid(input):
        guessed_words.append(input)
        handle_keyboard_colors(input, solution.get_colors(input))
        if input == solution.guessword:
            return ('', guessed_words, True)
        else:
            return ('', guessed_words, False)
    else:
        return (input, guessed_words, False)


def get_keyboard_row(letters: str, x: int, y: int):
    '''
        returns row of keyboard buttons
    '''
    ROW = []
    for letter in letters:
        button = Button((x, y), (KEY_SIZE, KEY_SIZE), letter)
        ROW.append(button)
        x += KEY_SIZE + KEY_MARGIN
    return ROW


def display_keyboard_row(ROW):
    '''
        displayes keyboard row on the screen
    '''
    for button in ROW:
        button.display(keyboard_colors.get(button.letter, GRAY))


class Button:
    '''
    class Button. Contains attributes:

    :param text: rendered given text to <KEY_FONT>
    :param surface: Rect containing <text>
    :param area: Rect containing area of the button
    :param width: width of the button
    :param height: height of the button
    :param letter: text displaying on the button as str
    '''
    def __init__(self, pos: tuple, measurements: tuple, text: str) -> None:
        '''
            Initializes class
        '''
        x, y = pos
        width, height = measurements
        center_value = (x + width // 2, y + height // 2)
        self.text = KEY_FONT.render(text, False, WHITE)
        self.surface = self.text.get_rect(center=center_value)
        self.area = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height
        self.letter = text

    def display(self, color=GRAY):
        '''
            displays the button on the screen
        '''
        x, y = pygame.mouse.get_pos()
        if color == GRAY:
            if self.area.x <= x <= self.area.x + self.width \
               and self.area.y <= y <= self.area.y + self.height:
                pygame.draw.rect(screen, DARK, self.area, border_radius=2)
            else:
                pygame.draw.rect(screen, GRAY, self.area, border_radius=2)
        else:
            pygame.draw.rect(screen, color, self.area, border_radius=2)
        screen.blit(self.text, self.surface)


def main():
    # variables
    input = ''
    guessed_words = []
    game_status = False  # not won

    # solution
    solution = Solution()
    guessword = solution.guessword

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
        y += KEY_SIZE
        x = WINDOW_KEY_MARGIN
        FIRST_ROW = get_keyboard_row(FIRST_LETTERS, x, y)
        display_keyboard_row(FIRST_ROW)

        # keyboard's second row
        y += KEY_SIZE + KEY_MARGIN
        x = WINDOW_KEY_MARGIN + KEY_SIZE // 2
        SECOND_ROW = get_keyboard_row(SECOND_LETTERS, x, y)
        display_keyboard_row(SECOND_ROW)

        # delete button
        y += KEY_SIZE + KEY_MARGIN
        x = WINDOW_KEY_MARGIN
        delete_button = Button((x, y), (KEY_SIZE, KEY_SIZE), '<-')
        delete_button.display()
        # keyboard's last row of letters
        x += KEY_SIZE + KEY_MARGIN
        LAST_ROW = get_keyboard_row(LAST_LETTERS, x, y)
        display_keyboard_row(LAST_ROW)
        # display enter
        x += len(LAST_ROW) * (KEY_SIZE + KEY_MARGIN)
        enter_button = Button((x, y), (KEY_SIZE*2, KEY_SIZE), 'enter')
        enter_button.display()

        # display answer if failed to guess
        if len(guessed_words) == TRIES and guessed_words[TRIES-1] != guessword:
            game_status = True
            center_value = (250, 620)
            display_text(guessword, DARK, center_value, 'solution')

        for event in pygame.event.get():
            # close the window
            if event.type == pygame.QUIT:
                showing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                KEYBOARD = FIRST_ROW + SECOND_ROW + LAST_ROW
                for button in KEYBOARD:
                    if button.area.collidepoint(event.pos):
                        if len(input) < WORD_LEN:
                            input += button.letter
                if delete_button.area.collidepoint(event.pos):
                    if len(input) > 0:
                        input = input[:-1]
                if enter_button.area.collidepoint(event.pos):
                    temp = handle_enter(input, guessed_words, solution)
                    input, guessed_words, game_status = temp

            elif event.type == pygame.KEYDOWN:
                # press enter to enter guess
                if event.key == pygame.K_RETURN:
                    temp = handle_enter(input, guessed_words, solution)
                    input, guessed_words, game_status = temp
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
