"""
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be
replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters. No two characters may map to
the same character, but a character may map to itself.


Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_idx = [0] * 2**7  # 7-bit ASCII
        t_idx = [0] * 2**7
        for i in range(len(s)):
            if s_idx[ord(s[i])] != t_idx[ord(t[i])]:
                return False
            else:
                s_idx[ord(s[i])] = i + 1
                t_idx[ord(t[i])] = i + 1
        return True


print(Solution().isIsomorphic("egg", "add"))
# True
print(Solution().isIsomorphic("foo", "bar"))
# False
print(Solution().isIsomorphic("paper", "title"))
# True
print(Solution().isIsomorphic("babc", "baba"))
# False
