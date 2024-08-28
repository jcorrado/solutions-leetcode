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

        if len(s) % 2 != 0:
            return False

        st = []
        for elt in s:
            if elt in opening:
                st.append(elt)
            elif not st or st.pop() != closing[elt]:
                return False

        return not st


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

print(Solution().isValid("){"))
# False
