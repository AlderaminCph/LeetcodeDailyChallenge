"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
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
import collections
from itertools import compress



def max_profit(prices: List[int]) -> int:
    """
    Return maximum profit from an array prices
    """
    # check if prices are in descending order
    if all(earlier >= later for earlier, later in zip(prices, prices[1:])):
        profit = 0
        return profit

    newprices = collections.deque(prices)
    newprices.appendleft(-1)
    newprices = list(newprices)
    mask = [
        earlier >= later
        for earlier, later in zip(newprices, newprices[1:])
    ]
    if newprices[1] <= newprices[2]:
        mask[0] = True
    if (list(compress(prices, mask)) != []
            and list(compress(prices, mask)).index(
                min(list(compress(prices, mask))))
            != len(list(compress(prices, mask)))):
        min_price = list(compress(prices, mask))[0]
    else:
        min_price = min(prices)
    max_prices = list(
        compress(
            prices,
            [
                earlier <= later
                for earlier, later in zip(newprices, newprices[1:])
            ],
        )
    )
    max_prices.sort()
    max_price = max_prices.pop()
    for i, val in enumerate(prices):
        if val == max_price:
            if i > prices.index(min_price):
                profit = max_price - min_price
                return profit
            max_price = max_prices.pop()


doctest.testmod()
