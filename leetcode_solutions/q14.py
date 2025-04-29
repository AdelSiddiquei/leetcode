"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, strings: list[str]) -> str:
        if not strings:
            return ""
        prefix = strings[0]             #set prefix to first string
        for string in strings[1:]:
            while string[: len(prefix)] != prefix:   #check for match
                prefix = prefix[:-1]               #shorten prefix for no match
                if not prefix:                         #checking if prefix is empty
                    return ""
        return prefix
