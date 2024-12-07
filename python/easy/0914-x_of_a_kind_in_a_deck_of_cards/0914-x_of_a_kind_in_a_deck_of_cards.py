"""
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

You are given an integer array deck where deck[i] represents the
number written on the ith card.

Partition the cards into one or more groups such that:

* Each group has exactly x cards where x > 1, and

* All the cards in one group have the same integer written on
them.

Return true if such partition is possible, or false otherwise.

Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:
Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
"""

from typing import List
from collections import defaultdict
import math
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = defaultdict(int)
        for n in deck:
            counts[n] = counts[n] + 1
        return reduce(math.gcd, counts.values()) >= 2


print(Solution().hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
# True

print(Solution().hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
# False

print(Solution().hasGroupsSizeX([1]))
# False

print(Solution().hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
# True

print(Solution().hasGroupsSizeX([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]))
# True
