def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strings are not of equal length!')
    count = 0
    for i in range(len(strand_a)):
        if strand_a[i]!= strand_b[i]:
            count += 1
    return count

"""
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must have same length')
    return sum(a != b for a, b in zip(strand_a, strand_b))  # sum(True, True, False) = 2
"""
