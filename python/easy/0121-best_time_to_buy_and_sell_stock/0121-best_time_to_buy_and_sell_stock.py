"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one
stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If
you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is
not allowed because you must buy before you sell.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = max(prices)
        max_profit = 0
        for i in range(0, len(prices)):
            price = prices[i]
            if price < lowest_price:
                lowest_price = price
                profit = max(prices[i:]) - price
                if profit > max_profit:
                    max_profit = profit
        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
