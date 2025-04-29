from leetcode_solutions.q26 import Solution
import numpy as np

test_input_1 = [1, 1, 2]
expected_output_1 = 2
test_input_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expected_output_2 = 5


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert test_input_1[0:expected_output_1] == [1, 2]

    assert expected_output_2 == solution.solution_1(test_input_2)
    assert test_input_2[0:expected_output_2] == [0, 1, 2, 3, 4]


def test_solution_2():
    solution = Solution()
    assert expected_output_1 == solution.solution_2(test_input_1)
    assert test_input_1[0:expected_output_1] == [1, 2]

    assert expected_output_2 == solution.solution_2(test_input_2)
    assert test_input_2[0:expected_output_2] == [0, 1, 2, 3, 4]
