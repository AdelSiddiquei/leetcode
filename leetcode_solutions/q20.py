"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, string: str) -> bool:
        """Check for Valid parenthesis use in a string.

        Args:
            string (str): _description_

        Returns:
            bool: _description_
        """
        open_brackets = []  # will use this to keep track of open brackets as we iterate over the string

        pairs = {"}": "{", ")": "(", "]": "["}  # dict of bracket pairs

        for char in string:
            if char in pairs.values():
                open_brackets.append(char)
            else:
                if (
                    not open_brackets or open_brackets.pop() != pairs[char]
                ):  # checks if char closes the most recently opened bracket.
                    return False
        return (
            not open_brackets
        )  # true if open is empty, i.e. all brackets have been closed appropriately.
