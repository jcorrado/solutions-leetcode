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


# 0-9: 48-57, a-z: 97-122
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def to_ord(c):
            x = ord(c)
            if 65 <= x <= 90:
                # A-Z, convert to lower case
                return x + 22
            elif 48 <= x <= 57 or 97 <= x <= 122:
                # 0-9 or a-z
                return x
            else:
                return None

        s = s.lower()
        i, j = 0, len(s) - 1
        while i <= j:

            ci = to_ord(s[i])
            if ci is None:
                i += 1
                continue

            cj = to_ord(s[j])
            if cj is None:
                j -= 1
                continue

            if ci != cj:
                return False
            i += 1
            j -= 1

        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
# True
print(Solution().isPalindrome(" "))
# True
