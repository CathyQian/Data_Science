def score(word):
    word = word.upper()
    letter_dict = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'R':1, 'S':1,
                   'T':1, 'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4,
                   'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8,'Q':10, 'Z':10}
    s = 0
    for w in word:
       if w in letter_dict.keys():
           s += letter_dict[w]
    return s


"""
def score(word):
    scores = dict.fromkeys(["a","e","i","o","u","l","n","r","s","t"], 1)
    scores.update(dict.fromkeys(["d","g"], 2))
    scores.update(dict.fromkeys(["b","c","m","p"], 3))
    scores.update(dict.fromkeys(["f","h","v","w","y"], 4))
    scores.update(dict.fromkeys(["j","x"], 8))
    scores.update(dict.fromkeys(["q","z"], 10))
    scores["k"] = 5
    return sum([scores[c] for c in word.lower()])


"""
