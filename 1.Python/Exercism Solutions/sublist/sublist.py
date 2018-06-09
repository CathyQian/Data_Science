EQUAL = 'EQUAL'
SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
UNEQUAL = 'UNEQUAL'

def check_lists(first_list, second_list):
    first_str = ','.join([str(i) for i in first_list])
    second_str = ','.join([str(i) for i in second_list])

    if first_str == second_str:
        return EQUAL
    elif first_str in second_str:
        return SUBLIST
    elif second_str in first_str:
        return SUPERLIST
    else:
        return UNEQUAL
