def nth_prime(positive_number):
    if positive_number < 1:
        raise ValueError('n is not valid!')
    prime_list = [2]
    i = 3
    while len(prime_list) < positive_number:
        temp = [i%j for j in prime_list]
        if 0 not in temp:
            prime_list.append(i)
        i += 1
    return prime_list[-1]
