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
            self._length = len(self._wordlist)
        except FileNotFoundError:
            raise FileNotFoundError(f'File {path} not found')

    @property
    def wordlist(self) -> list:
        return self._wordlist

    @property
    def length(self) -> int:
        return self._length
