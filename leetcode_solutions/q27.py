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
        Changes an inputed list in place such that any entry matching the given value is put at the end.
        Args:
            array (list): _description_
            value (array.dtypy): _description_

        Returns:
            int: number of entries that did not match the given value.
        """
        self.difcount = len(array)
        for i in range(self.difcount):
            if array[i] == value:
                self.difcount -= 1
                r = array.pop(array[i])
                array.append(r)
            else:
                continue
        return self.difcount
