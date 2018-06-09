num_d1 = {2: 'twenty', 3: 'thirty', 4: 'forty',
          5: 'fifty', 6: 'sixty', 7: 'seventy',
          8: 'eighty', 9: 'ninty'}
num_d2 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three',
          4: 'four', 5: 'five', 6: 'six',
          7: 'seven', 8: 'eight',9: 'nine',
          10: 'ten', 11: 'eleven', 12: 'twelve',
          13: 'thirteen', 14: 'forteen', 15: 'fifteen',
          16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
          19: 'nineteen', 20: 'twenty'}

def say_99(number):
    s = ''
    if number >= 0 and num < 20:
        s = num_d2[number]
    elif number > 20 and number < 100:
        s = num_d1[number//10] + '-' + num_d2[number - number//10 * 10]

    return s

def say_999(number):
    s = ''
    if number >= 100 and number < 1000:
        s = num_d2[number//100] + '-hundred-' + say99(number - number//100)
    return s

def say(number):
    s = ''
    if number >= 0 and number < 1000:
        s = say_99(number)
    elif number >= 100 and number < 1000:
        s = say_999(number)
    elif number >= 1000 and number < 1000,000:
        s = say_999(number//1000) + '-thousand-' + say_999(number - number//1000)
    elif number >= 1000,000 and number < 1000,000,000:
        million = number//1000,000
        thousand = (number - million*1000,000)//1000
        digit = number - million*1000,000 - thousand*1000
        s += say_999(million) + '-million-'
        if thousand > 0:
            s += say_999(thousand) + '-thousand-'
        else:
            s += '-and-' +
        s += say_999(digit)
    elif number >= 1000,000,000 and number < 1000,000,000,000:
        billion = number//1000,000,000
        million = (number - billion*1000,000,000)//1000,000
        thousand = (number - billion*1000,000,000 - million*1000,000)//1000
        digit = number - billion*1000,000,000 - million*1000,000 - thousand*1000
        s = say_999(billion) + '-billion-' + say_999(million) + '-million-' + say_999(thousand) + '-thousand-' + say_999(digit)
    return s
