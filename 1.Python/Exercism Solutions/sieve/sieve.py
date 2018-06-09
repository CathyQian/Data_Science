def sieve(limit):
    if limit < 2:
        return []
    filtered = [i for i in range(2, limit + 1)]
    for i in range(2, limit + 1):
        if i in filtered:
            filter = [i*j for j in range(i, limit//i + 1)]
            temp = [items for items in filtered if items not in filter]
            filtered = temp
    return filtered
