"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example, Given [100, 4, 200, 1, 3, 2], The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity.

"""



Class Solution(object):
    def longestConsecutive(self, num):
        """
        type num: list[int]
        rtype: int
        """
        result, lengths = 1, {key: 0 for key in num}
        for i in num:
            if lengths[i] == 0:
                lengths[i] = 1
                left, right = lengths.get(i-1, 0), lengths.get(i+1, 0)
                length = 1 + left + right
                result = max(result, length)
                lengths[i - left], lengths[i + right] = length, length
        return result