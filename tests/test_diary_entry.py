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
given 
'''