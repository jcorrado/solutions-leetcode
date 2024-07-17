"""
https://leetcode.com/problems/merge-sorted-array

You are given two integer arrays nums1 and nums2, sorted in
non-decreasing order, and two integers m and n, representing the
number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing
order.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].

The result of the merge is [1,2,2,3,5,6] with the underlined elements
coming from nums1.

"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1
        i = len(nums1) - 1
        while i >= 0:
            if m < 0:
                nums1[i] = nums2[n]
                n -= 1
            elif n < 0:
                break
            elif nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1
