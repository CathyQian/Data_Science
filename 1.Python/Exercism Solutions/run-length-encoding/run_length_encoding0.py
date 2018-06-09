def decode(string):
    decode_s = ''
    num = ''
    if len(string) == 0:
        return string
    for i in range(len(string)):
        if string[i].isnumeric():
            num += string[i]
        elif string[i].isalpha() or string[i] == ' ':
            if len(num) > 0:
                decode_s += int(num)*string[i]
            else:
                decode_s += string[i]
            num = ''

    return decode_s

def encode(string):
    # if string is empty
    if len(string) < 1:
        return string

    count, encode_s = 1, ''
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            if count > 1:
                encode_s += str(count) + string[i-1]
            else:
                encode_s += string[i-1]
            count = 1

    # deal with the last character
    if count > 1:
        encode_s += str(count) + string[-1]
    else:
        encode_s += string[-1]
    return encode_s
