from lib.grammar_checker import *
"""
check if the first character of the string is a capital letter and the last character is a punctuation mark
"""

def test_correct_grammar_check():
    result = grammar_checker("Hello!")
    assert result == "This looks like it's grammatically correct!"

"""
test if there are no capital letters in the first character and no puntuation mark in the last character.
"""

def test_wrong_grammar_check():
    result = grammar_checker("fakdjfhak")
    assert result == "This doesn't look like it's grammatically correct!"

"""
Check when the first character is a capital letter, but the last character is not a punctuation mark
"""

def test_first_char_uppercase_but_last_char_not_punctuation():
    result = grammar_checker("Hello")
    assert result == "This doesn't look like it's grammatically correct!" 

"""
Check when the first character is not a capital letter, but the last character is a punctuation mark
"""

def test_first_char_not_uppercase_but_last_char_punctuation():
    result = grammar_checker("hello!")
    assert result == "This doesn't look like it's grammatically correct!" 

"""
check if argument is not a string
"""

def test_if_argument_not_a_string():
    result = grammar_checker(5)
    assert result == "This is not a string!"
