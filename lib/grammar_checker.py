import string
def grammar_checker(text):
    capital = text[0]
    last_letter = text[-1]
    punctuation = string.punctuation
    hasPunc = False
    for char in punctuation:
        if last_letter == char:
            hasPunc = True
    if (capital.isupper() and hasPunc):
        return True
    else:
        return False