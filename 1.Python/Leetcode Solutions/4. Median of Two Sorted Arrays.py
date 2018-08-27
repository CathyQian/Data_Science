"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

"""
Analysis: This problem is a case of the find kth element in two sorted arrays. If m+n is even,
the median is the average of the ((m+n)//2)th and ((m+n)//2 + 1)th element; If m + n is odd,
the median is the ((m+n)//2 + 1)th element.

So the key is to find the kth element in two sorted arrays. This can be done in a subfunction 
getKth(nums1, nums1_start, nums2, nums2_start, k). 

Two key points for the getKth function: 
1) nums1 and nums2 may have repeated elements.
2) be careful with index to avoid overflow.
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        if (l1 + l2) % 2 == 0:
            return (self.getKth(nums1, 0, nums2, 0, (l1+l2)//2) + self.getKth(nums1, 0, nums2, 0, (l1+l2)//2 + 1))*0.5
        else:
            return self.getKth(nums1, 0, nums2, 0, (l1+l2)//2 + 1)
    
    def getKth(self, A, A_start, B, B_start, k):
        """ find the kth largest element in sorted array A and B
        """
        # deal with unit case and exception
        if A_start >= len(A):
            return B[B_start + k - 1]
        elif B_start >= len(B):
            return A[A_start + k - 1]
        
        if k == 1:
            return min(A[A_start], B[B_start])
        
        # core recursion code
        A_key = A_start + k//2 - 1
        B_key = B_start + k//2 - 1
        
        if A_key < len(A) and B_key < len(B) and A[A_key] >= B[B_key] or A_key >= len(A):
            return self.getKth(A, A_start, B, B_start + k//2, k - k//2)
        elif A_key < len(A) and B_key < len(B) and A[A_key] < B[B_key] or B_key >= len(B):
            return self.getKth(A, A_start + k//2, B, B_start, k - k//2)
        