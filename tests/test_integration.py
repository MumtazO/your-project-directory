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