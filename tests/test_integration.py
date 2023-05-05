from lib.integration_diary import *
from lib.integration_diary_entry import *

def test_add_multiple_entries_to_diary():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "Some more contents 2")
    entry_2 = DiaryEntry("My Title 3", "Some more contents 4")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

def test_word_count_of_all_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "Some more contents 2")
    entry_2 = DiaryEntry("My Title 3", "Some more contents 4")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 8


"""
Given a wpm for reading #reading_time returns an integer representing the estimate of reading time in minutes 
"""

def test_reading_time_for_3_words_per_minute():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "Some more contents 2")
    entry_2 = DiaryEntry("My Title 3", "Some more contents 4")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(3) == 3


"""
Given a wpm of 3 and and 2 minutes for reading #find_best_entry_for_reading_time returns the diary entry that is closest to but not over the time that the user can read
"""
def test_wpm_of_3_and_reading_time_of_2():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "Some more contents for you to read")
    entry_2 = DiaryEntry("My Title 3", "Some more contents 4 4")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(3, 2) == entry_2