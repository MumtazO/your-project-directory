def words_per_minute(words):
    if type(words) != int:
        return "this is not an integer"
    else: 
        minutecounts = words / 200
        finalcount = int(minutecounts)
        return f"this will take {finalcount} minute(s) to read"