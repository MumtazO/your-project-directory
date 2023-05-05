import math
from lib.integration_diary_entry import *

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list

    def all(self):
        return self._entries
        

    def count_words(self):
        words = str(self._entries)
        total_of_words = words.split()
        return len(total_of_words)

        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        

    def reading_time(self, wpm):
        minutecounts = self.count_words() / wpm
        finalcount = math.ceil(minutecounts)
        return finalcount
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        

    def find_best_entry_for_reading_time(self, wpm, minutes):
        best_entry = None
        highest_wpm = 0
        max_words = wpm * minutes

        for entry in DiaryEntry.contents:
            entry_wpm = DiaryEntry.reading_time()

            if entry_wpm > highest_wpm and DiaryEntry.count_words() <= max_words:
                highest_wpm = entry_wpm
                best_entry = entry
            
            return best_entry


        # best_entry = None
        # highest_wpm = 0
        # for entry in self._entries:
        #     count_words =  DiaryEntry.count_words
        #     print(count_words)
        #     entry_wpm = int(count_words) / wpm

        #     if entry_wpm > highest_wpm and DiaryEntry.reading_time(entry_wpm) <= minutes:
        #         highest_wpm = entry_wpm
        #         best_entry = entry
        # return best_entry
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        # for loop would have to check 
        # wpm * minutes