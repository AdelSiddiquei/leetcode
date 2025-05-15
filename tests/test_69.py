from leetcode_solutions.q69 import Solution

test_input_1 = 4
expected_output_1 = 2
test_input_2 = 8
expected_output_2 = 2
test_input_3 = 10001
expected_output_3 = 100


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert expected_output_2 == solution.solution_1(test_input_2)
    assert expected_output_3 == solution.solution_1(test_input_3)
