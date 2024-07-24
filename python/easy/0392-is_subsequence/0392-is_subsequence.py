"""
https://leetcode.com/problems/is-subsequence

Given two strings s and t, return true if s is a subsequence of t, or
false otherwise.

A subsequence of a string is a new string that is formed from the
original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is
not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        len_s, len_t = len(s), len(t)

        if len_s == 0:
            return True
        if len_s > len_t:
            return False

        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i += 1
            if i == len_s:
                return True
            j += 1
        return False


print(Solution().isSubsequence("abc", "ahbgdc"))
print(Solution().isSubsequence("axc", "ahbgdc"))
