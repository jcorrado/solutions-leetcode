"""
https://leetcode.com/problems/roman-to-integer

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        tot, last_n = 0, 0
        for c in s:
            n = numerals[c]
            if last_n < n:
                tot += n - (last_n * 2)
            else:
                tot += n
            last_n = n
        return tot


print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
