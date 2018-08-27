"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     Iwww.hua

"""

"""
Analysis:
Method 1: Arrange a string with a length l to a zigzag shape will need a matrix of dimention r * [(l//(2*r-2)+1)*(r-1)] max
to hold. So the main idea is to reconstruct that zigzag patter in the matrix first and then read the string line
by line.

"""
# method 1: brutal force, but the math of the index is very difficult to figure out.
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # predefine a matrix to hold the result
        l = len(s)
        col = (l//(2*numRows-2)+1)*(numRows-1)
        m = [[-1 for i in range(col)] for j in range(numRows)]

        # fill in the matrix
        for i in range(l):
        # the math of the index is hard to figure out !!!    
           


        # read the matrix line by line into a new string
        res = ""
        for i in range(col):
            for j in range(numRows):
                if m[i][j] != -1:
                    res += m[i][j]
        return res

# method 2: row number increase or decrease by step size of 1 while column number doesn't really matter -- we only
# care about the order of the letters showing up in each row. So we start with empty string representing each row, 
# and fill in each row with the strings consecutively (column number doesn't matter, only the order matters here),
# only considering row numbers. For row numbers, keep adding 1 until it goes to numRows - 1, then keep substracting 
# 1 until it goes to 0, then keep adding 1.
# The last step is to join all rows.
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)