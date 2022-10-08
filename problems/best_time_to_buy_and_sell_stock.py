"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.

>>> max_profit([2,1,2,1,0,1,2])
2

>>> max_profit([2,4,1])
2

Example 1:

>>> max_profit([7,1,5,3,6,4])
5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must
buy before you sell.

Example 2:

>>> max_profit([7,6,4,3,1])
0

Explanation: In this case, no transactions are done and the max profit = 0.

>>> max_profit([1,2])
1

>>> max_profit([1,4,2])
3
"""
from typing import List
import doctest


def max_profit(prices: List[int]) -> int:
    """
    Return maximum profit from an array prices
    """
    # check if prices are in descending order
    profit = 0
    left_pointer, right_pointer = 0, 1
    while right_pointer < len(prices):
        current_profit = prices[right_pointer] - prices[left_pointer]
        if current_profit > 0:
            profit = max(current_profit, profit)
        else:
            left_pointer = right_pointer
        right_pointer += 1
    return profit


doctest.testmod()
