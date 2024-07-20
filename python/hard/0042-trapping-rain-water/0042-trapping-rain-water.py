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

        def find_valleys(arr, end):
            # Return a list of (left, right) valley tuples, found in
            # arr.  This algo will miss valleys at the end of arr and
            # needs to be re-run on the tail, in reverse.
            valleys = []
            left = right = 0
            i = 1
            while i <= end:
                if left == right:
                    if arr[i] >= arr[left]:
                        # The left side is still climbing and right advances
                        # as well.
                        left = right = i
                    else:
                        # We've just entered into a valley.  Left is frozen
                        # and right advances in descent.
                        right = i
                else:
                    if arr[right] >= arr[left]:
                        # We've just ended a valley.  Save it.
                        valleys.append([left, right])
                        left = right = i - 1
                    else:
                        right = i
                i += 1

            # Run that same alog again in "reverse" for the tail of the
            # heights list; that is, everything after the last found valley.
            # TODO: refactor this if the algo works.
            i = len(arr) - 1

            end = 0
            if valleys:
                end = valleys[-1][1]  # right side of last valley

            left = right = i - 1
            while i >= end:
                if left == right:
                    if arr[i] >= arr[left]:
                        # The left side is still climbing and right advances
                        # as well.
                        left = right = i
                    else:
                        # We've just entered into a valley.  Left is frozen
                        # and right advances in descent.
                        right = i
                else:
                    if arr[right] >= arr[left]:
                        # We've just ended a valley.  Save it.
                        valleys.append([right, left])
                        left = right = i + 1
                    else:
                        right = i
                i -= 1

            return valleys

        capacity = 0
        for left, right in find_valleys(height, len(height) - 1):
            print("adding valley:", left, right)
            capacity += valley_capacity(height, left, right)
        return capacity


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(arr))

# arr = [4, 2, 0, 3, 2, 5]
# print(Solution().trap(arr))

# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# find_valleys(arr, len(arr) - 1)


# from:
#  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#
# to:
# [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
#  [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
#   0  1  2  3  4  5  6  7  8  9 10 11
#         V     V  V  V        V
