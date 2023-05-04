class MusicTracker():
    def __init__(self):
        self._song = []

    def add_music(self, song):
        self._song.append(song)
        # Parameters:
            #song: string representing the song the user adds

    def get_music(self):
        return self._song