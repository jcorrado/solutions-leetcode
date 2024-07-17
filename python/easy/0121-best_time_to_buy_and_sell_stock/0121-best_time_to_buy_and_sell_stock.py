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
        max = 0
        tot_prices = len(prices)
        for i in range(0, tot_prices):
            highest_day = 0
            for j in range(i + 1, tot_prices):
                if prices[j] > highest_day:
                    highest_day = prices[j]
            if highest_day - prices[i] > max:
                max = highest_day - prices[i]
        return max


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
