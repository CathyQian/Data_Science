"""
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
"""
Analysis:
1) There may be duplicated elements in nums.
2) For duplicated elements, the returning elements needs to be different.
For examples: nums = [2, 2], target = 4, return [0, 1], not [0, 0] or [1, 1]
Therefore, two pointers both start from the beginning of the list can not be used.
3) This is not a sorted array. So two pointers --- one start from the beginning and one start
from the end of the list can not be used.
"""
# solution 1: brutal force, time ~ O(n^2), space ~ O(1)
"""" use one pointer i to enumerate the list, check if target - nums[i]
# is in the list or not, if yes, return index
The problem of this method is time complexity of checking if an element is in a list or not 
is O(n). Replacing the list with dictionary will change time complexity to be O(1).
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        for i in range(len(nums) - 1):
            other = target - nums[i]
            if other in nums[i+1:]:
                return [i, nums[i+1:].index(other) + i + 1]

# faster Solution using dict/hash (find use O(1)), O(n)
""" similarily, use one pointer i to enumerate the list -- there is no way to get around it.
The trick here is to put scanned elements in a dictionary, making checking elements easier 
(O(1) time complexity versus O(n) in a list).
The key of the dictionary is the target - x while the value is index i. When target - x is
found in the dictionary, index i is returned. Worth to mention is that, d[target - x] < i.
So [d[target - x], i] should be returned.
"""
class Solution:
    def twoSum(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            if target-x in d.keys():
                return [d[target-x], i]
            d[x] = i
