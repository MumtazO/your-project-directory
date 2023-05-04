from lib.class_task_tracker import *

"""
Test if #task_list is empty when no task has been added
"""

def test_task_list_empty():
    task_tracker = TaskTracker()
    assert task_tracker.task_list() == []
    

"""
Given provided task, check if task is added to #task_list
"""

def test_add_new_task():
    task_tracker = TaskTracker()
    task_tracker.add("walk the snail")
    task_tracker.add("walk the frog")
    task_tracker.add("walk the plant")
    assert task_tracker.task_list() == ["walk the snail", "walk the frog", "walk the plant"]

"""
Given completed task index, #task_completed removes task from #task_list
"""

def test_complete_task_removed():
    task_tracker = TaskTracker()
    task_tracker.add("walk the snail")
    task_tracker.add("walk the frog")
    task_tracker.add("walk the plant")
    task_tracker.task_completed(1)
    assert task_tracker.task_list() == ["walk the snail", "walk the plant"]
