from lib.music_tracker import *

"""
Test that the #get_music contains an empty list at the beginning
"""

def test_music_tracker_empty():
    music_tracker = MusicTracker()
    result = music_tracker.get_music()
    assert result == []

"""
Given a song #add_music adds to song to the list inside #get_music
"""

def test_music_tracker_added_multiple_songs():
    music_tracker = MusicTracker()
    music_tracker.add_music("die for you")
    music_tracker.add_music("single ladies")
    music_tracker.add_music("anti hero")
    assert music_tracker.get_music() == ["die for you", "single ladies", "anti hero"]

