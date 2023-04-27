from lib.words_per_minute import *

def test_words_per_minute():
    result = words_per_minute(400)
    assert result == "this will take 2 minute(s) to read"

def test_words_per_minute_are_not_integer():
    result = words_per_minute("hello")
    assert result == "this is not an integer"
