from leetcode_solutions.q35 import Solution

test_input_1 = [[1, 3, 5, 6], 5]
expected_output_1 = 2
test_input_2 = [[1, 3, 5, 6], 2]
expected_output_2 = 1
test_input_3 = [[1, 3, 5, 6], 7]
expected_output_3 = 4


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(*test_input_1)
    assert expected_output_2 == solution.solution_1(*test_input_2)
    assert expected_output_3 == solution.solution_1(*test_input_3)


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_2(*test_input_1)
    assert expected_output_2 == solution.solution_2(*test_input_2)
    assert expected_output_3 == solution.solution_2(*test_input_3)
