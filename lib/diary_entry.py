class DiaryEntry:
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents
        

    def format(self):
        return f"{self._title}: {self._contents}"

    def count_words(self):
        wordcount = self.format().split()
        return len(wordcount)

    def reading_time(self, wpm):
        wordcount = self._contents.split()
        reading = len(wordcount)
        minutecounts = reading / wpm
        finalcount = int(minutecounts)
        return f"this will take {finalcount} minute(s) to read"


    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass


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