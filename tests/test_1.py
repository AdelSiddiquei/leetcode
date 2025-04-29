from leetcode_solutions.q1 import Solution

test_input_1 = [[2, 7, 11, 15], 9]
expected_output_1 = [0, 1]
test_input_2 = [[3, 2, 4], 6]
expected_output_2 = [1, 2]
test_input_3 = [[3, 3], 6]
expected_output_3 = [0, 1]


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(*test_input_1)
    assert expected_output_2 == solution.solution_1(*test_input_2)
    assert expected_output_3 == solution.solution_1(*test_input_3)
