"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored
 in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as
 a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

"""
Note:
1) The digits are stored in reverse order, so we can simply add the numbers from the head of the linked
list.
2) A flag number is needed to indicate the sum of any digits is over 10. 
3) There are no leading zeros. So we need to add additional elements in the sum linked list if flag = 1
after the addition of the last elements.
4) The two linked list may or may not have the same number of elements.
5) Both linked lists are non-empty. So we don't need to consider empty linked lists.
"""


# Solution: time complexity O(max(m,n)), space complexity O(max(m,n))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        head = ListNode(-1) # define dummy node as head
        r = head
        while l1 and l2:
            total = l1.val + l2.val + flag
            flag = total // 10
            r.next = ListNode(total % 10)
            l1, l2, r = l1.next, l2.next, r.next
        while l1:
            total = l1.val + flag
            flag = total // 10
            r.next = ListNode(total % 10)
            l1, r = l1.next, r.next
        while l2:
            total = l2.val + flag
            flag = total // 10
            r.next = ListNode(total % 10)
            l2, r = l2.next, r.next
        if flag == 1:
            r.next = ListNode(1)
        return head.next