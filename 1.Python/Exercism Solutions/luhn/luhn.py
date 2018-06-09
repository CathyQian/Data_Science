class Luhn(object):
    def __init__(self, card_num):
        self.card_number = card_num

    def is_valid(self):
        num_str = self.card_number.replace(' ', '')
        length = len(num_str)
        if length <= 1:
            return False

        new_num = []
        for i in range(length):
            if not num_str[length - 1 - i].isdigit():
                return False

            if i%2 != 0:
                temp = int(num_str[length - 1 - i])*2
                if temp > 9:
                    temp -= 9
                new_num.append(temp)
            else:
                new_num.append(int(num_str[length - 1 - i]))
        return sum(new_num)%10 == 0
