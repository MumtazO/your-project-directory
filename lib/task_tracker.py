
def task_tracker(text):
    if type(text) != str:
        return "This is not a string!"
    elif text.__contains__("#TODO"):
        return "this task is still pending"
    else:
        return  "this is not pending"