"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, strings):
        if not strings:
            return ""
        prefix = strings[0]
        for string in strings[1:]:
            while string[: len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
