"""
Given an array of size n, find the majority element. The majority element is 
the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always 
exist in the array.
"""
import collections
class solution(object):
    def majorelement(self, nums):
        """
        type nums: list of integer
        rtype: int
        """
        return sorted(collections.Counter(nums).items(), key = lambda a: a[1], reverse = True)[0][0]
        