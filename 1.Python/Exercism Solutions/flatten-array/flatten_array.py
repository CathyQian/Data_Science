def flatten(iterable):
    s = []
    for i in iterable:
        # if i is list:
        #if not isinstance(i, str) and hasattr(i, '__iter__'):
        if isinstance(i, (list, tuple)):
            s += flatten(i)
        # if i a str
        elif i != None:
            s.append(i)
    return s
