"""
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote
can be constructed by using the letters from magazine and false
otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

"""

from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = defaultdict(int)
        for c in magazine:
            available[c] += 1

        for c in ransomNote:
            if c in available and available[c] > 0:
                available[c] -= 1
            else:
                return False

        return True


print(Solution().canConstruct("a", "b"))
print(Solution().canConstruct("aa", "ab"))
print(Solution().canConstruct("aa", "aab"))
