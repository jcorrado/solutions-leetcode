"""
https://leetcode.com/problems/rotate-array

Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

from typing import List


class Solution:

    # Implement with a single array element tmp var

    def rotate(self, nums: List[int], k: int) -> None:
        while k > 0:
            i = len(nums) - 1
            while i >= 1:
                tmp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = tmp
                i -= 1
            k -= 1


nums = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums, 3)
print(nums)
