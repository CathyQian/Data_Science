# -*- coding: utf-8 -*-
"""
Given a sorted integer array without duplicates, return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Analysis：
这道题给定我们一个有序数组，让我们总结区间，具体来说就是让我们找出连续的序列，然后首尾两
个数字之间用个“->"来连接，那么我只需遍历一遍数组即可，
每次检查下一个数是不是递增的，如果是，则继续往下遍历，如果不是了，我们还要判断此时是一个
数还是一个序列，一个数直接存入结果，序列的话要存入首尾
数字和箭头“->"。我们需要两个变量i和j，其中i是连续序列起始数字的位置，j是连续数列的长度，
当j为1时，说明只有一个数字，若大于1，则是一个连续序列，
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rlist, i = [], 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1
            if j > i:
                rlist.append(str(nums[i]) + '->' + str(nums[j]))
            else:
                rlist.append(str(nums[i]))
            i = j + 1
         return rlist
