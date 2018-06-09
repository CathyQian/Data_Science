"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
need to modify nums in place
Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II
"""

# method 1: list1 + list2, but not in place
class solution(object):    
    def rotateArray(self, nums, k):
        # can't use nums = nums[len(nums) - k:] + nums[:len(nums) - k] because it is not IN PLACE modification
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k] 
    
# method 2: double reverse in-situ

    def reverse(self, nums, start, end):
        # bring start and end to avoid overflow, i.e., k = 0, len(nums) = 0
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    def rotateArray2(self, nums, k):
        k %= len(nums) # don't forget this line
        if k > 0:
            self.reverse(nums, 0, len(nums) - 1)
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, len(nums) - 1)
           
            

    