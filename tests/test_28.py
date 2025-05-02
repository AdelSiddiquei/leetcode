from leetcode_solutions.q28 import Solution

test_input_1 = ["sadbutsad", "sad"]
expected_output_1 = 0
test_input_2 = ["leetcode", "leeto"]
expected_output_2 = -1


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(*test_input_1)
    assert expected_output_2 == solution.solution_1(*test_input_2)

def test_solution_2():
    solution = Solution()
    assert expected_output_1 == solution.solution_2(*test_input_1)
    assert expected_output_2 == solution.solution_2(*test_input_2)

