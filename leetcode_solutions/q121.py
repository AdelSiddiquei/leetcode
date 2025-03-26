"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""


class Solution:
    def __init__(self):
        self.solution_count = 1  # update as more solutions made

    def solution_1(self, prices):
        """
        Takes a list of prices/numbers and finds the largest profit possible if you buy in at a certain price and sell at a later one.
        Args:
            prices (list): Price list.

        Returns:
            : Largest possible profit
        """
        profit = 0
        for index, price in enumerate(prices):  # index and run loop over price list
            current_price = price
            for future_price in prices[index + 1 :]:
                new_profit = future_price - current_price
                if new_profit > profit:
                    profit = new_profit
        return profit
