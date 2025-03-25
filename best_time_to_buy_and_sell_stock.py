def max_profit_finder(prices: list) -> float:
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
