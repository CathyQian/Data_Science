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
"""注意:1)nums里可能有重复元素2）return index不能一样
examples: nums = [2, 2], target = 4, return [0, 1]
"""
# brutal force, O(n2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            other = target - nums[i]
            if other in nums[i+1:]:
                return [i, nums[i+1:].index(other) + i + 1]

# faster Solution using dict/hash (find use O(1)), O(n)
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            if target-x in d:
                return [d[target-x], i]
            d[x] = i
