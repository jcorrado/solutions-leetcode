"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and
false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters
exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_letters(s):
            letters = defaultdict(int)
            for c in s:
                letters[c] += 1
            return letters

        return get_letters(s) == get_letters(t)


print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))
