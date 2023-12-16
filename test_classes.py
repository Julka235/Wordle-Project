from classes import Database
import pytest


# test class Database

def test_create_database():
    database = Database('database_to_test.txt')
    wordlist = ['brand', 'crime', 'pouty']
    assert database.length == 3
    assert database.wordlist == wordlist


def test_create_database_incorrect_path():
    with pytest.raises(FileNotFoundError) as excinfo:
        Database('nonexistent_file.txt')
    assert str(excinfo.value) == 'File nonexistent_file.txt not found'
