"""
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters
include letters and numbers.

Given a string s, return true if it is a palindrome, or false
otherwise.
 
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        while i <= j:
            ci = ord(s[i])
            cj = ord(s[j])
            # 0-9: 48-57, a-z: 97-122
            if not ((48 <= ci <= 57) or (97 <= ci <= 122)):
                i += 1
            elif not ((48 <= cj <= 57) or (97 <= cj <= 122)):
                j -= 1
            else:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
# True
print(Solution().isPalindrome(" "))
# True
