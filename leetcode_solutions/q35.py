"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, array, target):
        for n, x in enumerate(array):
            if x >= target: 
                return n                #return the index which the target fits
        return len(array)                  #returns final index in case of no x in array >= target
