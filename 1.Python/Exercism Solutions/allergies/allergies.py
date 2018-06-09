# bitwise operation
class Allergies(object):
    allergies = {'eggs'         : 1,
                 'peanuts'      : 2,
                 'shellfish'    : 4,
                 'strawberries' : 8,
                 'tomatoes'     : 16,
                 'chocolate'    : 32,
                  'pollen'      : 64,
                  'cats'        : 128}

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return (self.score & self.allergies.get(item)) > 0

    @property
    def lst(self):
        return [a for a, v in self.allergies.items() if self.score & v]
