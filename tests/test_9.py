from leetcode_solutions.q9 import Solution

test_input_1 = 121
expected_output_1 = True
test_input_2 = -121
expected_output_2 = False
test_input_3 = 10
expected_output_3 = False

def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert expected_output_2 == solution.solution_1(test_input_2)
    assert expected_output_3 == solution.solution_1(test_input_3)