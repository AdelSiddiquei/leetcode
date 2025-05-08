from leetcode_solutions.q58 import Solution

test_input_1 = "Hello World"
expected_output_1 = 5
test_input_2 = "   fly me   to   the moon  "
expected_output_2 = 4
test_input_3 = "luffy is still joyboy"
expected_output_3 = 6


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert expected_output_2 == solution.solution_1(test_input_2)
    assert expected_output_3 == solution.solution_1(test_input_3)


def test_solution_2():
    solution = Solution()
    assert expected_output_1 == solution.solution_2(test_input_1)
    assert expected_output_2 == solution.solution_2(test_input_2)
    assert expected_output_3 == solution.solution_2(test_input_3)
