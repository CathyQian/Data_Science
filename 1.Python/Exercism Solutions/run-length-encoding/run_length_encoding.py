import re
# more concise solution
def decode(string):
    result = ''
    while len(string) != 0:
        substring = re.match(r"\d*(\w|\s)", string).group()
        string = string.replace(substring, '', 1)
        if len(substring) > 1:
            result += substring[-1] * int(substring[:-1])
    return result


def encode(string):
    result = ''
    while len(string) != 0:
        substring = re.match(r"(\w|\s)\1*", string).group()
        string = string.replace(substring, '', 1)
        if len(substring) > 1:
            substring = "{}{}".format(len(substring), substring[0])
        result += substring
    return result
