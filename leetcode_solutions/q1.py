"""
1. Two Sum
https://leetcode.com/problems/two-sum
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, input: list[int], target: int) -> list:
        """Method using Dictionaries

        Args:
            input (list[int]): List of integers.
            target (int): integer which our to be chosen numbers must sum to.

        Returns:
            list: The indices of the numbers that sum to the target from the input list.
        """
        seen = {}
        
        for i, num in enumerate(input):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return "No Solution found"
            