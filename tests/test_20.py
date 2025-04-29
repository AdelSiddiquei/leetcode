from leetcode_solutions.q20 import Solution

test_input_1 = "()"
expected_output_1 = True
test_input_2 = r"()[]{}"
expected_output_2 = True
test_input_3 = "(]"
expected_output_3 = False
test_input_4 = "([])"
expected_output_4 = True


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert expected_output_2 == solution.solution_1(test_input_2)
    assert expected_output_3 == solution.solution_1(test_input_3)
    assert expected_output_4 == solution.solution_1(test_input_4)
