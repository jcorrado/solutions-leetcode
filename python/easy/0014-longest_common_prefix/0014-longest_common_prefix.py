"""
https://leetcode.com/problems/longest-common-prefix

Write a function to find the longest common prefix string amongst an
array of strings.

If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        strs.sort(key=len)
        shortest = strs.pop(0)
        required_matches = len(strs)
        for i, char in enumerate(shortest):
            matches = 0
            for str in strs:
                if shortest[i] == str[i]:
                    matches += 1
            if matches == required_matches:
                prefix.append(char)
            else:
                break
        return "".join(prefix)


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
# print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
