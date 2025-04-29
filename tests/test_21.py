from leetcode_solutions.q21 import Solution

test_input_1 = [[1, 2, 4], [1, 3, 4]]
expected_output_1 = [1, 1, 2, 3, 4, 4]
test_input_2 = [[], []]
expected_output_2 = []
test_input_3 = [[], [0]]
expected_output_3 = [0]


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert expected_output_2 == solution.solution_1(test_input_2)
    assert expected_output_3 == solution.solution_1(test_input_3)
