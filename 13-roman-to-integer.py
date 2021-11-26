
"""
https://leetcode-cn.com/problems/roman-to-integer/
"""


class Solution:

    def romanToInt(self, s: str) -> int:

        romanMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        if len(s) == 1:
            return romanMap[s]

        res = 0
        i = 0
        while i < len(s):


            if i+1 < len(s) and (romanMap[s[i]] * 5 == romanMap[s[i+1]] or romanMap[s[i]] * 10 == romanMap[s[i+1]]):
                res += romanMap[s[i+1]] - romanMap[s[i]]
                i += 2
            else:
                res += romanMap[s[i]]
                i += 1

        return res





if __name__ == "__main__":

    s = "MCMXCIV"

    Solution().romanToInt(s)
