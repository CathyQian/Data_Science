def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError('The input values are invalid!')

    return [series[n:n+length] for n in range(len(series) - length + 1)]
