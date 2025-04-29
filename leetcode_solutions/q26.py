"""
26. Remove Duplicates from Sorted Array
Must change input array in place and return number of unique elements.

https://leetcode.com/remove-duplicates-from-sorted-array
"""

import numpy as np


class Solution:
    """
    26. Remove Duplicates from Sorted Array
    self.solution_count for number of methods implemented.
    self.difcount for nubmer of unique elements found in array from most recent call of a solution (initialised to 0)
    """

    def __init__(self):
        self.solution_count = 2  # update as more solutions made
        self.difcount = 0

    def solution_1(self, array: list) -> int:
        """Two pointer method

        Args:
            array (np.ndarray): input array
        """
        if len(array) == 0:
            self.difcount = 0
            return 0
        self.difcount = 1
        for i in range(1, len(array)):
            if array[i] != array[i - 1]:
                array[self.difcount] = array[i]
                self.difcount += 1
        return self.difcount

    def solution_2(self, array: np.ndarray) -> int:
        """
        Method using NumPy
        Args:
            array (np.ndarray): A 1d array

        Returns:
            int: The number of unique elements in the input.
        """
        unique_elements = np.unique(
            array
        )  # np.unique() returns an array of all unique elements of the input array

        self.difcount = len(unique_elements)

        array[: self.difcount] = unique_elements  # modify input array in place.

        return self.difcount
