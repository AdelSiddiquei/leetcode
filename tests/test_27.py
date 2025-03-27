from leetcode_solutions.q27 import Solution

test_input_1 = {"array": [3, 2, 2, 3], "value": 3}
expected_output_1 = {'difcount' : 2, 'array': [2,2,'','']}
test_input_2 = {"array": [0, 1, 2, 2, 3, 0, 4, 2], "value": 2}
expected_output_2 = {'difcount' : 5, 'array': [0,1,4,0,3,2,2,2]}


def test_solution_1():
    solution = Solution()
    
    assert expected_output_1["array"][:1] == solution.solution_1(
        test_input_1["array"], test_input_1["value"]
    )[:solution.difcount-1]
    assert expected_output_1['difcount'] == solution.difcount

    assert expected_output_1["array"][:1] == solution.solution_1(
        test_input_2["array"], test_input_2["value"]
    )[:solution.difcount-1]
    assert expected_output_2['difcount'] == solution.difcount
