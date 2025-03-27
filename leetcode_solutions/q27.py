"""
27. Remove Element
https://leetcode.com/problems/remove-element
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made
        self.difcount = 0

    def solution_1(self, array: list, value):
        """
        Changes an inputed list in place such that all elements different from given value are listed first.
        Check self.difcount for how many elements are different from value.
        Args:
            array (list): array to be cleaned.
            value (): The element value to be removed from list.

        Returns:
            array: all elements not matching the value in array[:self.difcount]
        """
        self.difcount = 0
        for i in range(len(array)):
            if array[i] != value:
                array[self.difcount] = array[i]
                self.difcount += 1
        return self.difcount
