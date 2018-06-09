aa = ('wink','double blink','close your eyes','jump')

def handshake(code):
    r = []
    for a in aa:
        if code%2: r.append(a)
        code >>= 1
    if code: r.reverse()
    return r

def secret_code(actions):
    part1, part2, t = 0, 0, 1
    for i, a in enumerate(aa):
        if a in actions:
            part1 += t>>i
    # if reversed
    if len(actions)>1 and aa.index(actions[0]) > aa.index(actions[1]):
        part2 += t<<4

    return part1 + part2
