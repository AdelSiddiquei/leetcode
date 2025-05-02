"""
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
"""

class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
   
    def solution_2(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)

        if n == 0: return 0
        
        for i in range(h-n+1):
            if haystack[i:i+n] == needle: return i
        
        return -1