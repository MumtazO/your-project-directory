def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
        #print(char)
        #print(f"Char is {counter[char]}")
    letter = sorted(counter.items(), key=lambda item: item[1], reverse = True)[0][0]
    #print("Letter")
    #print(letter)
    #print(counter)
    #print(counter.items())
    #print(sorted(counter.items(), key=lambda item: item[1], reverse = True))
    #print(sorted(counter.items(), key=lambda item: item[1], reverse = True)[0][0])
    return letter


print(get_most_common_letter("the roof, the roof, the roof is on fire!"))
print(get_most_common_letter("a a a a b c d !"))

    