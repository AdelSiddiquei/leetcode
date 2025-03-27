from leetcode_solutions.q27 import Solution

test_input_1 = {"array": [3, 2, 2, 3], "value": 3}
expected_output_1 = 2
test_input_2 = {"array": [0, 1, 2, 2, 3, 0, 4, 2], "value": 2}
expected_output_2 = 5


def test_solution_1():
    solution = Solution()
    assert expected_output_1 == solution.solution_1(
        test_input_1["array"], test_input_1["value"]
    )
    assert expected_output_2 == solution.solution_1(
        test_input_2["array"], test_input_2["value"]
    )
