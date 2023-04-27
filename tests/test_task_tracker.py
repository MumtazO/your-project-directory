from lib.task_tracker import *

def test_task_tracker():
    result = task_tracker("#TODO")
    assert result == "this task is still pending"

def test_task_tracker_no_hashtag_TODO():
    result = task_tracker("done")
    assert result == "this is not pending"

def test_task_tracker_is_not_a_string():
    result = task_tracker(5)
    assert result == "This is not a string!"

def test_task_tracker_partial_result_only():
    result = task_tracker("TODO")
    assert result == "this is not pending"