"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        # leaf node
        elif root.left is None and root.right is None:
            return 1

        elif root.right is None:
            left = self.minDepth(root.left)
            return left + 1
        elif root.left is None:
            right = self.minDepth(root.right)
            return right + 1

        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)

            return min(left, right) + 1
