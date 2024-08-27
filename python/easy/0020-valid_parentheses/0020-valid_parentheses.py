"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Every close bracket has a corresponding open bracket of the same
  type.

"""


class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")": "(", "}": "{", "]": "["}
        opening = set(closing.values())
        delimeters = []

        for elt in s:
            if elt in opening:
                delimeters.append(elt)
            elif delimeters[-1] == closing[elt]:
                delimeters.pop()
            else:
                return False

        return False if delimeters else True


# Example 1:
print(Solution().isValid("()"))
# True

# Example 2:
print(Solution().isValid("()[]{}"))
# True

# Example 3:
print(Solution().isValid("(]"))
# False

# Example 4:
print(Solution().isValid("([])"))
# True
