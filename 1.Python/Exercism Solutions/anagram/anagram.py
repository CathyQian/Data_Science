def detect_anagrams(word, candidates):
    # find the candidates with the same letters but different order
    w = sorted(list(word.lower()))
    r = []
    for c in candidates:
        cc = sorted(list(c.lower()))
        if cc == w and word.lower() != c.lower():
            r.append(c)

    return r
