def is_armstrong(number):
    n_str = str(number)
    l = len(n_str)
    sum = 0
    for i in n_str:
        sum += int(i)**l
    return sum == number

"""
def is_armstrong(number):
    temp_list = [int(x) for x in str(number)]
    l = len(temp_list)
    return number = sum(map(lambda x: x**l, temp_list))
"""
