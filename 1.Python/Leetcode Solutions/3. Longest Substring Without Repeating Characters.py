"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", which the length is 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

"""
Analysis:
A substring is a consecutive subsection of the string s, defined by the starting and ending string
without any duplicates. So we need two pointers, one pointing at the beginning and one at the end
of the string. We enumerate the string s, so the index of the current element c is the end pointer.
The start pointer is initialized to be -1. If duplicated elements is found, the start pointer will 
move to the largest index of the already found duplicates. Scanned elements is put in a dictionary,
to make it easy to find duplicates.
An additional parameter is used to record the longest length during the enumeration.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        """
        # runtime: 95ms
        dic = {}
        res, last_match = 0, -1
        for i, c in enumerate(s):
            if c in dic and last_match < dic[c]:
                last_match = dic[c]
            res = max(res, i - last_match)
            dic[c] = i
        return res