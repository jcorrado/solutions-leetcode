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
        def get_pat(s):
            pat = ""
            for w in s.split():
                pat += w[0:1]
            return pat

        def is_isomorphic(s: str, t: str) -> bool:
            s_idx = [0] * 2**7  # 7-bit ASCII
            t_idx = [0] * 2**7
            for i in range(len(s)):
                if s_idx[ord(s[i])] != t_idx[ord(t[i])]:
                    return False
                else:
                    s_idx[ord(s[i])] = i + 1
                    t_idx[ord(t[i])] = i + 1
            return True

        word_pat = get_pat(s)
        if len(pattern) != len(word_pat):
            return False

        return is_isomorphic(pattern, word_pat)


print(Solution().wordPattern("abba", "dog cat cat dog"))
# True
print(Solution().wordPattern("abba", "dog cat cat fish"))
# False
print(Solution().wordPattern("aaaa", "dog cat cat dog"))
# False
