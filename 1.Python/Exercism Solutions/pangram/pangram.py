def is_pangram(sentence):
    sentence = sentence.lower()
    new_sent = []
    for s in sentence:
        if s.isalpha() and s not in new_sent:
                new_sent.append(s)
    return len(new_sent) == 26
