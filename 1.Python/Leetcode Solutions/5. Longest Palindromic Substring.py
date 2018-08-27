"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

"""
Analysis:
This problem can be reframed into finding the longest consecutive string that is palindromic.
This is another 'longest' and "palindrom" problem.

For longest/maximum/shortest/minimum problem, it's intuitive to set a marker and compare with the marker every time
when getting a new value.

For palindrom problem, there are two ideas. One is to find the start and end of the string and compare what's in-between
one-by-one. The other one is to start from the center and then compare it from both sides. The trick here is to make sure
to consider two circumstances: 'aba'(odd case) and 'abba' (even case).

"""
# time complexity O(n^2)
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]