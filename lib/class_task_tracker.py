class TaskTracker():
    def __init__(self):
        self._tasks = []

    def add(self, task):
        self._tasks.append(task)

    def task_list(self):
        return self._tasks
        
    def task_completed(self, index):
        del self._tasks[index]
        