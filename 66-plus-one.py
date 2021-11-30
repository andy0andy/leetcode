from typing import List

"""
https://leetcode-cn.com/problems/plus-one/
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits.reverse()
        #
        # plus = 0
        # for i in range(len(digits)):
        #
        #     if plus > 0:
        #         digits[i] += plus
        #         plus = 0
        #
        #     if digits[i] >= 10:
        #         plus = digits[i] // 10
        #         digits[i] %= 10
        #
        #     if i == 0:
        #         if digits[i]+1 >= 10:
        #             digits[i] = digits[i] + 1 - 10
        #             plus = 1
        #         else:
        #             digits[i] += 1
        #
        # if plus > 0:
        #     digits.append(plus)
        #
        # digits.reverse()

        digits = [int(ch) for ch in str(int("".join(list(map(str, digits)))) + 1)]

        return digits


if __name__ == "__main__":
    digits = [9, 9]

    res = Solution().plusOne(digits)

    print(res)