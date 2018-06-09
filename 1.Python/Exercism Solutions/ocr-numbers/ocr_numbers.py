digit_dict = {(" _ ", "| |", "|_|", "   "): '0',
              ("   ", "  |", "  |", "   "): '1',
              (" _ ", " _|", "|_ ", "   "): '2',
              (" _ ", " _|", " _|", "   "): '3',
              ("   ", "|_|", "  |", "   "): '4',
              (" _ ", "|_ ", " _|", "   "): '5',
              (" _ ", "|_ ", "|_|", "   "): '6',
              (" _ ", "  |", "  |", "   "): '7',
              (" _ ", "|_|", "|_|", "   "): '8',
              (" _ ", "|_|", " _|", "   "): '9'}

def convert(input_grid):
    return multiple_lines(input_grid)

def single_digit(input_g):
    if len(input_g)!= 4 or len(input_g[0]) != 3:
         raise Exception('The input dimension should be (4,3).')
    elif tuple(input_g) in digit_dict.keys():
        return digit_dict[tuple(input_g)]
    else:
        return '?'

def multi_digit(input_g):
    r = ''
    if len(input_g) != 4 or len(input_g[0]) %3 != 0:
        raise Exception('The input dimension is incorrect!')

    for w in range(len(input_g[0])//3):
        single = [input_g[0][w*3:w*3 + 3], input_g[1][w*3:w*3 + 3],
                  input_g[2][w*3:w*3 + 3], input_g[3][w*3:w*3 + 3]]
        r += single_digit(single)

    return r

def multiple_lines(input_g):
    r = ''
    if len(input_g) %4 != 0 or len(input_g[0]) %3 != 0:
        raise Exception('The input dimension is incorrect!')
    for h in range(len(input_g)//4):
        line = input_g[h*4:h*4 + 4]
        r += multi_digit(line) + ','
    return r[:-1]
