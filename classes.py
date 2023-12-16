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
        init class, write words to <self._wordlist> from file <path>
        and calculate length
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


class GuesswordsDatabase(Database):
    '''
    class Guesswords inherits from class Database.
    Contains the same attributes as Database
    '''
    def __init__(self) -> None:
        super().__init__('guesswords.txt')

    def generate_guessword(self) -> str:
        '''
        Generates random guessword
        '''
        guessword_index = randint(0, super().length - 1)
        return super().wordlist[guessword_index]


class ValidWords(Database):
    '''
    class ValidWords inherits from class Database.
    Contains the same attributes as Database
    '''
    def __init__(self) -> None:
        super().__init__('valid_words.txt')

    def binary_search(self, word: str) -> bool:
        '''
        Uses binary search algorithm to verify whether
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
