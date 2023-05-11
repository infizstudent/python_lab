import os
import pytest

from task_6 import connect_to_database, extract_chapters


@pytest.fixture(scope='module')
def conn():
    connection = connect_to_database()
    yield connection
    connection.close()
    os.remove('books.db')


@pytest.mark.database
def test_connect_to_database(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    result = cursor.fetchone()[0]
    assert result == 'books'


@pytest.mark.extract
def test_extract_chapters():
    content = '''CHAPTER I—START IN LIFE
    CHAPTER II—SLAVERY AND ESCAPE
    CHAPTER III—WRECKED ON A DESOLATE ISLAND
    CHAPTER IV—FIRST WEEKS ON THE ISLAND
    CHAPTER V—BUILDS A HOUSE—THE JOURNAL
    CHAPTER VI—ILL AND CONSCIENCE-STRICKEN
    '''
    extract_chapters(content)
    with open('../../chapters.txt', 'r') as f:
        result = f.read()
    assert result == 'CHAPTER I—START IN LIFE\nCHAPTER II—SLAVERY AND ESCAPE\nCHAPTER III—WRECKED ON A DESOLATE ISLAND\nCHAPTER IV—FIRST WEEKS ON THE ISLAND\nCHAPTER V—BUILDS A HOUSE—THE JOURNAL\nCHAPTER VI—ILL AND CONSCIENCE-STRICKEN\n'

