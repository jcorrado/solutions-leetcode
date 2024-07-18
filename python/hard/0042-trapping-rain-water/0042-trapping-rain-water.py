"""
https://leetcode.com/problems/trapping-rain-water

Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after
raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by
array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
(blue section) are being trapped.
"""

# height_to_matrix():
#
# from:
#  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#
# to:
# [[0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
#  [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
#  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        def toggle_padding_zeros(arr):
            # Toggle leading and tailing zeros to ones, from passed
            # array, in place.
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    break
            for i in range(len(arr) - 1, -1, -1):
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    break

        count_of_zeros = 0

        # Repeatedly loop through our height list one "layer" at a
        # time.  Imagine expanding a height of three to three rows of
        # one.
        for _ in range(max(height)):
            row = [0 for _ in range(len(height))]
            n = 0
            while n < len(height):
                if height[n] > 0:
                    row[n] = 1
                    height[n] -= 1
                n += 1

            toggle_padding_zeros(row)

            # Remaining zeros represent the negative space between the
            # bars defined in the "height" elevation map, that would
            # accumulate water.
            count_of_zeros += row.count(0)

        return count_of_zeros


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(arr))
