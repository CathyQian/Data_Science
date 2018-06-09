def prime_factors(natural_number):
    r, i = [], 2
    while i <= natural_number and natural_number > 1:
        if natural_number%i == 0:
            r.append(i)
            natural_number /= i
        else:
            i += 1
    return r
