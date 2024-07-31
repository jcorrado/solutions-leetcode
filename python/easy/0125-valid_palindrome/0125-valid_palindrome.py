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
        s = re.sub(r"(?i)[^a-z0-9]", "", s.lower())
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
# True
print(Solution().isPalindrome(" "))
# True
