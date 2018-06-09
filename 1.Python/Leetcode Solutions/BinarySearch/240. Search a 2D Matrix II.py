"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # if matrix is empty
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False

        m, n = len(matrix), len(matrix[0])
        cr, cc = 0, n - 1
        while cr < m and cc >= 0:
            if matrix[cr][cc] == target:
                return True
            elif matrix[cr][cc] > target:
                cc -= 1
            else:
                cr += 1

        return False
