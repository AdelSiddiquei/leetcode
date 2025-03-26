from leetcode_solutions.q121_best_time_to_buy_and_sell_stock import Solution


def test_case_1():
    prices = [7, 1, 5, 3, 6, 4]
    output = 5
    solution = Solution()
    answer = solution.solution_1(prices)
    assert answer == output


def test_case_2():
    prices = [7, 6, 4, 3, 1]
    output = 0
    solution = Solution()
    answer = solution.solution_1(prices)
    assert answer == output
