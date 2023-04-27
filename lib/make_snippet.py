def make_snippet(string):
    if len(string.split()) < 6:
        return string
    else:
        five = string.split()[:5]
        rightfive= " ".join(five)
        return f"{rightfive}..."