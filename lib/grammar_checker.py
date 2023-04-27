def grammar_checker(string):
    if type(string) != str:
        return "This is not a string!"
    elif len(string) < 2:
        return "Not long enough!" 
    elif string[0].isupper() and string[-1] in [".", "!", "?"]:
        return "This looks like it's grammatically correct!"
    else:
        return "This doesn't look like it's grammatically correct!"