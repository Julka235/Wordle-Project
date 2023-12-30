from classes import (
    Database,
    Guesswords,
    ValidWords,
    Solution
)
import pytest


# test class Database

def test_create_database():
    '''
    tests init, getting words containng numbers,
    uppercase or having more or less than 5 letters,
    checks if wordlist is sorted
    '''
    database = Database('txt_files/database_to_test.txt')
    wordlist = ['BRAND', 'CRIME', 'POUTY']
    assert database.length == 3
    assert database.wordlist == wordlist


def test_create_database_incorrect_path():
    with pytest.raises(FileNotFoundError) as excinfo:
        Database('nonexistent_file.txt')
    assert str(excinfo.value) == 'File nonexistent_file.txt not found'


# test class GuesswordsDatabase

def test_create_guesswords():
    assert Guesswords().length == 2315


def test_generate_guessword(monkeypatch):
    def return_aback(f):
        return 'ABACK'
    monkeypatch.setattr('classes.choice', return_aback)
    assert Guesswords().generate_guessword() == 'ABACK'


# test class ValidWords

def test_create_valid_words():
    assert ValidWords().length == 14839


def test_binary_search_word_exists():
    assert ValidWords().binary_search('abaca') is True


def test_binary_search_word_nonexistent():
    assert ValidWords().binary_search('caleb') is False


def test_binary_search_first_word():
    assert ValidWords().binary_search('aahed') is True


def test_binary_search_last_word():
    assert ValidWords().binary_search('zymic') is True


def test_binary_search_odd_index():  # checking for infinite loop
    valid_words = ValidWords()
    assert valid_words.binary_search(valid_words.wordlist[1]) is True


def test_binary_search_even_index():  # checking for infinite loop
    valid_words = ValidWords()
    assert valid_words.binary_search(valid_words.wordlist[7420]) is True


def test_binary_search_word_smaller_than_first():
    assert ValidWords().binary_search('aaaaa') is False


def test_binary_search_word_greater_than_last():
    assert ValidWords().binary_search('zzzzz') is False


def test_is_valid_for_valid():
    assert ValidWords().is_valid('abaca') is True


def test_is_valid_for_invalid():
    assert ValidWords().is_valid('bruce') is False


def test_is_valid_for_none():
    assert ValidWords().is_valid(None) is False


def test_is_valid_for_numbers_as_str():
    assert ValidWords().is_valid('12345') is False


def test_is_valid_len_four():
    assert ValidWords().is_valid('pick') is False


def test_is_valid_len_six():
    assert ValidWords().is_valid('banana') is False


# test class Solution

def test_create_solution(monkeypatch):
    def return_aback(f):
        return 'ABACK'
    monkeypatch.setattr('classes.choice', return_aback)
    solution = Solution()
    assert solution.guessword == 'ABACK'


def test_get_clues(monkeypatch):
    def return_aback(f):
        return 'ABACK'
    monkeypatch.setattr('classes.choice', return_aback)
    solution = Solution()
    word = 'ACCOY'
    clues = [
        'green',
        'yellow',
        'gray',
        'gray',
        'gray'
    ]
    assert solution.get_clues(word) == clues


def test_get_clues_two_same_letters_in_word(monkeypatch):
    def return_aback(f):
        return 'ABACK'
    monkeypatch.setattr('classes.choice', return_aback)
    solution = Solution()
    word = 'aalii'
    clues = [
        'green',
        'gray',
        'gray',
        'gray',
        'gray'
    ]
    assert solution.get_clues(word) == clues


def test_get_clues_invalid_word(monkeypatch):
    def return_aback(f):
        return 'ABACK'
    monkeypatch.setattr('classes.choice', return_aback)
    solution = Solution()
    word = 'abcde'
    assert solution.get_clues(word) is False


def test_get_clues_guessed_guessword(monkeypatch):
    def return_aback(f):
        return 'ABACK'
    monkeypatch.setattr('classes.choice', return_aback)
    solution = Solution()
    word = 'aback'
    assert solution.get_clues(word) is True


def test_get_clues_same_letter_second_in_guessword(monkeypatch):
    def return_evade(f):
        return 'EVADE'
    monkeypatch.setattr('classes.choice', return_evade)
    solution = Solution()
    word = 'aback'
    clues = [
        'yellow',
        'gray',
        'gray',
        'gray',
        'gray'
    ]
    assert solution.get_clues(word) == clues
