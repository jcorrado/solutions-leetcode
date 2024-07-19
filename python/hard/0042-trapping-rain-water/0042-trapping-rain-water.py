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

# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# print(Solution().trap(arr))

from typing import List


# class Solution:
#     def trap(self, height: List[int]) -> int:

#         capacity = 0

#         def valley_capacity(left, right, arr):
#             # Calculate the capacity of the space between left and
#             # right, exclusive.
#             capacity = 0
#             top = min(arr[left], arr[right])
#             i = left - 1
#             while i < right:
#                 capacity += top - arr[i]
#                 i += 1
#             return capacity


def find_valleys(end, arr):
    # Return a list of (left, right) valley tuples, found in
    # arr.  This algo will miss valleys at the end or arr and
    # needs to be re-run on the tail, in reverse.
    valleys = []

    # Advance valley markers
    i = left = right = 0
    while i <= end:
        if arr[i] >= arr[left]:
            left = right = i
        else:
            right = i

        # Possibly save a newly defined valley
        if right > left + 1 and arr[right] >= arr[left]:
            valleys.append([left, right])

        i += 1

    return valleys


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
find_valleys(len(arr) - 1, arr)
