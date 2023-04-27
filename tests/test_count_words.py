from lib.count_words import *

def test_words_in_string():
    result = words_in_string("words in string")
    assert result == 3

def test_words_in_string_when_not_a_string():
    result = words_in_string(5)
    assert result == "Not a string!"