"""
https://leetcode.com/problems/remove-element

Given an integer array nums and an integer val, remove all occurrences
of val in nums in-place. The order of the elements may be
changed. Then return the number of elements in nums which are not
equal to val.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Explanation: Your function should return k = 2, with the first two
elements of nums being 2. It does not matter what you leave beyond the
returned k (hence they are underscores).

"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = j = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


# nums = [3, 2, 2, 3]
# print(Solution().removeElement(nums, 3))
# print(nums)

nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(Solution().removeElement(nums, 2))
print(nums)
