"""
66. Plus One
https://leetcode.com/problems/plus-one
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, digits: list) -> list:
        """Adds 1 to integer number where the numbers digits are represented by list.

        Args:
            digits (list): Represents the number when read left to right.

        Returns:
            list: New list representing the original integer + 1
        """
        n = len(digits)
        for i in range(1,n+1,1):        
            if digits[-i] < 9:          #right to left traversal
                digits[-i] += 1
                return digits
            digits[-i] = 0
        return [1] + digits             #if all elements == 9 prepends a 1 to the list
