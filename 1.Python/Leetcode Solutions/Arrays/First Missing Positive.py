# -*- coding: utf-8 -*-
"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
Analysis: 
1) This problem is looking for the first missing positive integer starting from 1, therefore all negative values are ignored.
2) natural thinking is first sort the values, but quick sort/binary sort takes O(nlogn)
3) This problem is different from other sorting problem:
   result of any sorting ignore the negative values would put x in [x-1] position in the sorted list.


"""