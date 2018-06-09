# Score categories
# Change the values as you see fit
YACHT = 'Yacht'
ONES = 'Ones'
TWOS = 'Twos'
THREES = 'Threes'
FOURS = 'Fours'
FIVES = 'Fives'
SIXES = 'Sixes'
FULL_HOUSE = 'Full House'
FOUR_OF_A_KIND = 'Four of a Kind'
LITTLE_STRAIGHT = 'Little Straight'
BIG_STRAIGHT = 'Big Straight'
CHOICE = 'Choice'

def score(dice, category):
    d_dict = {}
    for i in dice:
        if i not in d_dict.keys():
            d_dict[i] = 1
        else:
            d_dict[i] += 1

    cat_map = {'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6}
    if category in cat_map.keys():
        num = cat_map[category]
        if num in d_dict.keys():
            return d_dict[num]*num
        else:
            return 0

    if category == 'Choice':
        return sum(dice)

    if category == 'Yacht':
        if len(d_dict) == 1:
            return 50
        else:
            return 0

    if category == 'Little Straight':
        if set(dice) == {1,2,3,4,5}:
            return 30
        else:
            return 0

    if category == 'Big Straight':
        if set(dice) == {2,3,4,5,6}:
            return 30
        else:
            return 0

    if category == 'Full House':
        if len(d_dict) == 2 and 2 in d_dict.values():
            return sum(dice)
        else:
            return 0

    if category == 'Four of a Kind':
        if len(d_dict) == 1 or len(d_dict) == 2:
            for d in d_dict.keys():
                if d_dict[d] >= 4:
                    return d*4
        else:
            return 0
