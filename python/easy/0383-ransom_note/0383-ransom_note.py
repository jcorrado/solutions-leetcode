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
        note_letters = defaultdict(int)
        for c in ransomNote:
            note_letters[c] += 1

        found_letters, needed_letters = 0, len(ransomNote)
        for c in magazine:
            if c in note_letters and note_letters[c] > 0:
                note_letters[c] -= 1
                found_letters += 1
                if found_letters == needed_letters:
                    return True

        return False


print(Solution().canConstruct("a", "b"))
print(Solution().canConstruct("aa", "ab"))
print(Solution().canConstruct("aa", "aab"))
