
"""
https://leetcode-cn.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False


        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for ch in s:

            if ch in pairs:
                if stack == [] or stack[-1] != pairs[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)

        return stack == []




if __name__ == "__main__":

    s = "(]"

    res = Solution().isValid(s)
    print(res)

