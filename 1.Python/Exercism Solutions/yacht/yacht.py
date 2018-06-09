# Score categories
# Change the values as you see fit

## This one is much faster

YACHT = lambda d: 50 if len(set(d)) == 1 else 0
ONES = lambda d: sum(x for x in d if x == 1)
TWOS = lambda d: sum(x for x in d if x == 2)
THREES = lambda d: sum(x for x in d if x == 3)
FOURS = lambda d: sum(x for x in d if x == 4)
FIVES = lambda d: sum(x for x in d if x == 5)
SIXES = lambda d: sum(x for x in d if x == 6)
FULL_HOUSE = lambda d: sum(d) if len(set(d)) == 2 and any(d.count(x) == 3 for x in set(d)) else 0
FOUR_OF_A_KIND = lambda d: sum(x * 4 for x in set(d) if d.count(x) > 3)
LITTLE_STRAIGHT = lambda d: 30 if sum(d) == 15 and len(set(d)) == 5 else 0
BIG_STRAIGHT = lambda d: 30 if sum(d) == 20 and len(set(d)) == 5 else 0
CHOICE = lambda d: sum(d)


def score(dice, category):
    if any(not 0 < x < 7 for x in dice):
        raise ValueError("Invalid dice {}".format(dice))

    return category(dice)
