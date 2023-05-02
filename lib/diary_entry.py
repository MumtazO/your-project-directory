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