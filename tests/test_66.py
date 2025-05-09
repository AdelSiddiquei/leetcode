from leetcode_solutions.q66 import Solution

# Note that I have added an extra test case compared to the leetcode ones, this is to ensure testing of all edge cases.

test_input_1 = [1,2,3]
expected_output_1 = [1,2,4]
test_input_2 = [4,3,2,1]
expected_output_2 = [4,3,2,2]
test_input_3 = [9]
expected_output_3 = [1,0]
test_input_4 = [9,9,9]
expected_output_4 = [1,0,0,0]


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert expected_output_2 == solution.solution_1(test_input_2)
    assert expected_output_3 == solution.solution_1(test_input_3)
    assert expected_output_4 == solution.solution_1(test_input_4)
