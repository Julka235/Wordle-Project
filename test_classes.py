from classes import Database
from classes import IncorrectPath
import pytest


# test class Database

def test_create_database():
    database = Database('database_to_test.txt')
    wordlist = ['brand', 'crime', 'pouty']
    assert database.length == 3
    assert database.wordlist == wordlist


def test_create_database_incorrect_path():
    with pytest.raises(IncorrectPath) as excinfo:
        Database('nonexistent_file.txt')
    assert str(excinfo.value) == 'File not found in path nonexistent_file.txt'
