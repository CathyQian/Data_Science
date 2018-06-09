import re

def word_count(phrase):
    list_ = re.sub(r"[^a-zA-Z0-9 ']|[,_\t\n]", ' ', phrase).lower().split(" ")
    words_count = {}
    for word in list_:
        word = re.sub(r"\A'|'$", '', word)
        if not word:
            continue
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return words_count
