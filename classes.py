from random import randint


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
        initialises class, writes words to <self._wordlist> from file <path>
        and calculates length
        '''
        try:
            self._wordlist = []
            with open(path, 'r') as file_handle:
                for line in file_handle:
                    line = line.rstrip()
                    if len(line) == 5 and line.isalpha():
                        self._wordlist.append(line.lower())
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
        guessword_index = randint(0, super().length - 1)
        return super().wordlist[guessword_index]


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
        initialises class and chooses password for the game
        '''
        self._guessword = Guesswords().generate_guessword()

    @property
    def guessword(self) -> str:
        return self._guessword

    def get_clues(self, word: str) -> list or bool:
        '''
        returns five-element list with clues for <word> compared to <guessword>
        'green' if letter is in the same place in <guessword>
        'yellow' if letter is not in the same place in <guessword>
        'gray' if letter is not in <guessword>
        returns False if <word> is invalid
        returns True if <word> is equal to <guessword>
        '''
        if not ValidWords().is_valid(word):
            return False

        if word == self._guessword:
            return True

        clues = []
        guessword = self._guessword
        for index in range(0, 5):
            letter = word[index]
            if letter == guessword[index] and letter not in word[0:index]:
                clues.append('green')
            elif letter in guessword and letter not in word[0:index]:
                clues.append('yellow')
            else:
                clues.append('gray')
        return clues
