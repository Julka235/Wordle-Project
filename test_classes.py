from classes import Database, GuesswordsDatabase, ValidWords
import pytest


# test class Database

def test_create_database():
    '''
    tests init, getting words containng numbers,
    uppercase or having more or less than 5 letters
    '''
    database = Database('database_to_test.txt')
    wordlist = ['brand', 'crime', 'pouty']
    assert database.length == 3
    assert database.wordlist == wordlist


def test_create_database_incorrect_path():
    with pytest.raises(FileNotFoundError) as excinfo:
        Database('nonexistent_file.txt')
    assert str(excinfo.value) == 'File nonexistent_file.txt not found'


# test class GuesswordsDatabase

def test_create_guesswords():
    guesswords = GuesswordsDatabase()
    assert guesswords.length == 2315


def test_generate_guessword(monkeypatch):
    def return_zero(f, t):
        return 0
    monkeypatch.setattr('classes.randint', return_zero)
    guesswords = GuesswordsDatabase()
    assert guesswords.generate_guessword() == 'aback'


# test class ValidWords

def test_create_valid_words():
    valid_words = ValidWords()
    assert valid_words.length == 14839


def test_binary_search_word_exists():
    valid_words = ValidWords()
    assert valid_words.binary_search('abaca') is True


def test_binary_search_word_nonexistent():
    valid_words = ValidWords()
    assert valid_words.binary_search('caleb') is False


def test_binary_search_first_word():
    valid_words = ValidWords()
    assert valid_words.binary_search('aahed') is True


def test_binary_search_last_word():
    valid_words = ValidWords()
    assert valid_words.binary_search('zymic') is True


def test_binary_search_odd_index():  # checking for infinite loop
    valid_words = ValidWords()
    assert valid_words.binary_search(valid_words.wordlist[1]) is True


def test_binary_search_even_index():  # checking for infinite loop
    valid_words = ValidWords()
    assert valid_words.binary_search(valid_words.wordlist[7420]) is True


def test_binary_search_word_smaller_than_first():
    valid_words = ValidWords()
    assert valid_words.binary_search('aaaaa') is False


def test_binary_search_word_greater_than_last():
    valid_words = ValidWords()
    assert valid_words.binary_search('zzzzz') is False


def test_is_valid_for_valid():
    valid_words = ValidWords()
    assert valid_words.is_valid('abaca') is True


def test_is_valid_for_invalid():
    valid_words = ValidWords()
    assert valid_words.is_valid('bruce') is False


def test_is_valid_for_none():
    valid_words = ValidWords()
    assert valid_words.is_valid(None) is False


def test_is_valid_for_numbers_as_str():
    valid_words = ValidWords()
    assert valid_words.is_valid('12345') is False


def test_is_valid_len_four():
    valid_words = ValidWords()
    assert valid_words.is_valid('pick') is False


def test_is_valid_len_six():
    valid_words = ValidWords()
    assert valid_words.is_valid('banana') is False
