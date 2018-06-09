"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
# O(n) method 
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return sum(nums)

        cursum, maxsum = nums[0], nums[0]
        for i in range(1, len(nums)):
            cursum = max(nums[i], cursum + nums[i])
            maxsum = max(cursum, maxsum)

        return maxsum
