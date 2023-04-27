from lib.grammar_checker import *

def test_correct_grammar_check():
    result = grammar_checker("Hello!")
    assert result == True

def test_wrong_grammar_check():
    result = grammar_checker("hdjkfhadkj")
    assert result == False