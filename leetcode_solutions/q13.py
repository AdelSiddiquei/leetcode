"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/description/
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, numeral):

        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        sum = 0

        for char in numeral:
            pass


