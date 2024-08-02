"""https://leetcode.com/problems/contains-duplicate-ii/

Given an integer array nums and an integer k, return true if there are
two distinct indices i and j in the array such that nums[i] == nums[j]
and abs(i - j) <= k.


Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx_by_value = defaultdict(list)
        for idx, x in enumerate(nums):
            idx_by_value[x].append(idx)

        for idxs in idx_by_value.values():
            length = len(idxs)
            i, j = 0, 1
            while j < length:
                if abs(idxs[j] - idxs[i]) <= k:
                    return True
                i += 1
                j += 1
        return False


print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
# True
print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
# True
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
# False
print(Solution().containsNearbyDuplicate([99, 99], 2))
# True
print(Solution().containsNearbyDuplicate([1, 2, 1], 0))
# False
print(Solution().containsNearbyDuplicate([4, 1, 2, 3, 1, 5], 3))
# True
