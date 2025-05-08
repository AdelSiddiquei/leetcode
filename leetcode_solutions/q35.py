"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position
"""


class Solution:
    def __init__(self):
        self.solution_count = 2  # update as more solutions made

    def solution_1(self, array: list, target: int) -> int:
        """A function that returns the index a target number would have when placed into a sorted array.

        Args:
            array (_type_): Sorted list (non-descending)
            target (int): _description_

        Returns:
            int: index of where the target would fit if added to sorted array
        """
        for n, x in enumerate(array):
            if x >= target:
                return n  # return the index which the target fits
        return len(array)  # returns final index in case of no x in array >= target

    def solution_2(self, array: list, target: int) -> int:
        """Binary Search to find the index a target number would take when added to a sorted array

        Args:
            array (list): sorted, non-descending
            target (int): number to be indexed

        Returns:
            int: index of target if added to list
        """
        left, right = 0, len(array)
        while left < right:
            mid = (left + right) // 2
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
