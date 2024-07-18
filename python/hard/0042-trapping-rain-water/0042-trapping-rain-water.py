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

        def height_to_matrix(arr):
            # Return a matrix of zeros and ones representing passed
            # array of heights.
            rows, cols = max(arr), len(arr)
            mat = [[0 for _ in range(cols)] for _ in range(rows)]
            m = 0
            while m < rows:
                n = 0
                while n < cols:
                    if arr[n] > 0:
                        mat[m][n] = 1
                        arr[n] -= 1
                    n += 1
                m += 1
            return mat

        def toggle_padding_zeros(arr):
            # Toggle leading and trailing zeros to ones, from passed
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

        # Remaining zeros represent the negative space (or "cells")
        # between the bars defined in the "height" elevation map, that
        # would accumulate water.
        count_of_zeros = 0
        for row in height_to_matrix(height):
            toggle_padding_zeros(row)
            # print(row)
            for cell in row:
                if cell == 0:
                    count_of_zeros += 1
        return count_of_zeros


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(arr))
