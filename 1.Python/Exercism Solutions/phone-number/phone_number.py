class Phone(object):
    def __init__(self, phone_number):
        # Retain only the digits in the string
        number_list = [c for c in phone_number if c.isdigit()]

        # Check number length. if length is 11, and number begins with country code 1, then return last 10 numbers
        if (len(number_list) == 11) and number_list[0] == "1":
            number_list = number_list[1:]
        # If number_length is incorrect, or if the area code or exchange
        # code is incorrect, raise an error
        elif (len(number_list) != 10) or (number_list[0] in "01") or (number_list[3] in "01"):
            raise ValueError("Invalid phone number")

        self.number = "".join(number_list)

    @property
    def area_code(self):
        return self.number[0: 3]

    def pretty(self):
        return "({}) {}-{}".format(self.area_code, self.number[3:6], self.number[6:])
