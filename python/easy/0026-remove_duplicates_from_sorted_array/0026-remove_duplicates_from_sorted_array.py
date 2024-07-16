"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array

Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only
once. The relative order of the elements should be kept the same. Then
return the number of unique elements in nums.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]


Explanation: Your function should return k = 2, with the first two
elements of nums being 1 and 2 respectively. It does not matter what
you leave beyond the returned k (hence they are underscores).

"""

from typing import List


class Solution:

    def _overwrite_left_to(self, arr, pos):
        """
        Shift the contents of arr left, overwriting the contents
        of arr[pos].
        """
        while pos < len(arr) - 1:
            arr[pos] = arr[pos + 1]
            pos += 1

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i = 1
        j = len(nums)
        while i < j:
            # compare to prior elt
            if nums[i] == nums[i - 1]:
                self._overwrite_left_to(nums, i)
                j -= 1
            else:
                i += 1

        return i


arr = [1, 2]
print(Solution().removeDuplicates(arr))
print(arr)
