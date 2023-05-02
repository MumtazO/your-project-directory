from lib.diary_entry import *


'''
given title and contents, #format returns a string format of diary entry
'''
def test_diary_entry_format():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    result = diary_entry.format()
    assert result == "My Title: These are the contents"

'''
given diary entry, #count_words returns number of words as an integer.
'''

def test_diary_entry_count_words():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    result = diary_entry.count_words()
    assert result == 6

'''
given a diary entry, #reading_time returns the amount of time it will take to read in minutes
'''

def test_diary_entry_reading_time():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    result = diary_entry.reading_time(2)
    assert result == "this will take 2 minute(s) to read"

''''
given the contents of a diary entry, and the #wpm, and the amount of #minutes you have, #reading_chunk returns the the chunk of the contents that can be read in that time 
'''

def test_reading_chunk_with_2_wpm_and_2_minutes():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2,2)
    assert result == "one two three four"


"""
after calling #reading_chunk again it will give us the following chunk as per #wpm and #minutes provided
"""

def test_reading_chunk_with_2_wpm_and_1_minutes_multiple_times():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2,1) == "one two"
    assert diary_entry.reading_chunk(2,1) == "three four"
    assert diary_entry.reading_chunk(2,1) == "five six"

def test_reading_chunk_with_3_wpm_and_1_minutes_multiple_times():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(3,1) == "one two three"
    assert diary_entry.reading_chunk(2,1) == "four five"
    assert diary_entry.reading_chunk(1,1) == "six"

"""

"""
    