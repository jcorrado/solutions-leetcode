"""
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
* Starting with any positive integer, replace the number by the sum of
  the squares of its digits.
* Repeat the process until the number equals 1 (where it will stay),
  or it loops endlessly in a cycle which does not include 1.
* Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.


Example 1:
Input: n = 19
Output: true

Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

Example 2:
Input: n = 2
Output: false
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squared_digits(n):
            accum = 0
            for x in str(n):
                accum += int(x) ** 2
            return accum

        seen = set()
        queue = [n]
        for x in queue:
            x = sum_squared_digits(x)
            if x == 1:
                return True
            elif x in seen:
                return False
            else:
                seen.add(x)
                queue.append(x)

        return True


print(Solution().isHappy(19))
# True
print(Solution().isHappy(2))
# False
