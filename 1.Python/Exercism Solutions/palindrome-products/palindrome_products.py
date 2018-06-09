def palindrome(max_factor, min_factor):
    # output both smallest_palindrome and largest_palindrome
    product = {}
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            pct = i*j
            if str(pct)[::-1] == str(pct) and pct not in product:
                product[pct] = [(i, j)]
            elif str(pct)[::-1] == str(pct):
                product[pct].append((i, j))
    # find min and max
    smallest, largest = max_factor**2, min_factor**2
    small_factors, large_factors = {}, {}
    for k, v in product.items():
        if k < smallest:
            smallest = k
            small_factors = set(v)
        if k > largest:
            largest = k
            large_factors = set(v)
     return ((smallest, small_factors), (largest, large_factors))
