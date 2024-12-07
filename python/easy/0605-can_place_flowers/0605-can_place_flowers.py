"""
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and
some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means
empty and 1 means not empty, and an integer n, return true if n new
flowers can be planted in the flowerbed without violating the
no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def left_ok(bed, i):
            if i == 0:
                return True
            return bed[i - 1] == 0

        def right_ok(bed, i):
            if i == len(bed) - 1:
                return True
            return bed[i + 1] == 0

        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if left_ok(flowerbed, i) and right_ok(flowerbed, i):
                flowerbed[i] = 1
                cnt += 1
        return cnt >= n


print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))
# True
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))
# False
print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
# False
print(Solution().canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0))
# True
print(Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1))
# True
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
# True
