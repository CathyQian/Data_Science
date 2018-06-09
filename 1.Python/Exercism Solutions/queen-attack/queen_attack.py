class Queen(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        # need to detect exception
        if self.row > 7 or self.row < 0 or self.column > 7 or self.column < 0:
            raise ValueError('Queen position outside of range [0, 7]*[0, 7]')

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("The two queens can't overlap!")
        elif self.row == another_queen.row or self.column == another_queen.column\
            or abs((self.row - another_queen.row)/(self.column - another_queen.column)) == 1:
            return True
        else:
            return False
