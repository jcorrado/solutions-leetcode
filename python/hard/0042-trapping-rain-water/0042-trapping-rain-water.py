"""
https://leetcode.com/problems/trapping-rain-water

Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after
raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by
array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
(blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        def valley_capacity(arr, left, right):
            # Calculate the capacity of the space between left and
            # right, exclusive.
            capacity = 0
            top = min(arr[left], arr[right])
            i = left + 1
            while i < right:
                capacity += top - arr[i]
                i += 1
            return capacity

        # This strategy will miss valleys at the end of arr and needs
        # to be re-run on the tail, in reverse.  We do that next.
        capacity = 0

        last_right = 0

        left, right = 0, 1
        while right <= len(height) - 1:
            if height[right] >= height[left]:
                if right - left >= 2:
                    # we've just exited a valley
                    capacity += valley_capacity(height, left, right)
                    last_right = right
                left = right
            right += 1

        # Run that same algorithm again in "reverse" for the tail of
        # the heights list; that is, everything after the last found
        # valley, saved in `last_right`.
        start = last_right
        right = len(height) - 1
        left = right - 1
        while left >= start:
            if height[left] >= height[right]:
                if right - left >= 2:
                    capacity += valley_capacity(height, left, right)
                right = left
            left -= 1

        return capacity


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(arr))

arr = [4, 2, 0, 3, 2, 5]
print(Solution().trap(arr))


# from:
#  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#
# to:
# [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
#  [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
#   0  1  2  3  4  5  6  7  8  9 10 11
#         V     V  V  V        V
