def words_in_string(string):
    if type(string) != str:
        return "Not a string!"
    else:
        wordcount = len(string.split())
        return wordcount