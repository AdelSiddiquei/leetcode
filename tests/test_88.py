from leetcode_solutions.q88 import Solution

test_input_1 = [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3]
expected_output_1 = [1, 2, 2, 3, 5, 6]

test_input_2 = [[1], 1, [], 0]
expected_output_2 = [1]

test_input_3 = [[0], 0, [1], 1]
expected_output_3 = [1]


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert expected_output_2 == solution.solution_1(test_input_2)
    assert expected_output_3 == solution.solution_1(test_input_3)
