from leetcode_solutions.q27 import Solution

test_input_1 = [[3, 2, 2, 3], 3]
expected_output_1 = [[2, 2, "", ""], 2]
test_input_2 = [[0, 1, 2, 2, 3, 0, 4, 2], 2]
expected_output_2 = [[0, 1, 3, 0, 4, 2, 2, 2], 5]


def test_solution_1():
    solution = Solution()
    solution.solution_1(*test_input_1)
    assert solution.difcount == expected_output_1[1]
    assert (
        test_input_1[0][: solution.difcount - 1]
        == expected_output_1[0][: expected_output_1[1] - 1]
    )

    solution.solution_1(*test_input_2)
    assert solution.difcount == expected_output_2[1]
    assert (
        test_input_2[0][: solution.difcount - 1]
        == expected_output_2[0][: expected_output_2[1] - 1]
    )
