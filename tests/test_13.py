from leetcode_solutions.q13 import Solution

test_input_1 = "III"
expected_output_1 = 3
test_input_2 = "LVIII"
expected_output_2 = 58
test_input_3 = "MCMXCIV"
expected_output_3 = 1994


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert expected_output_2 == solution.solution_1(test_input_2)
    assert expected_output_3 == solution.solution_1(test_input_3)
