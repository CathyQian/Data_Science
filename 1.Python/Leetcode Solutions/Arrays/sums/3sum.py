"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is: [ [-1, 0, 1], [-1, -1, 2] ]
"""

"""method 1. brutal force method, O(n^3) time complexity"""

class Solution():
    def 3sum(self, nums):
        """
        type nums: list[int]
        return: list[list[int]]
        """
        if len(nums) < 3:
            return []
        r = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        r.append(tuple(sorted([nums[i], nums[j], nums[k]])))
        return list(set(r))


"""method 2.time complexity O(n^2),space complexity O(n) """
"""重点：双指针，subfunction为2sum, 把target - 扫过的元素的放进set
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result, visited = set(), set()
        for i in range(len(nums) - 2):
            d, target = set(), - nums[i]
            if nums[i] not in visited:
                for j in range(i+1,len(nums)):
                    if nums[j] not in d:
                        d.add(target - nums[j])
                    else:
                        result.add((nums[i], target-nums[j], nums[j]))
                visited.add(nums[i])
        return list(result)
