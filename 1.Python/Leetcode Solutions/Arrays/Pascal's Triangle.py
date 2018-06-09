# -*- coding: utf-8 -*-
"""
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        r = []
        for i in range(numRows):
            rlist = [1]*(i + 1)
            j = 1
            while j < i:
                rlist[j] = r[i - 1][j - 1] + r[i - 1][j]
                j += 1
            r.append(rlist)
            
        return r