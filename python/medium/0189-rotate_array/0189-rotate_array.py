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
    def rotate(self, nums: List[int], k: int) -> None:

        def reverse(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        n = len(nums)
        k = k % n
        end = n - 1
        middle = end - k
        reverse(nums, 0, middle)
        reverse(nums, middle + 1, end)
        reverse(nums, 0, end)


nums = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums, 3)
print(nums)

nums = [1, 2]
Solution().rotate(nums, 3)
print(nums)
