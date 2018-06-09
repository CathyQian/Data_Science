# -*- coding: utf-8 -*-
"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?

Analysis: (x, y) --> (y, n-1-x) after 90 degrees clockwise rotation
Difficulty is to do this in-place using limited extra space.
For any element with index (x, y), it's rotating values with the following four elements:
(x, y) --> (y, n-1-x) --> (n-1-x, n-1-y) --> (n-1-y, x) --> (x, y)

"""
"""

