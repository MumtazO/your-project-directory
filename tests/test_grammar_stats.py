from lib.grammar_stats import *

'''
given a string #check returns True if string starts with a capital letter and ends with a punctuation mark otherwise it returns False.
'''

def test_grammar_stats_string_with_capital_letter_and_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello!")
    assert result == True

def test_grammar_stats_string_with_capital_letter():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello")
    assert result == False

def test_grammar_stats_string_with_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("ello!")
    assert result == False

"""
given several texts #percentage_good returns a percentage that has passed the check
"""

def test_percentage_good():
    grammar_stats = GrammarStats()
    assert grammar_stats.percentage_good()

'''

'''

def test_check_amounts_of_trues():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello")
    grammar_stats.check("ello")
    grammar_stats.check("Hello!")
    grammar_stats.check("Mello!")
    result = grammar_stats.percentage_good()
    assert result == 50

def test_check_amounts_of_checks():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello")
    grammar_stats.check("ello")
    grammar_stats.check("Hello!")
    result = grammar_stats.percentage_good()
    assert result == 33