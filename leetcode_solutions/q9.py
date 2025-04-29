"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/description/
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, number: int) -> bool:
        """Convert to string method

        Args:
            number (int): _description_

        Returns:
            bool: True/False on whether the input is a palindrome
        """
        return str(number) == str(number)[::-1]
