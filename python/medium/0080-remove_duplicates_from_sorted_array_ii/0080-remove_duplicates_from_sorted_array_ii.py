"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given an integer array nums sorted in non-decreasing order, remove
some duplicates in-place such that each unique element appears at most
twice. The relative order of the elements should be kept the same.

Return k after placing the final result in the first k slots of nums.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]

Explanation: Your function should return k = 5, with the first five
elements of nums being 1, 1, 2, 2 and 3 respectively. It does not
matter what you leave beyond the returned k (hence they are
underscores).
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 2
        while i < len(nums):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


arr = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(arr))
print(arr)
