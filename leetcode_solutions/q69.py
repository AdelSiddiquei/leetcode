"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, x:int) -> int:
        if x < 4: return 1
        i = 2
        while i < x/i:
            i+=1
        if i > x/i:
            return i-1
        else:
            return i

