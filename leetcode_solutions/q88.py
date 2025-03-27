"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array
"""

import numpy as np


class Solution:
    """
    For merging arrays lists of length m and n. The first array will have length m+n, with the final n entries as 0s.
    The second array will have length m.
    The output will be the merged array, sorted in ascending order.
    """

    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, array1, m, array2, n):
        for i in range(n):
            array1[i - n] = array2[i]
        array1.sort()
        return array1
