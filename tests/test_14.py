from leetcode_solutions.q14 import Solution

test_input_1 = ["flower", "flow", "flight"]
expected_output_1 = "fl"
test_input_2 = ["dog", "racecar", "car"]
expected_output_2 = ""


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(test_input_1)
    assert expected_output_2 == solution.solution_1(test_input_2)
