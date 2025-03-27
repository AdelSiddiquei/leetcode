from leetcode_solutions.q121 import Solution

test_input_1 = [7, 1, 5, 3, 6, 4]
expected_output_1 = 5
test_input_2 = [7, 6, 4, 3, 1]
expected_output_2 = 0


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert expected_output_2 == solution.solution_1(test_input_2)
