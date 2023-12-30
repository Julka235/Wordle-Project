from random import choice


class Database:
    '''
    class Database. Contains attributes:

    :param wordlist: list of words in database
    :type wordlist: list of str

    :param length: number of words in database
    :type length: int
    '''
    def __init__(self, path: str) -> None:
        '''
        initializes class, writes words to <self._wordlist> from file <path>
        and calculates length
        '''
        try:
            self._wordlist = []
            with open(path, 'r') as file_handle:
                for line in file_handle:
                    line = line.rstrip()
                    if len(line) == 5 and line.isalpha():
                        self._wordlist.append(line.upper())
            self._wordlist.sort()
            self._length = len(self._wordlist)
        except FileNotFoundError:
            raise FileNotFoundError(f'File {path} not found')

    @property
    def wordlist(self) -> list:
        return self._wordlist

    @property
    def length(self) -> int:
        return self._length


class Guesswords(Database):
    '''
    class Guesswords inherits from class Database.
    Contains the same attributes as Database
    '''
    def __init__(self) -> None:
        super().__init__('txt_files/guesswords.txt')

    def generate_guessword(self) -> str:
        '''
        Generates and returns random guessword
        '''
        return choice(super().wordlist)


class ValidWords(Database):
    '''
    class ValidWords inherits from class Database.
    Contains the same attributes as Database
    '''
    def __init__(self) -> None:
        super().__init__('txt_files/valid_words.txt')

    def binary_search(self, word: str) -> bool:
        '''
        uses binary search algorithm to verify whether
        <word> is in ValidWords' <wordlist>
        '''
        word = word.upper()
        begin = 0
        end = super().length - 1
        while begin < end:
            shoot = (begin + end) / 2
            shoot = int(shoot)
            if super().wordlist[shoot] >= word:
                end = shoot
            else:
                begin = shoot + 1
        return super().wordlist[begin] == word

    def is_valid(self, word: str) -> bool:
        '''
        returns True if <word> is in ValidWords' <wordlist>
        '''
        if not word or not isinstance(word, str) or len(word) != 5:
            return False
        return self.binary_search(word)


class Solution:
    '''
    class Solution. Contains attribute:

    :param guessword: selected password for the game
    :type guessword: str
    '''
    def __init__(self) -> None:
        '''
        initializes class and chooses password for the game
        '''
        self._guessword = Guesswords().generate_guessword()

    @property
    def guessword(self) -> str:
        return self._guessword

    def get_colors(self, word: str) -> list or bool:
        '''
        returns five-element list with colors for <word>
        GREEN if letter is in the same place in <guessword>
        YELLOW if letter is not in the same place in <guessword>
        GRAY if letter is not in <guessword> or was earlier flagged
        as green or yellow

        case where two same letters appear in <word> or/and <guessword>
        is treated the same way as in classic Wordle

        returns False if <word> is invalid
        '''
        word = word.upper()

        if not ValidWords().is_valid(word):
            return False

        GREEN = (12, 191, 29)
        YELLOW = (255, 191, 0)
        GRAY = (133, 146, 158)
        guessword = self._guessword

        resolution_type = True
        for letter in word:
            if word.count(letter) == 2 and guessword.count(letter) == 1:
                resolution_type = False

        colors = []

        if resolution_type:
            for i in range(5):
                letter = word[i]
                if letter == guessword[i] and letter not in word[:i]:
                    colors.append(GREEN)
                elif letter == guessword[i] and guessword.count(letter) == 2:
                    colors.append(GREEN)
                elif letter in guessword and letter not in word[:i]:
                    colors.append(YELLOW)
                elif letter in guessword and guessword.count(letter) == 2:
                    colors.append(YELLOW)
                else:
                    colors.append(GRAY)
        else:
            colors = [GRAY, GRAY, GRAY, GRAY, GRAY]
            used_letters = []

            for i in range(5):
                letter = word[i]
                con = word.count(letter) == 2 and guessword.count(letter) == 1
                if letter == guessword[i]:
                    colors[i] = GREEN
                    if con:
                        used_letters.append(letter)

            for i in range(5):
                letter = word[i]
                if colors[i] == GREEN:
                    pass
                elif letter in used_letters:
                    pass
                elif letter == guessword[i] and guessword.count(letter) == 2:
                    colors[i] = GREEN
                elif letter in guessword and letter not in word[:i]:
                    colors[i] = YELLOW
                elif letter in guessword and guessword.count(letter) == 2:
                    colors[i] = YELLOW
        return colors
