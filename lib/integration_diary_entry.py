import math

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self._words_already_read = 0
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        wordcount = self.contents.split()
        return len(wordcount)
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        wordcount = self.contents.split()
        reading = len(wordcount)
        minutecounts = reading / wpm
        finalcount = math.ceil(minutecounts)
        return finalcount
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        readable_words = wpm * minutes
        wordcount = self.contents.split()
        if self._words_already_read >= len(wordcount):
            self._words_already_read = 0
        chunk_start = self._words_already_read
        chunk_end = self._words_already_read + readable_words
        newlist = wordcount[chunk_start:chunk_end]
        self._words_already_read = chunk_end
        return " ".join(newlist)
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass