"""
https://leetcode.com/problems/word-pattern/

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty word in s.


Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        length = len(pattern)

        if length != len(words):
            return False

        mapping = {}
        seen = set()
        for i in range(len(pattern)):
            word = words[i]

            if pattern[i] in mapping:
                if mapping[pattern[i]] != word:
                    return False
            else:
                if word in seen:
                    return False
                else:
                    mapping[pattern[i]] = word
                    seen.add(word)

        return True


print(Solution().wordPattern("abba", "dog cat cat dog"))
# True
print(Solution().wordPattern("abba", "dog cat cat fish"))
# False
print(Solution().wordPattern("aaaa", "dog cat cat dog"))
# False
