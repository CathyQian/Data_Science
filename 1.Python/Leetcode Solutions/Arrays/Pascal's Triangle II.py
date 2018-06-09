# -*- coding: utf-8 -*-
"""
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):
    def generate(self, k):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if k < 0:
            return []
        prev, curr = [], []
        for i in range(k+1):
            curr = [1]*(i + 1)
            j = 1
            while j < i:
                curr[j] = prev[j - 1] + prev[j]
                j += 1
            prev = curr
        return curr